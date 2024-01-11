"""
Import math for power function
Ask user to choose which calculation they would like
Produce an if statement for their decision, convert their input so that
it is stored the same no matter how it is typed in

If investment, ask for the amount of deposit, the interest rate (as a number),
number of years of investing and type of interest
Convert the inputs as a integer, float and integer respectively
If 'simple', calculate for simple interest (A = P *(1 + r*t))
If 'compound', calculate for compound interest (A = P * math.pow((1+r),t))
Print the calculation

If bond, ask for the present value of the house, interest rate and
number of months to repay
Store inputs as integer, float and integer respectively
For repayment, use (i * P)/(1 - (1 + i)**(-n))
Calculate the amount to repay each month and print the answer
"""

import math

"""'.capitalize' used to convert text to capitalise the first letter so the
program can read the word, regardless of case sensitivity"""
print('''investment - to calculate the amount of interest you'll earn \
on your investment''')
print("bond - to calculate the amount you'll have to pay on a home loan")
calculation_type = input('''Enter either 'investment' or 'bond' from the \
menu above to proceed: ''').capitalize()

if calculation_type == 'Investment':
    print("You have chosen Investment")
    
    deposit = int(input("How much are you depositing? £"))
    interest_rate = float(input("At what interest rate? "))
    years = int(input("For how many years? "))
    interest_rate_div = interest_rate / 100
    
    interest = input('''Please choose either 'simple' or 'compound' \
interest: ''').capitalize()
    
    if interest == 'Simple':
        simple = deposit *(1 + interest_rate_div*years)
        print(f'''With 'Simple' interest, the total amount you will get back \
after {years} years at {interest_rate}% interest rate is \
£{round(simple, 2)}. ''')

    #Round function used to print the number to 2 decimal places
    elif interest == 'Compound':
        compound = deposit * math.pow((1+interest_rate_div),years)
        print(f'''With 'Compound' interest, the total amount you will get \
back after {years} years at {interest_rate}% interest rate \
is £{round(compound, 2)}. ''')
    else:
        print("Please choose an option.")

elif calculation_type == 'Bond':
    print("You have chosen Bond")
    
    value = int(input("What is the present value of the house? £"))
    interest_rate = float(input("At what interest rate? "))
    months = int(input("How many months do you plan on taking to repay? "))
    monthly_interest_rate = (interest_rate / 100) / 12
    repayment = (monthly_interest_rate * value)/(1
                                - (1 + monthly_interest_rate)**(-months))
    
    print(f'''With a house value of {value}, an interest rate of \
{interest_rate}% and for {months} months, your monthly repayment is \
£{round(repayment, 2)}.''')

else:
    print("Please choose an option")