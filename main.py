a=(input("What should we call you?:"))
b=(input("How old are you?:"))
c=(input("Where do you live?:"))
import time
T=time.strftime('%H:%M:%S')
print("Your current time is:",T)
h=int(time.strftime('%H'))
if(h<12):
  print("Good Morning!",a)
elif(h>12 and h<18):
  print("Good Afternoon!")
else:
  print("Good Night!")


