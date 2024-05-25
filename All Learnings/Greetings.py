import time
timestamp = int(time.strftime("%H"))
#print(timestamp)
name = input("Enter your name : ")
if(timestamp < 12):
    print("Good Morning", name)
elif(timestamp >= 12 and timestamp < 16):
    print("Good Afternoon", name)
elif(timestamp >= 16 and timestamp < 20):
    print("Good Evening", name)
else:
    print("Good Night", name)