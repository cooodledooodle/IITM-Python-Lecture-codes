#Problem 2
#Find the total profit/loss of each trader working in a trading firm. Information regarding number of traders and number of transactions is unknown.

empID = input('Enter employee ID: ')
while(empID != '-1'):
    trade = int(input('Enter the trade amount: '))
    profit_loss = 0
    while(trade != 0 ):
        trade = int(input('Enter the trade amount: '))
    print(f'Profit/loss for employee {empID} is {profit_loss}')
    empID = input('Enter employee ID: ')