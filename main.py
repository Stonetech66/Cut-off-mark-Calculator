a1, b2, b3, c4, c5, c6= 4.0, 3.6, 3.2, 2.8, 2.4, 2.0
add, a, f, c, d, e= 0, 0, 0, 0, 0, 0
print("Waec Scores : A1, B2, B3, C4, C5, C6, D7, D8")

"""
For Waec Calculation 
Note: Waec subjects are 5
Grades= A1, B2, B3, C4, C5, C6, D7, D8
"""


for i in range(5):
 waec= input("enter your waec scores: ")
 if waec == "A1":
   a += 1
   A1= 4.0
   
 elif waec == "B2":
   b += 1
   B2= 3.6   
   
 elif waec == "B3":
   c += 1
   B3= 3.2
   
 elif waec == "C4":
   d += 1
   
 elif waec == "C5":
   e +=1
   C5= 3.6
   
 elif waec == "C6":
   f += 1
   C6= 3.6
   
 elif waec == "D7" or "E8":
  print("this Score is not allowed")
  break
  
 elif waec== "F9":
  print("sorry Universities dont accept this grade ",waec)
  break
   
agg_w=a*a1+b*b2+c*b3+d*c4+e*c5+f*c6

for i in range (3):
 jamb = int(input("enter your jamb score: "))
 if jamb < 400:
     break
 elif jamb >=400:
    print("invalid Score")

#calculation for Unilag
University= input("enter Your University")
if University == "Unilag"
 for i in range(3):
  post_utme= float(input("enter your post utme score: "))
  if post_utme< 30:
      break
  elif post_utme> 30:
     print("ivalid input")
 print("\n\n waec score: ",agg_w)
 print("jamb score: ",jamb)
 print("post utme score: ",post_utme)
 agg=agg_w+jamb/8+post_utme
 print("\n\n   Your aggregate is: ",agg)

 
 #Calculation For University of Ibadan
elif University == "U.I":
 for i in range(3):
  post_utme= float(input("enter your post utme score: "))
  if post_utme< 100:
      break
  elif post_utme>= 100:
     print("ivalid input")
 print("\n\n waec score: ",agg_w)
 print("jamb score: ",jamb)
 print("post utme score: ",post_utme)
 agg=agg_w+jamb/8+post_utme
 print("\n\n   Your aggregate is: ",agg)

#Calculation for UniIlorin
  
  
   

if agg < 30:
  print ("Sorry most schools dont accept aggregate lower than 30")
