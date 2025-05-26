def computepay(hours, rate) :
    # print("In computepay", hours, rate)
    if hours > 40 :
        print("Overtime")
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        #print(reg,otp)
        xp = reg + otp
    else:
        print("Regular")
        pay = hours * rate
    # print("Returning", pay)
    return pay


#Get input from user and convert to floating points
shrs = input("Enter Hours: ")
srt  = input("Enter Rate: ")
fhrs = float(shrs)
frt  =  float(srt)

xp = computepay(fhrs, frt)
#Print (shrs, srt)
print("Pay:",xp)
