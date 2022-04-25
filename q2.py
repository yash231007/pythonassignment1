"""let gri represent gross income and D represent the number of dependents and let st represent the standard deduction.
...also let... deduc represent the amount deducted per dependent, ti represent taxable income;
t represent tax rate;
"tax" represent total tax to be paid.
...given info:-Taxable income = GrossIncome - Standard deduction - (Dependent deduction
* No. of dependents)
Tax = Taxable Income * Tax Rate"""

gri= float(input("enter the gross income "))
d= float(input("number of dependents:- "))
st= 10000
deduc= 3000
ti= gri-st-(deduc*d)
t= 20/100
tax= ti*t
print("Total income tax:- ", tax)