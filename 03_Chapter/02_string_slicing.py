# string slicing is accessing strings via indexes in ranges (range can be either +ve or -ve)
sample_text = "ENCYCLOPEDIA"

# SLICING IN PYTHON
print(len(sample_text)) #12
print(sample_text[0:12]) # the 12 is exclusive so it would iterate till 11 which is till our last character `A`

# [start:stop:step]
# for reversing a string we can use
print(sample_text[::-1])

print(sample_text[0:]) # ENCYCLOPEDIA
print(sample_text[0:11:2]) # String Slicing with Skip Value