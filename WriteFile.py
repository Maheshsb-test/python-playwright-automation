#read the file and store all the lines in list
#reverse the list
#write the list back to the file

with open('test1.txt', 'r') as file:  #as reader
    content = file.readlines()
    reversed(content)

    with open('test1.txt', 'w') as file:   #as writer
        for line in reversed(content):
            file.write(line)

