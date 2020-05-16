import math

print("Greetings! This is co-ordinate converter")
print("Choose Your Option:")
print("1.Polar to Cartesian")
print("2.Cartesian to Polar")
n = int(input())

def PtoC():                                     #Polar to Cartesian
    a=float(input('Enter radius:'))
    b=float(input('Enter theta in degrees:'))
    b=b*(math.pi)/180.0                         #Angle- Degrees to radian

    x=a*math.cos(b)                             #Calculating X coordiante
    y=a*math.sin(b)                             #Calculating Y coordiante

    x=round(x,2)                                #Rounding off to 2 deciamls
    y=round(y,2)

    print "Cartesian co-ordinate is","x:", x,", y:",y

def CtoP():                                     #Cartesian to Polar
    x=float(input('Enter X coordinate:'))
    y=float(input('Enter Y coordinate:'))

    M=math.sqrt(x**2 + y**2)                    #Calculating Radius
    N=math.atan(y/x)                            #Calculating Angle
    N=N*180/(math.pi)                           #Angle- radian to degrees

    A=round(M,2)                                #Rounding off to 2 decimals
    B=round(N,2)

    print "Polar co-ordinate is","Radius:", A, ", Theta(in degrees)", B

if(n==1):
    PtoC()
elif(n==2):
    CtoP()
else:
    print("Invalid input! \nPlease select again.")  #For invalid input
