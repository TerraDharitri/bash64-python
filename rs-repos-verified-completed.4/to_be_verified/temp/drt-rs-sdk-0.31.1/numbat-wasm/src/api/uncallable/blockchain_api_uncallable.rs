use alloc::boxed::Box;

use crate::{
    api::{BlockchainApi, BlockchainApiImpl, Handle, ManagedTypeApi},
    types::{
        heap::{Address, H256},
        DcdtTokenData, ManagedAddress, TokenIdentifier,
    },
};

use super::UncallableApi;

impl BlockchainApi for UncallableApi {
    type BlockchainApiImpl = UncallableApi;

    fn blockchain_api_impl() -> Self::BlockchainApiImpl {
        unreachable!()
    }
}

impl BlockchainApiImpl for UncallableApi {
    fn get_sc_address_legacy(&self) -> Address {
        unreachable!()
    }

    fn get_owner_address_legacy(&self) -> Address {
        unreachable!()
    }

    fn get_shard_of_address_legacy(&self, _address: &Address) -> u32 {
        unreachable!()
    }

    fn is_smart_contract_legacy(&self, _address: &Address) -> bool {
        unreachable!()
    }

    fn get_caller_legacy(&self) -> Address {
        unreachable!()
    }

    fn load_balance_legacy(&self, _dest: Handle, _address: &Address) {
        unreachable!()
    }

    fn get_state_root_hash_legacy(&self) -> H256 {
        unreachable!()
    }

    fn get_tx_hash_legacy(&self) -> H256 {
        unreachable!()
    }

    fn get_gas_left(&self) -> u64 {
        unreachable!()
    }

    fn get_block_timestamp(&self) -> u64 {
        unreachable!()
    }

    fn get_block_nonce(&self) -> u64 {
        unreachable!()
    }

    fn get_block_round(&self) -> u64 {
        unreachable!()
    }

    fn get_block_epoch(&self) -> u64 {
        unreachable!()
    }

    fn get_block_random_seed_legacy(&self) -> Box<[u8; 48]> {
        unreachable!()
    }

    fn get_prev_block_timestamp(&self) -> u64 {
        unreachable!()
    }

    fn get_prev_block_nonce(&self) -> u64 {
        unreachable!()
    }

    fn get_prev_block_round(&self) -> u64 {
        unreachable!()
    }

    fn get_prev_block_epoch(&self) -> u64 {
        unreachable!()
    }

    fn get_prev_block_random_seed_legacy(&self) -> Box<[u8; 48]> {
        unreachable!()
    }

    fn get_current_dcdt_nft_nonce(&self, _address_handle: Handle, _token_id_handle: Handle) -> u64 {
        unreachable!()
    }

    fn load_dcdt_balance(
        &self,
        _address_handle: Handle,
        _token_id_handle: Handle,
        _nonce: u64,
        _dest: Handle,
    ) {
        unreachable!()
    }

    fn get_dcdt_token_data<M: ManagedTypeApi>(
        &self,
        _address: &ManagedAddress<M>,
        _token: &TokenIdentifier<M>,
        _nonce: u64,
    ) -> DcdtTokenData<M> {
        unreachable!()
    }

    fn get_dcdt_token_data_unmanaged<M: ManagedTypeApi>(
        &self,
        _address: &ManagedAddress<M>,
        _token: &TokenIdentifier<M>,
        _nonce: u64,
    ) -> DcdtTokenData<M> {
        unreachable!()
    }

    fn get_dcdt_local_roles(&self, _token_id_handle: Handle) -> crate::types::DcdtLocalRoleFlags {
        unreachable!()
    }
}
