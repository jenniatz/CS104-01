temp = 0


temp = int(input("please enter the current temeperature:"))
if temp > 90:
    print ("wear shorts")
elif temp > 70:
    print ("short sleeves are fine")
elif temp > 50:
    print ("wear a jacket")
elif temp > 32:
    print ("wear a heavy coat")
elif temp < 32:
    print ("stay inside")
# make program repeat until temp reaches 999
