#LIST DATA TYPE

Values = [1, 2, "mahesh", 4, 5]
#List is data type that allows multiple values and that can different data types

print(Values[0])

print(Values[1])
print(Values[-1])
print(Values[1:3])

Values.insert(3, "Badakal")
print(Values)

Values.append("end")
print(Values)


Values[2] = "MAHESH"  #Updating
print(Values)

del Values[0]   #deleting
print(Values)



#TUPLE Data Type - Same as LIST Data Type but immutable

Val = (1, 2, "praveen", 4, 5)
print(Val)

print(Val[1])
#Val[2] = "Mahesh"
#print(Val)



#Dictionary Data type - works on key value pair
Val = {1:"a", "b":2, "c":"Hello world", 3:4}
print(Val)

print(Val[1])
print(Val["b"])
print(Val["c"])
print(Val[3])


#
Dict = {}
print(Dict)

Dict["First name"] = "Mahesh"
Dict["Last name"] = "Badakal"
Dict["Gender"] = "Male"
print(Dict)
print(Dict["First name"])