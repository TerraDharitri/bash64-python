use numbat_wasm_debug::{denali_system::model::*, *};
use rust_testing_framework_tester::*; // TODO: clean up imports

const WASM_PATH_EXPR: &'static str = "file:output/rust-testing-framework-tester.wasm";

fn world() -> BlockchainMock {
    let mut blockchain = BlockchainMock::new();
    blockchain
        .set_current_dir_from_workspace("contracts/feature_tests/rust-testing-framework-tester");

    blockchain.register_contract_builder(
        WASM_PATH_EXPR,
        rust_testing_framework_tester::ContractBuilder,
    );
    blockchain
}

#[test]
fn tester_deploy_test() {
    let _ = DebugApi::dummy();
    let mut world = world();
    let ic = world.interpreter_context();

    let owner_address = "address:owner";
    let mut adder_contract =
        ContractInfo::<rust_testing_framework_tester::Proxy<DebugApi>>::new("sc:contract");

    world.denali_set_state(
        SetStateStep::new()
            .put_account(owner_address, Account::new())
            .new_address(owner_address, 0, &adder_contract),
    );

    // deploy
    let (new_address, result): (_, String) = adder_contract
        .init()
        .into_blockchain_call()
        .from(owner_address)
        .contract_code(WASM_PATH_EXPR, &ic)
        .gas_limit("5,000,000")
        .execute(&mut world);
    assert_eq!(new_address, adder_contract.to_address());
    assert_eq!(result, "constructor-result");

    world.write_denali_trace("denali/trace-deploy.scen.json");
}
