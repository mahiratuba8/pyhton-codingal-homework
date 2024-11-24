


def fibi(x):
   if x<=0:
    return []
   elif x==1:
     return[0]
   elif x==2:
     return[0,1]
   else:
     seq=fibi(x-1)
     seq.append(seq[-1] + seq[-2])
     return seq
   
number=int(input("Enter number: "))
if number<0:
  print("please enter a non-negative number")
else:
    print("Fibinaci sequence from ", number, "will be", fibi(number))   
   
 