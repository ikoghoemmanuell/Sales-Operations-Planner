#create a list for salesQty, StockLvl & ProductionQty
salesQty=[]
stockLvl=[]
productionQty=[]

#Ask the user for initial stock level
stockLvl.append(float(input('Please enter an initial stock level: ')))

#Ask the user for number of months
months=int(input('Please enter the number of months to plan '))

for i in range(0,months):
#Ask the user for the planned sales qty for each month
    salesQty.append(float(input(f'Please enter the planned sales quantity for month {i+1}: ')))

#Write logic to calculate production qty & stocklevel for each month
    if salesQty[i]<stockLvl[i]:
        productionQty.append(0)
        stockLvl.append(stockLvl[i]-salesQty[i])
    else:
        productionQty.append(int(salesQty[i]-stockLvl[i]))
        stockLvl.append(0)

#Displey the resulting production quantities
print()
print('The resulting production quantities are:\n')
for i in range(0,months):
    print(f'Production Quantity Month {i+1} - {productionQty[i]}')



