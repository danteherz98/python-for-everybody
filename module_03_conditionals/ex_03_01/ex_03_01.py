#Get input from user and convert to floating points
shrs = input("Enter Hours: ")
srt  = input("Enter Rate: ")
fhrs = float(shrs)
frt  =  float(srt)
#Print (shrs, srt)
if fhrs > 40 :
    print("Overtime")
    reg = fhrs * frt
    otp = (fhrs - 40.0) * (frt * 0.5)
    #print(reg,otp)
    xp = reg + otp
else:
    print("Regular")
    xp = fhrs * frt

print("Pay:",xp)
