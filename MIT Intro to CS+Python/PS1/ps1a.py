#down payment month estimate
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

down_payment=0.25*total_cost
monthly_salary = (annual_salary)/12.0
#print("annual salary =",annual_salary)

monthly_savings = monthly_salary*portion_saved
#print("monthly savings =",monthly_savings)
savings = 0
roi = 0.04/12
num_months = 0

while savings<down_payment:
    investment_gains = roi * savings
    savings+=monthly_savings+investment_gains
    num_months+=1

print(f"Number of months: {num_months}")