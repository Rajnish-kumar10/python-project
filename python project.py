no_of_student=int(input("number of student="))
names=[]
marks=[]
updates=[]
for i in range (0,no_of_student):
    a=input("names:")
    marks_of_student=int(input(" marks of student: "))
    updated_marks_of_student=int(input("updated marks of student:"))
    names.append(a)
    marks.append(marks_of_student)
    updates.append(updated_marks_of_student)
print(names,marks,updates, sep='\n')

#  first after updation in rank
def nameRank(names, marks, updates, n):
    # Array of students
    x = [[0 for j in range(3)] for i in range(n)]
    for i in range(n):
        # Store the name of the student
        x[i][0] = names[i]

        # Update the marks of the student
        x[i][1] = marks[i] + updates[i]

        # Store the current rank of the student
        x[i][2] = i + 1

    highest = x[0]
    for j in range(1, n):
        if (x[j][1] >= highest[1]):
            highest = x[j]

    # Print the name and jump in rank
    print("Name: ", highest[0], ", Jump: ",abs(highest[2] - 1), sep="")




AFTER RUNNING


number of student=3                # take number of student as much we want example= 3
names:NISHANT                      # then enter frist name ; example = nishant
 marks of student: 50              #then enter marks of first student example= 50
updated marks of student:-2	   #enter update marks of student; example=-2

names:RAJNISH                      #now enter second name; example= rajnish
 marks of student: 45              #then enter marks of first student example= 45
updated marks of student:+2        #enter update marks of student; example=+2

names:SANCHIT                      #now enter second name; example= sanchit
 marks of student: 40              #then enter marks of first student example= 40
updated marks of student:-5        #enter update marks of student; example=-5

['NISHANT', 'RAJNISH', 'SANCHIT']  # HERE OUR RESULT
[50, 45, 40]
[-2, 2, -5]
Name: NISHANT, Jump: 0

Process finished with exit code 0






