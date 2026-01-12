from algopy import ARC4Contract, Account, String, UInt64, Global, Txn, arc4, gtxn, itxn
from algopy.arc4 import abimethod


class LotteryContract(ARC4Contract):
    entry_fee : UInt64
    total_entries: UInt64
    creator: Account
    
    # method to initiate the contract
    @abimethod(create="require")
    def create_application (self, entry_fee: UInt64)-> None:
        self.entry_fee = entry_fee
        self.total_entries = UInt64(0)
        self.creator = Global.creator_address # Store the address of the perspn who has initiate the method
    
    @abimethod 
    def enter_lottery (self, payment_txn: gtxn.PaymentTransaction) -> None:
        # check if the payment is sent to the contract address
        assert payment_txn.receiver == Global.current_application_address
        # check if the payment ammount equals the entry fee
        assert payment_txn.amount == self.entry_fee
        
        # if all the above checkpoints pass permit the participant to enter
        self.total_entries+= UInt64(1)
        
    @abimethod
    def pick_winner (self) -> None:
        # check if the caller is the owner of the contract
        assert Txn.sender == self.creator
        assert self.total_entries > UInt64(0)
        
        round_num = Global.round
        rand_num = round_num % self.total_entries
        
        winner = gtxn.Transaction(rand_num).sender
        
        itxn.Payment (
            receiver= winner,
            amount= Global.current_application_address.balance - UInt64(1_000_000), # total - 1 algo
            fee=1000
        ).submit()
        
    @abimethod(allow_actions=["DeleteApplication"])
    def del_contract(self) -> None:
        # check if the caller is the owner
        assert Txn.sender == self.creator
        
        # send all the balance remains in the contract to the owner
        itxn.Payment(
            receiver= self.creator,
            close_remainder_to=self.creator,
            fee = 1000
        ).submit()