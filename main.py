#Temperature converter Problem
C = 30

#Subroutine to convert Centigrade to fareheit 
def CtoF(C):
  return (C * 1.8) + 32

#Subroutine to convert Farenheit to centigrade 
def FtC(F):
  return (F / 1.8) - 32

#Main Program
F = CtoF(C)
print(C,"degrees C is",F,"degrees F")