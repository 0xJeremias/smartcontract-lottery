# Actual (10/09/22) ETH price = 1778,99
# 50 $ <=> 0.0281 ETH

from brownie import Lottery, accounts, config, network
from web3 import Web3


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )

    assert lottery.getEntranceFee() > Web3.toWei(0.026, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.030, "ether")
