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

# set files
accounts = "accounts.csv"
blacklist = "blacklist.csv"
droped = "droped.csv"

def write(content,file):
    file_name = file
    f = open(file_name,'a')
    write = csv.writer(f)
    write.writerow(content)
    f.close()

def send(accout):
    os.system("cleos -u http://mainnet.eoscalgary.io --wallet-url=http://127.0.0.1:8900 push action " + token + " transfer '[ " + sender + " , \"" + accout + "\" , " + asset + " , " + memo + " ]' -p " + sender)

def logPrint(msg):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"+" "+msg))


if __name__ == '__main__':
    logPrint("start airdrop...")
    os.system("cleos  -u http://mainnet.eoscalgary.io --wallet-url=http://127.0.0.1:8900 wallet unlock -n " + walletName + " --password " + walletPass)
    
    f = open(accounts)
    b = open(blacklist)

    accRows = csv.reader(f)
    blkRows = csv.reader(b)

    for row in accRows:
        new = True
        num += 1

        # if you need random amout
        # rand = random.randint(0,100)+100
        # asset = '\"' + str(rand) + '.0000 HIG\"'

        to = row[0]

        for blk in blkRows:
            if blk[0] == to:
                new = False 
                break
        
        if new:
            write(row, droped)
            send(to)
            logPrint(to + ' # ' + str(num))
        else:
            logPrint(to + ' # ' + str(num) + '***IN BLACKLIST***')

        time.sleep(interval)
    logPrint("airdrop done...")
