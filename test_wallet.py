import pytest
from lambdata_keilayb.wallet import Wallet


@pytest.fixture
def empty_wallet():
    '''Returns a wallet instance with a zero balance'''
    wallet = Wallet()
    return wallet

@pytest.fixture
def wallet():
    '''Returns wallet of balance 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert (wallet.balance)*5 == 100

def test_wallet_add_cash(wallet):
    wallet.add_cash(100)
    assert wallet.balance == 120

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

