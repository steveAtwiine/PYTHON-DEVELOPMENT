##The following program gets all the total costs and expenses you have
#Spent in a month and reduces it from the total incomes you have earned so far.

#Total incomes
housing_allowance = int(input("Housing Allowance fee: "))
transport_allowance = int(input("Transport Allowance fee: "))
insurance_allowance = int(input("Insurance Allowance fee: "))
motor_vehicle_allowance = int(input("Motor vehicle Allowance: "))
salary = int(input("Your salary from work: "))

print("\n")

#Total incomes
grand_incomes = housing_allowance + transport_allowance + insurance_allowance + motor_vehicle_allowance + salary
print("Grand Income is:", grand_incomes)

print("\n")

#Total Expenses
rent = int(input("Rent costs: "))
fuel = int(input("Fuel costs: "))
foods = int(input("Food stuffs and drinks costs: "))
electricity = int(input("Electricity bills: "))
water = int(input("Your water bills ="))

print("\n")

#Total costs
grand_costs = rent + fuel + foods + electricity + water
print("Your Total expenses are =", grand_costs)

print("\n")

#Net Income for the month
net_income = grand_incomes - grand_costs
print("Your Net incomes for the month ended is =", net_income)


input("\n\tPrint enter for the program to exit..")