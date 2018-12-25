import time,datetime,os,csv

interval = 15
token = '\"tokencontract\"'
sender = '\"yourccount\"'
asset = '\"100.0000 SYM\"'
memo = '\" Your Memo \"'
walletName = "walletName"
walletPass = "PW5JMfG---walletPass---------3BGA"


def send(accout):
    
    os.system("cleos -u http://mainnet.eoscalgary.io --wallet-url=http://127.0.0.1:8900 push action " + token + " transfer '[ " + sender + " , \"" + accout + "\" , " + asset + " , " + memo + " ]' -p " + sender)

def logPrint(msg):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"+" "+msg))


if __name__ == '__main__':
    logPrint("start airdrop...")
    os.system("cleos  -u http://mainnet.eoscalgary.io --wallet-url=http://127.0.0.1:8900 wallet unlock -n " + walletName + " --password " + walletPass)
    f = open("accounts.csv")
    # f = open("drop.csv")
    rows = csv.reader(f)
    for row in rows:
        to = row[0]
        send(to)
        logPrint(to)
        time.sleep(interval)
    logPrint("airdrop done...")
