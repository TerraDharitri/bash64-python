////////////////////////////////////////////////////
////////////////// AUTO-GENERATED //////////////////
////////////////////////////////////////////////////

#![no_std]

numbat_wasm_node::wasm_endpoints! {
    basic_features
    (
        callBack
        add_assign_big_int
        add_assign_big_int_ref
        add_assign_big_uint
        add_assign_big_uint_ref
        add_big_int
        add_big_int_ref
        add_big_uint
        add_big_uint_ref
        add_to_whitelist
        big_int_from_biguint
        big_int_from_i64_1
        big_int_from_i64_2
        big_int_to_i64
        big_int_to_parts
        big_int_zero
        big_uint_from_managed_buffer
        big_uint_from_managed_buffer_ref
        big_uint_from_u64_1
        big_uint_from_u64_2
        big_uint_to_u64
        big_uint_zero
        bigint_overwrite_i64
        biguint_overwrite_u64
        bit_and_assign_big_uint
        bit_and_assign_big_uint_ref
        bit_and_big_uint
        bit_and_big_uint_ref
        bit_or_assign_big_uint
        bit_or_assign_big_uint_ref
        bit_or_big_uint
        bit_or_big_uint_ref
        bit_xor_assign_big_uint
        bit_xor_assign_big_uint_ref
        bit_xor_big_uint
        bit_xor_big_uint_ref
        burn_fungible
        check_contains
        clear_single_value_mapper
        clear_storage_value
        codec_err_contract_call
        codec_err_contract_init
        codec_err_event_data
        codec_err_event_topic
        codec_err_finish
        codec_err_storage_get
        codec_err_storage_key
        codec_err_storage_set
        compute_create_ec
        compute_ec_add
        compute_ec_double
        compute_generate_key_ec
        compute_get_ec_length
        compute_get_priv_key_byte_length
        compute_get_values
        compute_is_on_curve_ec
        compute_keccak256
        compute_keccak256_legacy_managed
        compute_marshal_compressed_ec
        compute_marshal_ec
        compute_ripemd160
        compute_scalar_base_mult
        compute_scalar_mult
        compute_secp256k1_der_signature
        compute_sha256
        compute_sha256_legacy_managed
        compute_unmarshal_compressed_ec
        compute_unmarshal_ec
        count_ones
        div_assign_big_int
        div_assign_big_int_ref
        div_assign_big_uint
        div_assign_big_uint_ref
        div_big_int
        div_big_int_ref
        div_big_uint
        div_big_uint_ref
        echo_array_u8
        echo_arrayvec
        echo_big_int
        echo_big_int_managed_vec
        echo_big_int_option
        echo_big_int_tuple
        echo_big_uint
        echo_bool
        echo_i32
        echo_i64
        echo_i8
        echo_isize
        echo_managed_address
        echo_managed_async_result_empty
        echo_managed_buffer
        echo_managed_vec_of_managed_vec
        echo_managed_vec_of_token_identifier
        echo_multi_value_tuples
        echo_multi_value_u32
        echo_non_zero_usize
        echo_nothing
        echo_opt_bool
        echo_ser_example_2
        echo_simple_enum
        echo_some_args_ignore_others
        echo_tuple_into_multiresult
        echo_u32
        echo_u64
        echo_u8
        echo_usize
        echo_varags_managed_eager
        echo_varags_managed_sum
        endpoint_with_mutable_arg
        finish_simple_enum_variant_1
        getFungibleTokenId
        getListMapper
        getNonFungibleTokenId
        get_balance_fungible
        get_block_epoch
        get_block_nonce
        get_block_random_seed
        get_block_round
        get_block_timestamp
        get_caller
        get_cumulated_validator_rewards
        get_gas_left
        get_nr_to_clear
        get_owner_address
        get_prev_block_epoch
        get_prev_block_nonce
        get_prev_block_random_seed
        get_prev_block_round
        get_prev_block_timestamp
        get_shard_of_address
        get_state_root_hash
        get_tx_hash_legacy
        init_unique_id_mapper
        is_empty_opt_addr
        is_empty_single_value_mapper
        is_smart_contract
        issue_and_set_all_roles_fungible
        issue_and_set_all_roles_meta
        issue_fungible_custom_callback
        issue_fungible_default_callback
        listMapperBack
        listMapperFront
        listMapperIterateByHand
        listMapperIterateByIter
        listMapperPopBack
        listMapperPopFront
        listMapperPushAfter
        listMapperPushBack
        listMapperPushBefore
        listMapperPushFront
        listMapperRemoveNode
        listMapperRemoveNodeById
        listMapperSetValue
        listMapperSetValueById
        load_addr
        load_big_int
        load_big_uint
        load_bool
        load_from_address_raw
        load_i64
        load_map1
        load_map2
        load_map3
        load_opt_addr
        load_ser_2
        load_u64
        load_usize
        log2_big_uint
        log2_big_uint_ref
        logEventA
        logEventARepeat
        logEventB
        maddress_from_array
        maddress_from_managed_buffer
        managed_address_eq
        managed_address_zero
        managed_struct_eq
        managed_vec_address_push
        managed_vec_array_push
        managed_vec_biguint_eq
        managed_vec_biguint_push
        managed_vec_contains
        managed_vec_find
        managed_vec_new
        managed_vec_remove
        managed_vec_set
        map_mapper
        map_mapper_contains_key
        map_mapper_entry_and_modify
        map_mapper_entry_or_default_update_increment
        map_mapper_entry_or_insert_default
        map_mapper_entry_or_insert_with_key
        map_mapper_get
        map_mapper_insert
        map_mapper_keys
        map_mapper_remove
        map_mapper_values
        map_my_single_value_mapper
        map_storage_mapper_clear
        map_storage_mapper_contains_key
        map_storage_mapper_entry_and_modify_increment_or_default
        map_storage_mapper_entry_or_default_update
        map_storage_mapper_entry_or_default_update_increment
        map_storage_mapper_get
        map_storage_mapper_get_value
        map_storage_mapper_insert_default
        map_storage_mapper_insert_value
        map_storage_mapper_remove
        map_storage_mapper_view
        mapper_get_token_attributes
        mapper_nft_add_quantity
        mapper_nft_add_quantity_and_send
        mapper_nft_burn
        mapper_nft_create
        mapper_nft_create_and_send
        mapper_nft_get_balance
        mapper_nft_set_token_id
        mbuffer_concat
        mbuffer_copy_slice
        mbuffer_eq
        mbuffer_new
        mbuffer_set_random
        mint_and_send_fungible
        mint_fungible
        mul_assign_big_int
        mul_assign_big_int_ref
        mul_assign_big_uint
        mul_assign_big_uint_ref
        mul_big_int
        mul_big_int_ref
        mul_big_uint
        mul_big_uint_ref
        my_single_value_mapper_increment_1
        my_single_value_mapper_increment_2
        my_single_value_mapper_set_if_empty
        my_single_value_mapper_subtract_with_require
        non_zero_usize_iter
        non_zero_usize_macro
        only_owner_endpoint
        only_user_account_endpoint
        panicWithMessage
        pow_big_int
        pow_big_int_ref
        pow_big_uint
        pow_big_uint_ref
        queue_mapper
        queue_mapper_front
        queue_mapper_pop_front
        queue_mapper_push_back
        raw_byte_length_single_value_mapper
        rem_assign_big_int
        rem_assign_big_int_ref
        rem_assign_big_uint
        rem_assign_big_uint_ref
        rem_big_int
        rem_big_int_ref
        rem_big_uint
        rem_big_uint_ref
        remove_from_whitelist
        require_all_same_token_fungible
        require_contains
        require_equals
        require_same_token_fungible
        sc_panic
        set_local_roles_fungible
        set_mapper
        set_mapper_contains
        set_mapper_insert
        set_mapper_remove
        shl_assign_big_uint
        shl_assign_big_uint_ref
        shl_big_uint
        shl_big_uint_ref
        shr_assign_big_uint
        shr_assign_big_uint_ref
        shr_big_uint
        shr_big_uint_ref
        sqrt_big_uint
        sqrt_big_uint_ref
        storage_read_from_address
        storage_read_raw
        storage_write_raw
        store_addr
        store_big_int
        store_big_uint
        store_bool
        store_i32
        store_i64
        store_map1
        store_map2
        store_map3
        store_opt_addr
        store_reserved_big_uint
        store_reserved_i64
        store_reserved_vec_u8
        store_ser_2
        store_u64
        store_usize
        sub_assign_big_int
        sub_assign_big_int_ref
        sub_assign_big_uint
        sub_assign_big_uint_ref
        sub_big_int
        sub_big_int_ref
        sub_big_uint
        sub_big_uint_ref
        token_attributes_clear
        token_attributes_get_attributes
        token_attributes_get_nonce
        token_attributes_has_attributes
        token_attributes_set
        token_attributes_update
        token_identifier_rewa
        token_identifier_is_valid_1
        token_identifier_is_valid_2
        unique_id_mapper
        unique_id_mapper_get
        unique_id_mapper_set
        unique_id_mapper_swap_remove
        vec_mapper
        vec_mapper_get
        vec_mapper_len
        vec_mapper_push
        verify_bls_signature
        verify_custom_secp256k1_signature
        verify_ed25519_signature
        verify_secp256k1_signature
    )
}
