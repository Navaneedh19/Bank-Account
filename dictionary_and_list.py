#Dictionary in Python
student_marks = {
   "Navanee" : 80,
   "Makizh" : 89,
   "Karthi" : 67,
   "Lokesh" : 79,
   "Kishore" : 60
}

print(student_marks["Navanee"])

# Dictionary is a collection of key-value pairs
# We can add, update, or delete key-value pairs
# Dictionaries are efficient for retrieving values based on keys

# List of tuples in Python

employee_salaries = [('Deena', "Software Engineer", 50000), ('Abishek', "Civil Engineer", 60000), ('Vinoth', "Mechanical Engineer", 55000)]
for name, proffession, salary, in employee_salaries:
 print(f"{name}'s  salary is {salary} - {proffession}")

# Lists are mutable
# We can modify the elements of the list including the tuples.
# It maintain the order of insertion, or when keys may be duplicated.
 

#  Use Cases:
 
#  Dictionary: 
#  Use when you have unique identifiers(keys) and need fast lookups based on those keys. 
#  For example, storing user information where each user has a unique username, by calling the unique key, we can fastly retrieve the data. 
 
#  List of Tuples: 
#  Use when you need to maintain insertion order or if you have duplicate keys. 
#  For example, recording the chronological order of events or storing data that may have repeated occurrences.