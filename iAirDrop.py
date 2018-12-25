import time,datetime,os,csv

# Sleep seconds
interval = 15 

# token contract account
token = '\"yourtokens\"'

# your account
sender = '\"account\"'

# amount and symbol
asset = '\"100.0000 SYM\"'

# memo
memo = '\" blablabla \"'

# wallet name and password
walletName = "wallet"
walletPass = "PW5-------walletPass--------GA"


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
