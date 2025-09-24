# list 
# ordererd List of data types with sequential values 
# mutable, values can alter 

# Example 1 
# Define List 

import gc 

sampleList = [1,2,4]
print(sampleList)
# Print list of values of the sample list 

sampleList.append(100)
print(sampleList)
# Append(value) added the values at the last using append 

sampleList.insert(2, 101)
print("add the values using index and values moves the values", sampleList)
# insert(index, value) add the values using index and values moves the values 

sampleList.pop()
print("removing the last element",sampleList)
# pop() remove the last element 

sampleList.pop(3)
print("removing the element based on index", sampleList)
# pop(index) remove the index element


sampleList.extend([4,9,10])
print("extending the multiple array values to existing", sampleList)
# extend() will add the multiple values to existing array

sampleList.sort()
print(sampleList)
# sort() the array of values using ascending order"

sampleList.sort(reverse=True)
print(sampleList)

sampleList.reverse()
print(sampleList)

sampleList.clear() 
print(sampleList)

del sampleList

gc.collect()

