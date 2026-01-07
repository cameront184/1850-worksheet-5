def classify(avg):
    if avg >= 70:
        return "1"
    elif avg >= 60:
        return "2:1"
    elif avg >= 50:
        return "2:2"
    elif avg >= 40:
        return "3"
    else:
        return "F"


in_filename = input()
out_filename = in_filename + "_out.csv"

with open(in_filename, "r") as infile, open(out_filename, "w") as outfile:

    outfile.write("student_id,average_grade,classification\n")

    next(infile)

    for line in infile:                       # removing the whitespace and then making the text a list of strings
        line = line.strip()
        if line == "":
            continue

        parts = line.split(",")

        student_id = parts[0]                 # So we don't incorporate the student id into the average
        student_grades = parts[1:]

        grades = []
        for g in student_grades:              # turning the list of strings into a list of integers
            g = g.strip()
            if g != "":
                grades.append(int(g))

        avg = sum(grades) / len(grades)

        outfile.write(f"{student_id},{avg:.2f},{classify(avg)}\n")
