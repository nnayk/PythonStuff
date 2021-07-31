#down payment month estimate w raise
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_salary_raise = float(input("Enter the semi-annual raise, as a decimal: "))

down_payment=0.25*total_cost
monthly_salary = (annual_salary)/12.0
#print("annual salary =",annual_salary)

#print("monthly savings =",monthly_savings)
savings = 0
roi = 0.04/12
num_months = 0
salary_increase=1+semi_annual_salary_raise
monthly_savings = monthly_salary * portion_saved

while savings<down_payment:
    investment_gains = roi * savings
    savings+=monthly_savings+investment_gains
    num_months+=1
    if num_months%6==0:
        monthly_salary *=salary_increase
        monthly_savings = monthly_salary * portion_saved

print(f"Number of months: {num_months}")