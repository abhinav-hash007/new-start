# # Writing to a text file
# with open("notes.txt", "w") as file:
#     file.write("Hello Abhinav!\n")
#     file.write("You're mastering Python file I/O.\n")

# # Reading from the text file
# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)
# tasks = ["Revise regex", "Practice file I/O", "Win debate", "Optimize Arch Linux"]

# Write each task on a new line
# with open("tasks.txt", "w") as file:
#     for task in tasks:
#         file.write(task + "\n")

# # Read tasks line-by-line
# with open("tasks.txt", "r") as file:
#     for line in file:
#         print("Task:", line.strip())
# 1. re.search()
# Use: Find the first match anywhere in the string.

# ✅ Best for: Checking if a pattern exists.

# Challenge: Find the first 4-digit year in "He was born in 1998 and graduated in 2020".

# import re
# line = "He was born in 1998 and graduated in 2020"
# x = re.search(r"\d{4}", line)
# if x:
#     print(f"first yr with 4 letter in it is {x}")

#     2. re.findall()
# Use: Return all matches as a list.

# ✅ Best for: Extracting multiple items (emails, numbers, words).

# Chall"Abhinav and David went to Delhi"enge: Extract all words starting with capital letters from "Abhinav and David went to Delhi".
# import re
# line = "Abhinav and David went to Delhi"
# x = re.findall(r"[A-Z][a-z]+",line)
# if x:
#     print(f"all of the letters with capital alpha are {x}")

# import re
# num = "I have 1000 cars and 4 all of them are invisible. "
# x= re.findall(r"[0-9]+", num)
# for a in x:
#     print(a)
# 3. re.sub()
# Use: Replace all matches with something else.

# ✅ Best for: Masking, cleaning, formatting.

# Challenge: Replace all digits in "My number is 9876543210" with X.

# import re
# line =  "My number is 9876543210"
# sub = re.sub("[0-9]","X", line)
# print(sub)
import re
line = "CS50x"
check = re.search(r"^CS50x$", line)
if check:
    print("valid")
else:
    print("invalid")