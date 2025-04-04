use crate::{
    tx_execution::default_execution,
    tx_mock::{BlockchainUpdate, TxCache, TxInput, TxResult},
};

use super::{
    change_owner_mock::execute_change_owner, dcdt_local_burn::execute_local_burn,
    dcdt_local_mint::execute_local_mint, dcdt_multi_transfer_mock::execute_dcdt_multi_transfer,
    dcdt_nft_add_quantity_mock::execute_nft_add_quantity,
    dcdt_nft_add_uri_mock::execute_nft_add_uri, dcdt_nft_burn_mock::execute_nft_burn,
    dcdt_nft_create_mock::execute_dcdt_nft_create,
    dcdt_nft_transfer_mock::execute_dcdt_nft_transfer,
    dcdt_nft_update_attriutes_mock::execute_dcdt_nft_update_attriutes,
    dcdt_transfer_mock::execute_dcdt_transfer, set_username_mock::execute_set_username,
    upgrade_contract::execute_upgrade_contract,
};

use numbat_wasm::api::{
    CHANGE_OWNER_BUILTIN_FUNC_NAME, DCDT_LOCAL_BURN_FUNC_NAME, DCDT_LOCAL_MINT_FUNC_NAME,
    DCDT_MULTI_TRANSFER_FUNC_NAME, DCDT_NFT_ADD_QUANTITY_FUNC_NAME, DCDT_NFT_ADD_URI_FUNC_NAME,
    DCDT_NFT_BURN_FUNC_NAME, DCDT_NFT_CREATE_FUNC_NAME, DCDT_NFT_TRANSFER_FUNC_NAME,
    DCDT_NFT_UPDATE_ATTRIBUTES_FUNC_NAME, DCDT_TRANSFER_FUNC_NAME, SET_USERNAME_FUNC_NAME,
    UPGRADE_CONTRACT_FUNC_NAME,
};

const DCDT_ROLE_LOCAL_MINT: &[u8] = b"DCDTRoleLocalMint";
const DCDT_ROLE_LOCAL_BURN: &[u8] = b"DCDTRoleLocalBurn";
const DCDT_ROLE_NFT_CREATE: &[u8] = b"DCDTRoleNFTCreate";
const DCDT_ROLE_NFT_ADD_QUANTITY: &[u8] = b"DCDTRoleNFTAddQuantity";
const DCDT_ROLE_NFT_BURN: &[u8] = b"DCDTRoleNFTBurn";
const DCDT_ROLE_NFT_ADD_URI: &[u8] = b"DCDTRoleNFTAddURI";
const DCDT_ROLE_NFT_UPDATE_ATTRIBUTES: &[u8] = b"DCDTRoleNFTUpdateAttributes";

pub fn execute_builtin_function_or_default(
    tx_input: TxInput,
    tx_cache: TxCache,
) -> (TxResult, BlockchainUpdate) {
    match tx_input.func_name.as_slice() {
        DCDT_LOCAL_MINT_FUNC_NAME => check_and_execute_builtin_function(
            DCDT_ROLE_LOCAL_MINT,
            tx_input,
            tx_cache,
            &execute_local_mint,
        ),
        DCDT_LOCAL_BURN_FUNC_NAME => check_and_execute_builtin_function(
            DCDT_ROLE_LOCAL_BURN,
            tx_input,
            tx_cache,
            &execute_local_burn,
        ),
        DCDT_MULTI_TRANSFER_FUNC_NAME => execute_dcdt_multi_transfer(tx_input, tx_cache),
        DCDT_NFT_TRANSFER_FUNC_NAME => execute_dcdt_nft_transfer(tx_input, tx_cache),
        DCDT_NFT_CREATE_FUNC_NAME => check_and_execute_builtin_function(
            DCDT_ROLE_NFT_CREATE,
            tx_input,
            tx_cache,
            &execute_dcdt_nft_create,
        ),
        DCDT_NFT_ADD_QUANTITY_FUNC_NAME => check_and_execute_builtin_function(
            DCDT_ROLE_NFT_ADD_QUANTITY,
            tx_input,
            tx_cache,
            &execute_nft_add_quantity,
        ),
        DCDT_NFT_BURN_FUNC_NAME => check_and_execute_builtin_function(
            DCDT_ROLE_NFT_BURN,
            tx_input,
            tx_cache,
            &execute_nft_burn,
        ),
        DCDT_NFT_ADD_URI_FUNC_NAME => check_and_execute_builtin_function(
            DCDT_ROLE_NFT_ADD_URI,
            tx_input,
            tx_cache,
            &execute_nft_add_uri,
        ),
        DCDT_NFT_UPDATE_ATTRIBUTES_FUNC_NAME => check_and_execute_builtin_function(
            DCDT_ROLE_NFT_UPDATE_ATTRIBUTES,
            tx_input,
            tx_cache,
            &execute_dcdt_nft_update_attriutes,
        ),

        DCDT_TRANSFER_FUNC_NAME => execute_dcdt_transfer(tx_input, tx_cache),
        CHANGE_OWNER_BUILTIN_FUNC_NAME => execute_change_owner(tx_input, tx_cache),
        SET_USERNAME_FUNC_NAME => execute_set_username(tx_input, tx_cache),
        UPGRADE_CONTRACT_FUNC_NAME => execute_upgrade_contract(tx_input, tx_cache),
        _ => default_execution(tx_input, tx_cache),
    }
}

fn check_and_execute_builtin_function(
    role_name: &[u8],
    tx_input: TxInput,
    tx_cache: TxCache,
    f: &dyn Fn(TxInput, TxCache) -> (TxResult, BlockchainUpdate),
) -> (TxResult, BlockchainUpdate) {
    let check_result = check_allowed_to_execute(role_name, &tx_input, &tx_cache);
    if let Some(tx_result) = check_result {
        return (tx_result, BlockchainUpdate::empty());
    }
    f(tx_input, tx_cache)
}

pub fn check_allowed_to_execute(
    builtin_function_name: &[u8],
    tx_input: &TxInput,
    tx_cache: &TxCache,
) -> Option<TxResult> {
    let token_identifier = tx_input.args[0].clone();
    let available_roles = tx_cache.with_account_mut(&tx_input.to, |account| {
        account.dcdt.get_roles(&token_identifier)
    });
    if available_roles.contains(&builtin_function_name.to_vec()) {
        return None;
    }

    Some(TxResult::from_vm_error("action is not allowed".to_string()))
}
