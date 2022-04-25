"""let 'seconds' be the total seconds the user has to enter as an input. 'minutes' is the  integral number of minutes in
 those 'seconds' and rem_secs is the remaining number of seconds.(after minutes)"""

seconds= int(input("number of seconds:- "))
minutes= seconds//60
rem_secs= seconds%60
resultant= minutes ,"minutes and", rem_secs, "seconds"
print(resultant)
