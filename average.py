numberofTests = 0
score = 0
total = 0
average = 0.0
scorecount = 0

numberoftests=int(input("please enter the number of tests you want to average:"))
score = int(input("please enter score: "))
scorecount = scorecount + 1
total = total + score
average = total/scorecount
print("The average is ", average)
