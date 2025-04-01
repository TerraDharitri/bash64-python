use super::{ErrorApiImpl, Handle, ManagedTypeApiImpl};
use crate::types::DcdtTokenType;

pub trait CallValueApi {
    type CallValueApiImpl: CallValueApiImpl;

    fn call_value_api_impl() -> Self::CallValueApiImpl;
}

pub trait CallValueApiImpl: ErrorApiImpl + ManagedTypeApiImpl + Sized {
    fn check_not_payable(&self);

    /// Retrieves the REWA call value from the VM.
    /// Will return 0 in case of an DCDT transfer (cannot have both REWA and DCDT transfer simultaneously).
    fn load_rewa_value(&self, dest_handle: Handle);

    /// Loads all DCDT call values into a managed vec. Overwrites destination.
    fn load_all_dcdt_transfers(&self, dest_handle: Handle) {
        load_all_dcdt_transfers_from_unmanaged(self, dest_handle);
    }

    fn dcdt_num_transfers(&self) -> usize;

    /// Retrieves the DCDT call value from the VM.
    /// Will return 0 in case of an REWA transfer (cannot have both REWA and DCDT transfer simultaneously).
    fn load_single_dcdt_value(&self, dest_handle: Handle);

    /// Returns the call value token identifier of the current call.
    /// The identifier is wrapped in a TokenIdentifier object, to hide underlying logic.
    ///
    /// A note on implementation: even though the underlying api returns an empty name for REWA,
    /// but the REWA TokenIdentifier is serialized as `REWA`.
    fn token(&self) -> Handle;

    /// Returns the nonce of the received DCDT token.
    /// Will return 0 in case of REWA or fungible DCDT transfer.
    fn dcdt_token_nonce(&self) -> u64;

    /// Returns the DCDT token type.
    /// Will return "Fungible" for REWA.
    fn dcdt_token_type(&self) -> DcdtTokenType;

    fn dcdt_value_by_index(&self, index: usize) -> Handle;

    fn token_by_index(&self, index: usize) -> Handle;

    fn dcdt_token_nonce_by_index(&self, index: usize) -> u64;

    fn dcdt_token_type_by_index(&self, index: usize) -> DcdtTokenType;
}

pub fn load_all_dcdt_transfers_from_unmanaged<A>(api: &A, dest_handle: Handle)
where
    A: CallValueApiImpl,
{
    let num_transfers = api.dcdt_num_transfers();
    api.mb_overwrite(dest_handle, &[]);

    for i in 0..num_transfers {
        let token_identifier_handle = api.token_by_index(i);
        let token_nonce = api.dcdt_token_nonce_by_index(i);
        let amount_handle = api.dcdt_value_by_index(i);

        api.mb_append_bytes(dest_handle, &token_identifier_handle.to_be_bytes()[..]);
        api.mb_append_bytes(dest_handle, &token_nonce.to_be_bytes()[..]);
        api.mb_append_bytes(dest_handle, &amount_handle.to_be_bytes()[..]);
    }
}
