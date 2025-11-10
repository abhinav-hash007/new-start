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
