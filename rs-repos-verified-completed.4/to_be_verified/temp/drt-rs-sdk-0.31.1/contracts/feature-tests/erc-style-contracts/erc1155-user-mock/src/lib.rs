#![no_std]

numbat_wasm::imports!();

#[numbat_wasm::contract]
pub trait Erc1155UserMock {
    #[init]
    fn init(&self) {}

    #[endpoint(onERC1155Received)]
    fn on_erc1155_received(
        &self,
        _operator: ManagedAddress,
        _from: ManagedAddress,
        _type_id: BigUint,
        _value: BigUint,
        _data: ManagedBuffer,
    ) {
    }

    #[endpoint(onERC1155BatchReceived)]
    fn on_erc1155_batch_received(
        &self,
        _operator: ManagedAddress,
        _from: ManagedAddress,
        _type_ids: Vec<BigUint>,
        _values: Vec<BigUint>,
        _data: ManagedBuffer,
    ) {
    }
}
