import string


#man = "Sam"
#woman = "Bomi"
#man_woman = man + " " + woman


#swapped_names = " ".join([man_woman.split()[0][0] + man_woman.split()[1]])

#print(man_woman.split()[1])

#print(swapped_names)


string = input("Enter a string: ")

new_string = ""

first_letter = string[0]
middle_letter = string[len(string) // 2]
last_letter = string[len(string) - 1]

new_string = "---".join(first_letter + middle_letter + last_letter)

print(new_string)

