use numbat_wasm::{
    numbat_codec::{CodecFrom, TopEncodeMulti},
    types::ContractCall,
};

use crate::{
    denali_system::model::{AddressValue, BytesValue, TxExpect, TxQuery},
    DebugApi,
};

use super::{format_expect, process_contract_call};

#[derive(Debug, Default)]
pub struct ScQueryStep {
    pub tx_id: String,
    pub comment: Option<String>,
    pub tx: Box<TxQuery>,
    pub expect: Option<TxExpect>,
}

impl ScQueryStep {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn to<A>(mut self, address: A) -> Self
    where
        AddressValue: From<A>,
    {
        self.tx.to = AddressValue::from(address);
        self
    }

    pub fn function(mut self, expr: &str) -> Self {
        self.tx.function = expr.to_string();
        self
    }

    pub fn argument(mut self, expr: &str) -> Self {
        self.tx.arguments.push(BytesValue::from(expr));
        self
    }

    pub fn expect(mut self, expect: TxExpect) -> Self {
        self.expect = Some(expect);
        self
    }

    /// Sets following fields based on the smart contract proxy:
    /// - "to"
    /// - "function"
    /// - "arguments"
    pub fn call<OriginalResult>(
        mut self,
        contract_call: ContractCall<DebugApi, OriginalResult>,
    ) -> Self {
        let (to_str, function, denali_args) = process_contract_call(contract_call);
        self = self.to(to_str.as_str());
        self = self.function(function.as_str());
        for arg in denali_args {
            self = self.argument(arg.as_str());
        }
        self
    }

    /// Sets following fields based on the smart contract proxy:
    /// - "to"
    /// - "function"
    /// - "arguments"
    /// - "expect"
    ///     - "out"
    ///     - "status" set to 0
    pub fn call_expect<OriginalResult, ExpectedResult>(
        mut self,
        contract_call: ContractCall<DebugApi, OriginalResult>,
        expect_value: ExpectedResult,
    ) -> Self
    where
        OriginalResult: TopEncodeMulti,
        ExpectedResult: CodecFrom<OriginalResult> + TopEncodeMulti,
    {
        self = self.call(contract_call);
        self = self.expect(format_expect(expect_value));
        self
    }
}
