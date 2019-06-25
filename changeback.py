def change(cost,tender):
    
    #define amount of cash given back
    cash_back = tender - cost
    
    # assign cash back to a separate variable for later use
    change = cash_back
    
    #dictionary with bill name: count,value
    money = {'Twenties':[0,20],'Tens':[0,10],'Fives':[0,5],'Ones':[0,1],'Quarters':[0,0.25],'Dimes':[0,0.10],'Nickels':[0,0.05],'Pennies':[0,0.01]}
    
    #iterate over money dict to find bills and coins needed
    for item in money:
        if cash_back//money[item][1] >= 1:
            money[item][0] += (cash_back//money[item][1])
            cash_back -= money[item][1]*(cash_back//money[item][1])
            
    #return change and bills/coins
    print(f'Your change is: ${round(change,2)}')
    for item in money:
        if money[item][0] > 0:
            print(f'{item}: {int(money[item][0])}')
            

            
print('Welcome to Change Back!')

ask = True

while ask:
    
    try:
        cost = float(input("Enter the total cost: $"))
    except:
        print('Please enter a valid number!!')
        continue
        
    try:
        tender = float(input("Enter the amount tendered: $"))
        change(cost,tender)
        ask = False
    except:
        print('Please enter a valid number!')
        continue
    
    try_again = input("Would you like to try again? Y/N: ")
    
    if try_again[0].upper() == 'Y':
        ask = True
    else:
        break
        