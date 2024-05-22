grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
journal = {}
n = 0
while n <= len(grades) - 1:
    journal.update({students[n]: sum(grades[n])/len(grades[n])})
    n += 1
else:
    print(journal)
