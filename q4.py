'''We have 25, ’25’and 25.0 and we need to give resultant as 75 in string type.'''
result= 25+ int('25')+ int('25')
#now converting result into string type.
result=str(result)
print(result)
print(type(result))