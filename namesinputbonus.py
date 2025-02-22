import sys

students = sys.argv[1:]  
print("Student list:")
for i, student in enumerate(students, start=1):
    print(f"{i}. {student}")

