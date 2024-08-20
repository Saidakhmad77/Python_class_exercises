#first_name = "Here is"
#middle_name = "My"
#last_name = "Fullname"

#full_name = (print("Your full name is: " , first_name , middle_name , last_name, sep=" ", end="!"))



##### Only first name printed  #####

#full_name = (first_name)

#print("Your first name is: " + full_name, end="!")



##### Only last name prited   #####

#full_name = (last_name)

#print("Your last name is: " + last_name, end="^^")



#####  Only middle name printed  #####

#full_name = (middle_name)

#print("Your middle name is: " + middle_name, end="$")



#####  Allowing user to input their own names  #####

firstname = input("Please enter your first name: ")
middlename = input("Please enter your middle name: ")
lastname = input("Please enter your last name: ")
full_name =(firstname + middlename + lastname)

#print(f"First name: {firstname}")
#print(f"Middle name: {middlename}")
#print(f"Last name: {lastname}")
#print(f"Your full name is: {firstname} {middlename} {lastname}")

#full_name = (f"{firstname} {middlename} {lastname}")

#print("Your full name is: ", full_name, sep=" ", end="!")

#### Only first name ####
first_lenght = len(firstname)
print(full_name[0:first_lenght])

##### Only middle name ####
middle_index = first_lenght + 2
middle_name_length = len(middlename)
middle_end_index = middle_name_length + first_lenght + 1
print(full_name[middle_index:middle_end_index])

##### Only last name  #####

length_of_string = len(full_name)
print(full_name[middle_index:length_of_string]) 