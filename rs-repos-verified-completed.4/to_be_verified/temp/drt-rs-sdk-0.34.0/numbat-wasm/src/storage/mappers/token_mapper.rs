use crate::{
    api::{CallTypeApi, ErrorApiImpl, StorageMapperApi},
    contract_base::BlockchainWrapper,
    dcdt::DCDTSystemSmartContractProxy,
    storage::StorageKey,
    storage_get, storage_get_len, storage_set,
    types::{
        CallbackClosure, DcdtLocalRole, DcdtTokenPayment, ManagedAddress, ManagedRef, ManagedVec,
        TokenIdentifier,
    },
};

pub(crate) const TOKEN_ID_ALREADY_SET_ERR_MSG: &[u8] = b"Token ID already set";
pub(crate) const MUST_SET_TOKEN_ID_ERR_MSG: &[u8] = b"Must issue or set token ID first";
pub(crate) const INVALID_TOKEN_ID_ERR_MSG: &[u8] = b"Invalid token ID";
pub(crate) const INVALID_PAYMENT_TOKEN_ERR_MSG: &[u8] = b"Invalid payment token";

pub trait StorageTokenWrapper<SA>
where
    SA: StorageMapperApi + CallTypeApi,
{
    fn get_storage_key(&self) -> ManagedRef<SA, StorageKey<SA>>;

    fn is_empty(&self) -> bool {
        storage_get_len(self.get_storage_key()) == 0
    }

    fn get_token_id(&self) -> TokenIdentifier<SA> {
        storage_get(self.get_storage_key())
    }

    fn set_token_id(&self, token_id: &TokenIdentifier<SA>) {
        if !self.is_empty() {
            SA::error_api_impl().signal_error(TOKEN_ID_ALREADY_SET_ERR_MSG);
        }
        if !token_id.is_valid_dcdt_identifier() {
            SA::error_api_impl().signal_error(INVALID_TOKEN_ID_ERR_MSG);
        }

        storage_set(self.get_storage_key(), token_id);
    }

    fn require_same_token(&self, expected_token_id: &TokenIdentifier<SA>) {
        let actual_token_id = self.get_token_id();
        if &actual_token_id != expected_token_id {
            SA::error_api_impl().signal_error(INVALID_PAYMENT_TOKEN_ERR_MSG);
        }
    }

    fn require_all_same_token(&self, payments: &ManagedVec<SA, DcdtTokenPayment<SA>>) {
        let actual_token_id = self.get_token_id();
        for p in payments {
            if actual_token_id != p.token_identifier {
                SA::error_api_impl().signal_error(INVALID_PAYMENT_TOKEN_ERR_MSG);
            }
        }
    }

    fn set_local_roles(
        &self,
        roles: &[DcdtLocalRole],
        opt_callback: Option<CallbackClosure<SA>>,
    ) -> ! {
        let own_sc_address = Self::get_sc_address();
        self.set_local_roles_for_address(&own_sc_address, roles, opt_callback);
    }

    fn set_local_roles_for_address(
        &self,
        address: &ManagedAddress<SA>,
        roles: &[DcdtLocalRole],
        opt_callback: Option<CallbackClosure<SA>>,
    ) -> ! {
        if self.is_empty() {
            SA::error_api_impl().signal_error(MUST_SET_TOKEN_ID_ERR_MSG);
        }

        let system_sc_proxy = DCDTSystemSmartContractProxy::<SA>::new_proxy_obj();
        let token_id = self.get_token_id();
        let mut async_call = system_sc_proxy
            .set_special_roles(address, &token_id, roles[..].iter().cloned())
            .async_call();

        if let Some(cb) = opt_callback {
            async_call = async_call.with_callback(cb);
        }

        async_call.call_and_exit();
    }

    fn get_sc_address() -> ManagedAddress<SA> {
        let b_wrapper = BlockchainWrapper::new();
        b_wrapper.get_sc_address()
    }
}
