file = open('test1.txt')

#read all the contents of file
#print(file.read())

#reads N number of characters from file
#print(file.read(2))

#read one single line at a time
#print(file.readline())

#print(file.readline()) #reads second line

#to print all the contents line by line it's not best approach to use multiple times readline() method
#to overcome this below example

#print line by line using readline() method

# line = file.readline()
# while line!='':
#     print(line)
#     line = file.readline()


#conent stored in text file as list like below
#list = [Man, dog, elephant, cat, zebra]
#so other way to print content from file as line by line

for line in file.readlines():
    print(line)

file.close()