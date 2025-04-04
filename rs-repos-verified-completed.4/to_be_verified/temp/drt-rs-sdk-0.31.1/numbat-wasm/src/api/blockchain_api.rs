use super::{Handle, ManagedTypeApi, ManagedTypeApiImpl};
use crate::types::{
    heap::{Address, Box, H256},
    DcdtLocalRoleFlags, DcdtTokenData, ManagedAddress, TokenIdentifier,
};

pub trait BlockchainApi: ManagedTypeApi {
    type BlockchainApiImpl: BlockchainApiImpl;

    fn blockchain_api_impl() -> Self::BlockchainApiImpl;
}

/// Interface to be used by the actual smart contract code.
///
/// Note: contracts and the api are not mutable.
/// They simply pass on/retrieve data to/from the protocol.
/// When mocking the blockchain state, we use the Rc/RefCell pattern
/// to isolate mock state mutability from the contract interface.
pub trait BlockchainApiImpl: ManagedTypeApiImpl {
    fn get_caller_legacy(&self) -> Address;

    fn load_caller_managed(&self, dest: Handle) {
        self.mb_overwrite(dest, self.get_caller_legacy().as_bytes());
    }

    fn get_sc_address_legacy(&self) -> Address;

    fn load_sc_address_managed(&self, dest: Handle) {
        self.mb_overwrite(dest, self.get_sc_address_legacy().as_bytes())
    }

    fn get_owner_address_legacy(&self) -> Address;

    fn load_owner_address_managed(&self, dest: Handle) {
        self.mb_overwrite(dest, self.get_owner_address_legacy().as_bytes())
    }

    fn get_shard_of_address_legacy(&self, address: &Address) -> u32;

    fn get_shard_of_address(&self, address_handle: Handle) -> u32 {
        let mut address = Address::zero();
        let _ = self.mb_load_slice(address_handle, 0, address.as_mut());
        self.get_shard_of_address_legacy(&address)
    }

    fn is_smart_contract_legacy(&self, address: &Address) -> bool;

    fn is_smart_contract(&self, address_handle: Handle) -> bool {
        let mut address = Address::zero();
        let _ = self.mb_load_slice(address_handle, 0, address.as_mut());
        self.is_smart_contract_legacy(&address)
    }

    fn load_balance_legacy(&self, dest: Handle, address: &Address);

    fn load_balance(&self, dest: Handle, address_handle: Handle) {
        let mut address = Address::zero();
        let _ = self.mb_load_slice(address_handle, 0, address.as_mut());
        self.load_balance_legacy(dest, &address);
    }

    fn get_state_root_hash_legacy(&self) -> H256;

    fn load_state_root_hash_managed(&self, dest: Handle) {
        self.mb_overwrite(dest, self.get_state_root_hash_legacy().as_bytes());
    }

    fn get_tx_hash_legacy(&self) -> H256;

    fn load_tx_hash_managed(&self, dest: Handle) {
        self.mb_overwrite(dest, self.get_tx_hash_legacy().as_bytes());
    }

    fn get_gas_left(&self) -> u64;

    fn get_block_timestamp(&self) -> u64;

    fn get_block_nonce(&self) -> u64;

    fn get_block_round(&self) -> u64;

    fn get_block_epoch(&self) -> u64;

    fn get_block_random_seed_legacy(&self) -> Box<[u8; 48]>;

    fn load_block_random_seed_managed(&self, dest: Handle) {
        self.mb_overwrite(dest, &*self.get_block_random_seed_legacy());
    }

    fn get_prev_block_timestamp(&self) -> u64;

    fn get_prev_block_nonce(&self) -> u64;

    fn get_prev_block_round(&self) -> u64;

    fn get_prev_block_epoch(&self) -> u64;

    fn get_prev_block_random_seed_legacy(&self) -> Box<[u8; 48]>;

    fn load_prev_block_random_seed_managed(&self, dest: Handle) {
        self.mb_overwrite(dest, &*self.get_prev_block_random_seed_legacy());
    }

    fn get_current_dcdt_nft_nonce(&self, address_handle: Handle, token_id_handle: Handle) -> u64;

    fn load_dcdt_balance(
        &self,
        address_handle: Handle,
        token_id_handle: Handle,
        nonce: u64,
        dest: Handle,
    );

    fn get_dcdt_token_data<M: ManagedTypeApi>(
        &self,
        address: &ManagedAddress<M>,
        token_id: &TokenIdentifier<M>,
        nonce: u64,
    ) -> DcdtTokenData<M>;

    #[deprecated(
        since = "0.31.1",
        note = "Only used for ;imited backwards compatibility tests. Never use! Use `get_dcdt_token_data` instead."
    )]
    fn get_dcdt_token_data_unmanaged<M: ManagedTypeApi>(
        &self,
        address: &ManagedAddress<M>,
        token_id: &TokenIdentifier<M>,
        nonce: u64,
    ) -> DcdtTokenData<M>;

    fn get_dcdt_local_roles(&self, token_id_handle: Handle) -> DcdtLocalRoleFlags;
}
