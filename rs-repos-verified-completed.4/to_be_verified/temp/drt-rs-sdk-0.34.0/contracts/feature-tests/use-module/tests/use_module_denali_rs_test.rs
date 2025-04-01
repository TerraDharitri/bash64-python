mod user_builtin {
    numbat_wasm::imports!();

    #[numbat_wasm::proxy]
    pub trait UserBuiltin {
        #[endpoint(SetUserName)]
        fn set_user_name(&self, name: &BoxedBytes) -> BigUint;
    }
}

mod dns_mock {
    numbat_wasm::imports!();

    #[numbat_wasm::contract]
    pub trait DnsMock {
        #[proxy]
        fn user_builtin_proxy(&self, to: ManagedAddress) -> super::user_builtin::Proxy<Self::Api>;

        #[payable("REWA")]
        #[endpoint]
        fn register(&self, name: BoxedBytes) {
            let _payment = self.call_value().rewa_value();
            let address = self.blockchain().get_caller();
            self.user_builtin_proxy(address)
                .set_user_name(&name)
                .async_call()
                .call_and_exit()
        }
    }
}

use numbat_wasm_debug::*;

fn world() -> BlockchainMock {
    let mut blockchain = BlockchainMock::new();
    blockchain
        .register_contract_builder("file:output/use-module.wasm", use_module::ContractBuilder);

    blockchain.register_contract_builder(
        "file:test-wasm/numbat-wasm-sc-dns.wasm",
        dns_mock::ContractBuilder,
    );

    blockchain
}

#[test]
fn use_module_dns_register_rs() {
    numbat_wasm_debug::denali_rs("denali/use_module_dns_register.scen.json", world());
}

#[test]
fn use_module_features_rs() {
    numbat_wasm_debug::denali_rs("denali/use_module_features.scen.json", world());
}

#[test]
fn use_module_internal_rs() {
    numbat_wasm_debug::denali_rs("denali/use_module_internal.scen.json", world());
}

#[test]
fn use_module_no_endpoint_rs() {
    numbat_wasm_debug::denali_rs("denali/use_module_no_endpoint.scen.json", world());
}

#[test]
fn use_module_pause_rs() {
    numbat_wasm_debug::denali_rs("denali/use_module_pause.scen.json", world());
}
