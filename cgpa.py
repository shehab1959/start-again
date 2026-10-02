print("======================================")
print("       STUDENT INFORMATION SYSTEM")
print("======================================")

# Taking basic information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\n--------------------------------------")
print("Enter marks for 5 subjects")
print("--------------------------------------")

# Taking marks
c = float(input("C Programming: "))
python = float(input("Python: "))
dbms = float(input("DBMS: "))
math = float(input("Mathematics: "))
english = float(input("English: "))

# Calculate total and average
total = c + python + dbms + math + english
average = total / 5

# Determine grade
if average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "A-"
elif average >= 50:
    grade = "B"
elif average >= 40:
    grade = "C"
elif average >= 33:
    grade = "D"
else:
    grade = "F"

# Determine result
if average >= 33:
    result = "PASS"
else:
    result = "FAIL"

# Display result
print("\n======================================")
print("             STUDENT RESULT")
print("======================================")

print("Name    :", name)
print("Age     :", age)
print("City    :", city)

print("--------------------------------------")
print("C Programming :", c)
print("Python        :", python)
print("DBMS          :", dbms)
print("Mathematics   :", math)
print("English       :", english)

print("--------------------------------------")
print("Total Marks   :", total)
print("Average       :", round(average, 2))
print("Grade         :", grade)
print("Result        :", result)

print("======================================")
print("       Thank you for using the system!")
print("======================================")