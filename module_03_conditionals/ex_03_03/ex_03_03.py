#Aks user to input score value
score = input("Enter score: ")

#Error message for out of range or non numeric
try:
    fscore = float(score)
except:
    print("Please enter a valid score")
    quit()

#Return value to user
if fscore > 1.0 or fscore < 0.0:
    print("Please enter a valid score")
elif fscore >= 0.9 : 
    print("A")
elif fscore >= 0.8 :
    print("B")
elif fscore >= 0.7 :
    print("C")
elif fscore >= 0.6 : 
    print("D")
elif fscore < 0.6 :
    print("F")