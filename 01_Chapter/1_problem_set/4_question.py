# Use inbuild OS module to print the items of a directory
# Import the module
import os

directory_path = "./01_Chapter"
contents = os.listdir(directory_path) # many methods available as per req.  / use case
contents_list : list = contents
print(contents_list)
for content in contents:
    print(content)
