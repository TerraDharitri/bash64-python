use core::marker::PhantomData;

use crate::{
    api::{
        const_handles, CallValueApi, CallValueApiImpl, ErrorApi, ErrorApiImpl, ManagedBufferApi,
        ManagedTypeApi,
    },
    err_msg,
    types::{BigUint, DcdtTokenPayment, DcdtTokenType, ManagedType, ManagedVec, TokenIdentifier},
};

#[derive(Default)]
pub struct CallValueWrapper<A>
where
    A: CallValueApi + ErrorApi + ManagedTypeApi,
{
    _phantom: PhantomData<A>,
}

impl<A> CallValueWrapper<A>
where
    A: CallValueApi + ErrorApi + ManagedTypeApi,
{
    pub fn new() -> Self {
        CallValueWrapper {
            _phantom: PhantomData,
        }
    }

    /// Retrieves the REWA call value from the VM.
    /// Will return 0 in case of an DCDT transfer (cannot have both REWA and DCDT transfer simultaneously).
    pub fn rewa_value(&self) -> BigUint<A> {
        A::call_value_api_impl().load_rewa_value(const_handles::CALL_VALUE_REWA);
        BigUint::from_raw_handle(const_handles::CALL_VALUE_REWA) // unsafe, TODO: replace with ManagedRef<...>
    }

    /// Returns all DCDT transfers that accompany this SC call.
    /// Will return 0 results if nothing was transfered, or just REWA.
    /// Fully managed underlying types, very efficient.
    pub fn all_dcdt_transfers(&self) -> ManagedVec<A, DcdtTokenPayment<A>> {
        A::call_value_api_impl().load_all_dcdt_transfers(const_handles::CALL_VALUE_MULTI_DCDT);
        ManagedVec::from_raw_handle(const_handles::CALL_VALUE_MULTI_DCDT) // unsafe, TODO: replace with ManagedRef<...>
    }

    /// Retrieves the DCDT call value from the VM.
    /// Will return 0 in case of an REWA transfer (cannot have both REWA and DCDT transfer simultaneously).
    /// Warning, not tested with multi transfer, use `all_dcdt_transfers` instead!
    pub fn dcdt_value(&self) -> BigUint<A> {
        A::call_value_api_impl().load_single_dcdt_value(const_handles::CALL_VALUE_SINGLE_DCDT);
        BigUint::from_raw_handle(const_handles::CALL_VALUE_SINGLE_DCDT)
    }

    /// Returns the call value token identifier of the current call.
    /// The identifier is wrapped in a TokenIdentifier object, to hide underlying logic.
    ///
    /// A note on implementation: even though the underlying api returns an empty name for REWA,
    /// but the REWA TokenIdentifier is serialized as `REWA`.
    /// Warning, not tested with multi transfer, use `all_dcdt_transfers` instead!
    pub fn token(&self) -> TokenIdentifier<A> {
        let call_value_api = A::call_value_api_impl();
        if call_value_api.dcdt_num_transfers() == 0 {
            TokenIdentifier::rewa()
        } else {
            TokenIdentifier::from_raw_handle(call_value_api.token())
        }
    }

    /// Returns the nonce of the received DCDT token.
    /// Will return 0 in case of REWA or fungible DCDT transfer.
    /// Warning, not tested with multi transfer, use `all_dcdt_transfers` instead!
    pub fn dcdt_token_nonce(&self) -> u64 {
        let call_value_api = A::call_value_api_impl();
        if call_value_api.dcdt_num_transfers() > 0 {
            call_value_api.dcdt_token_nonce()
        } else {
            0
        }
    }

    /// Returns the DCDT token type.
    /// Will return "Fungible" for REWA.
    /// Warning, not tested with multi transfer, use `all_dcdt_transfers` instead!
    pub fn dcdt_token_type(&self) -> DcdtTokenType {
        let call_value_api = A::call_value_api_impl();
        if call_value_api.dcdt_num_transfers() > 0 {
            A::call_value_api_impl().dcdt_token_type()
        } else {
            DcdtTokenType::Fungible
        }
    }

    pub fn require_rewa(&self) -> BigUint<A> {
        let call_value_api = A::call_value_api_impl();
        if call_value_api.dcdt_num_transfers() > 0 {
            A::error_api_impl().signal_error(err_msg::NON_PAYABLE_FUNC_DCDT.as_bytes());
        }

        self.rewa_value()
    }

    pub fn require_dcdt(&self, token: &[u8]) -> BigUint<A> {
        let m_api = A::managed_type_impl();
        let call_value_api = A::call_value_api_impl();
        let error_api = A::error_api_impl();

        let expected_token_handle = const_handles::MBUF_TEMPORARY_1;
        m_api.mb_overwrite(expected_token_handle, token);
        if call_value_api.dcdt_num_transfers() != 1 {
            error_api.signal_error(err_msg::SINGLE_DCDT_EXPECTED.as_bytes());
        }
        if !m_api.mb_eq(call_value_api.token(), expected_token_handle) {
            error_api.signal_error(err_msg::BAD_TOKEN_PROVIDED.as_bytes());
        }
        call_value_api.load_single_dcdt_value(const_handles::CALL_VALUE_SINGLE_DCDT);
        BigUint::from_raw_handle(const_handles::CALL_VALUE_SINGLE_DCDT)
    }

    /// Returns both the call value (either REWA or DCDT) and the token identifier.
    /// Especially used in the `#[payable("*")] auto-generated snippets.
    /// TODO: replace with multi transfer handling everywhere
    pub fn payment_token_pair(&self) -> (BigUint<A>, TokenIdentifier<A>) {
        let call_value_api = A::call_value_api_impl();
        if call_value_api.dcdt_num_transfers() == 0 {
            (self.rewa_value(), TokenIdentifier::rewa())
        } else {
            (self.dcdt_value(), self.token())
        }
    }

    pub fn payment(&self) -> DcdtTokenPayment<A> {
        let api = A::call_value_api_impl();
        if api.dcdt_num_transfers() == 0 {
            DcdtTokenPayment::new(TokenIdentifier::rewa(), 0, self.rewa_value())
        } else {
            DcdtTokenPayment::new(self.token(), self.dcdt_token_nonce(), self.dcdt_value())
        }
    }

    pub fn payment_as_tuple(&self) -> (TokenIdentifier<A>, u64, BigUint<A>) {
        let (amount, token) = self.payment_token_pair();
        let nonce = self.dcdt_token_nonce();

        (token, nonce, amount)
    }
}
