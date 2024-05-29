# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#def main():
A = [1, 3, 6, 4, 1, 7, 100, -3, -4, 0, 2, 5]
'''
positive_set = set(x for x in A if x > 0)
   
# Start checking from 1 upwards to find the smallest missing positive integer
smallest_missing_positive = 1
while smallest_missing_positive in positive_set:
    smallest_missing_positive += 1
    
print (smallest_missing_positive)
'''
########
sorted_list = sorted(A) 
lower_possible = 1

for i in range (len(sorted_list)):
    if (sorted_list[i] > 0) & (sorted_list[i]==lower_possible):
        lower_possible +=1

########
pass
