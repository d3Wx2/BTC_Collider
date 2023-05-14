from steemhd.pyhd import hd_wallet_CreateFromMnemonic,hd_wallet_CreateFromprivatekey,steem_wallet_CreateFromMnemonic,btc_pub_to_addr
from mnemonic import Mnemonic
import os

BTC_DERIVATION_PATH = "m/44'/0'/0'/0"

x=0
adr_n=0

with open("adr.txt") as file:
    array = [row.strip() for row in file]

def mnem():
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=256)
    return words

while True:
    mnemonics = mnem()
    #print(mnemonics)

    while x<20:
        #BTC_Legacy
        addr_num=x
        coins="BTC"
        PATH=BTC_DERIVATION_PATH
        wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
        btc_addr=wallet.get("address")
        #print("Адрес № " + str(adr_n) + " " + btc_addr)
        adr_n+=1
        x+=1
        addr_num = addr_num + 1
        if btc_addr in array:
            x=0
            with open("found.txt", "a") as file:
              file.write(str(wallet) + "\n")
            print(wallet)
            break
    if x==20:
        x=0
        continue
