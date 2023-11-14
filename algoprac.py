#Exercise #1
#Reverse the list below in-place using an in-place algorithm.
#For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']

def swap_string(words):
    words[0], words[-1] = words[-1], words[0]

print(f'{words = } before')
sorted_list = swap_string(words)
print(f'{words = } after/n{sorted_list = }')



#I tried to reverse the strings w/in the same function but kept getting an error that 'list has no attribute split'

# words = ['this' , 'is', 'a', 'sentence', '.']

# def swap_reverse_string(words):
#     word =  words.split()
#     for w in word:
#         return words[::-1]
#     words[0], words[-1] = words[-1], words[0]
    

# print(f'{words = } before')
# sorted_list = swap_reverse_string(words)
# print(f'{words = } after/n{sorted_list = }')




# Exercise #2
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...


a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'


def word_count(a_text):
    dict_count = {}
    text = a_text.split()
    for t in text:
        if t in dict_count:
            dict_count[t] += 1
        else:
            dict_count[t] = 1
    return dict_count

print(word_count(a_text))



# Exercise #3
# Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

# Hint: Linear Searching will require searching a list for a given number.
        


list_num = [2,5,6,4,42,7,5,74,32,3,1,18,28]

#O(N)
def linear_search(list,target):
    for i in range(len(list)):              #O(N)
        if list[i] == target:               #O(1)
            return i                        #O(1)
    else:
        if list[i] != target:               #O(1)
            print(f'{target_num} not found.')

target_num = 7

print(f' {target_num} found at index {linear_search(list_num, target_num)}')



