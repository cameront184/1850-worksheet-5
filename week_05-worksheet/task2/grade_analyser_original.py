'''
Portfolio Task - Grade Analyser

In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be achieved by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.

Note:
Your code will only be tested on valid files in the format shown in the 4 example files in this folder - you do not need to validate any data.
'''
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

    for line in infile:                       # removing the whitespace and then making the text a list of strings
        line = line.strip()
        if line == "":
            continue

        parts = line.split(",")

        student_id = parts[0]                 # So we don't incorporate the student id into the average
        student_grades = parts[1:]

        grades = []
        for g in student_grades:               # turning the list of strings into a list of integers
            g = g.strip()
            if g != "":
                grades.append(int(g))

        avg = sum(grades) / len(grades)

        outfile.write(f"{student_id},{avg:.2f},{classify(avg)}\n")







     
     



