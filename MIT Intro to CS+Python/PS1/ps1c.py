#down payment monthly savings rate estimate w bisection search
annual_salary = float(input("Enter your annual salary: "))

down_payment=.25*1000000
monthly_salary = (annual_salary)/12.0
#print("annual salary =",annual_salary)

#print("monthly savings =",monthly_savings)
total_savings = 0.00
roi = 0.04/12 #monthly return on investment
num_months = 0
salary_increase=1+0.07

#low and high will be the lower and upper guesses for the savings rate respectively, and actual_rate will be used to
#incrementally get closer to the best savings rate
low_rate = 0.0
high_rate = 1.0
actual_rate = 0

num_guesses = 0 #number of guesses/steps in bisection search process

epsilon = 100 #epsilon is the delta between the total savings and down payment - it is set to within 100 based on instructions

possible=True #determines whether user even has enough money (assuming he/she saves everything)

while ((abs(total_savings-down_payment) >= epsilon or total_savings < down_payment) and possible):
    total_savings=0
    monthly_salary = (annual_salary) / 12.0

    #the first iteration in this loop is purely to see if the user has enough money. Thus, we assume he saves all their
    #money initially and check if he will be able to pay off their down payment - if yes, the loop continues, if no,
    #the value of possible is set to false and the loop terminates
    if num_guesses == 0:
        actual_rate = 1
    else:
        actual_rate = (low_rate + high_rate) / 2

    for month in range(1,37):
        investment_gains = roi*total_savings
        total_savings+=monthly_salary*actual_rate+investment_gains
        if month%6==0:
            monthly_salary*=1.07

    if num_guesses==0 and total_savings<down_payment:
        possible=False
    else:
        if total_savings>down_payment:
            high_rate = actual_rate
        else:
            low_rate = actual_rate
    num_guesses += 1

if possible:
    print(f"total savings is {total_savings} and down payment is {down_payment}")
    print(f"Best savings rate: {actual_rate}")
    print(f"Steps in bisection search: {num_guesses-1}")
else:
    print("Sorry, it is not possible to pay off the down payment within 3 years.")