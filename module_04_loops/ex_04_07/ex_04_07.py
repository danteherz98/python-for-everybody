def computegrade(score):
    try:
        fscore = float(score)
        if fscore > 1.0 or fscore < 0.0:
            return "Bad Score"
        elif fscore >= 0.9:
            return "A"
        elif fscore >= 0.8:
            return "B"
        elif fscore >= 0.7:
            return "C"
        elif fscore >= 0.6:
            return "D"
        else:
            return "F"
    except ValueError:
        return "Bad score"

score_input = input("Enter score: ")
grade = computegrade(score_input)
print(grade)
