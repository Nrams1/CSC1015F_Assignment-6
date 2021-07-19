# vectormath
import math

def vector_math():
      x=(input("Enter vector A:\n"))
      y=(input("Enter vector B:\n"))
      xlist=x.split()
      ylist=y.split()
      add =[eval(xlist[0])+eval(ylist[0]),eval(xlist[1])+eval(ylist[1]),eval(xlist[2])+eval(ylist[2])]
      print("A+B =",add)
      mul =eval(xlist[0])*eval(ylist[0])+ eval(xlist[1])*eval(ylist[1])+eval(xlist[2])*eval(ylist[2])
      print("A.B =",mul)
      normA =math.sqrt(eval(xlist[0])**2+eval(xlist[1])**2+eval(xlist[2])**2)
      normA="{0:.2f}".format(normA)
      print("|A| =",normA)
      normB=math.sqrt(eval(ylist[0])**2+eval(ylist[1])**2+eval(ylist[2])**2)
      normB="{0:.2f}".format(normB)
      print("|B| =",normB)
      
      
      
      
      
    
vector_math()