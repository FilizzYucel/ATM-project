#Bankamatik uygulaması

FilizAccount = {
    'name': 'Filiz Yücel',
    'accountNo': '123456543',
    'balance': 3000,
    'addAccount': 2000
}

MusaAccount = {
    'name': 'Musa Karasoy ',
    'accountNo': '23454321',
    'balance': 4000,
    'addAccount': 1000
}

#para çekme
def withdrawMoney(account, amount):
    print(f"Hello {account['name']}")
    if (account['balance']>= amount):
        account['balance']-= amount
        print('You can take your money.')
        balanceInquiry(account)
    else:
        sum = account['balance']+ account['addAccount']

        if sum >= amount :
            addAccountUse = input('Use additional account ? (t,/f)\n')

            if addAccountUse =='t':
                addAccountUseAmount = amount-account['balance']
                account['balance']=0
                account['addAccount']= account['addAccount'] - addAccountUseAmount


                print('you can take your money')
                balanceInquiry(account)

            else:
                print(f"number {account['accountNo']} account have {account['balance']}  ")
        else:
            print('sorry amount not enough.')

#bakiye sorgulama
def balanceInquiry(account):
    print(f"{account['accountNo']} no have {account['balance']} TL and your additional account have {account['addAccount']} TL.")

#para yatırma 
def deposit(account,money):
    addMoney=input('Which account(main or additional) can you use for put money ? m/n ')
    if addMoney=='m':
        account['balance'] = account['balance'] + money

    else:
        account['addAccount'] += money


withdrawMoney(FilizAccount, 3000)

print('***********')

deposit(FilizAccount,1000)
balanceInquiry(FilizAccount)




