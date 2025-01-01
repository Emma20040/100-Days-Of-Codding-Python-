
# reading
# file = open("./Day 24/file.txt")
# content = file.read()
# print(content)
# file.close()

# another method of opening and clossing files
# with open("./Day 24/file.txt") as file:
#     content = file.read()
#     print(content)

# writting
with open("./Day 24/file.txt", mode='w') as file:
    file.write("i just replace the content found in this file")

