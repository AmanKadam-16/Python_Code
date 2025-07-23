# String in-built functions in Python
sample_str = "NEPTUNE"

# len() function is used to find the lenght of string
print(len(sample_str))

# str.endswith("string_sequence") This method is used to find 
# if a given string ends with argumented sequence / sub-string or not | returns Bool ~ True / False
print(sample_str.endswith('NE')) # Output : True
# if we want to check irrespective of string case either upper or lower case
print(sample_str.lower().endswith('ne')) # Output : True
# if we want to find the count of any character in required string we can use count() method
print(sample_str.count('E')) # Output : 2
# if we want to caplitalize every first character of a given string we can use capitalize() method
sample_str1 = "neptune"
print(sample_str1.capitalize()) # Output : Neptune
# if we want to find if a given string exists and at what index then find() method is useful in Python for strings
print(sample_str.find('TUNE')) # 3 // The substring TUNE starts from index 3 of the target string
# replace() this Method is used to replace the required character with targetted character in a string
print(sample_str1.replace("t", "l"))