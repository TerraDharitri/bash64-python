use crate::denali_system::model::{AddressValue, BigUintValue, U64Value};
use denali::{
    interpret_trait::{InterpretableFrom, InterpreterContext, IntoRaw},
    serde_raw::TxTransferRaw,
};

use super::{tx_interpret_util::interpret_rewa_value, TxCall, TxDCDT};

#[derive(Debug, Default)]
pub struct TxTransfer {
    pub from: AddressValue,
    pub to: AddressValue,
    pub rewa_value: BigUintValue,
    pub dcdt_value: Vec<TxDCDT>,
    pub gas_limit: U64Value,
    pub gas_price: U64Value,
}

impl InterpretableFrom<TxTransferRaw> for TxTransfer {
    fn interpret_from(from: TxTransferRaw, context: &InterpreterContext) -> Self {
        TxTransfer {
            from: AddressValue::interpret_from(from.from, context),
            to: AddressValue::interpret_from(from.to, context),
            rewa_value: interpret_rewa_value(from.value, from.rewa_value, context),
            dcdt_value: from
                .dcdt_value
                .iter()
                .map(|dcdt_value| TxDCDT::interpret_from(dcdt_value.clone(), context))
                .collect(),
            gas_limit: U64Value::interpret_from(from.gas_limit.unwrap_or_default(), context),
            gas_price: U64Value::interpret_from(from.gas_price.unwrap_or_default(), context),
        }
    }
}

impl IntoRaw<TxTransferRaw> for TxTransfer {
    fn into_raw(self) -> TxTransferRaw {
        TxTransferRaw {
            from: self.from.into_raw(),
            to: self.to.into_raw(),
            value: None,
            rewa_value: self.rewa_value.into_raw_opt(),
            dcdt_value: self
                .dcdt_value
                .into_iter()
                .map(|dcdt_value| dcdt_value.into_raw())
                .collect(),
            gas_limit: self.gas_limit.into_raw_opt(),
            gas_price: self.gas_price.into_raw_opt(),
        }
    }
}

impl TxTransfer {
    /// Converts to a TxCall, with empty endpoint and arguments.
    pub fn to_tx_call(&self) -> TxCall {
        TxCall {
            from: self.from.clone(),
            to: self.to.clone(),
            rewa_value: self.rewa_value.clone(),
            dcdt_value: self.dcdt_value.clone(),
            function: String::new(),
            arguments: Vec::new(),
            gas_limit: self.gas_limit.clone(),
            gas_price: self.gas_price.clone(),
        }
    }
}
