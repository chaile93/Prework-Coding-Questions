#1
def hello_name(user_name):
    print(f"hello_{user_name}!")

hello_name("chaile")



#2
def first_odds():
    for num in range(1, 101, 2):
        print(num)

#3 
def max_num_in_list(a_list):
    if not a_list:
        return None 
    
max_num = a_list[0]
for num in a_list:
        if num > max_num:
            max_num = num    
    return max_num


nums = [3, 8, 1, 10, 5]
print(max_num_in_list(nums)) 

empty_list = []
print(max_num_in_list(empty_list)) 

#4
def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year(2020))  
print(is_leap_year(2021))  
print(is_leap_year(1900))  
print(is_leap_year(2000))  
print(is_leap_year(2024)) 


#5
def is_consecutive(a_list):
    if len(a_list) < 2:
        return False 
    
    sorted_list = sorted(a_list) 
    
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i-1] + 1:
            return False
    
    return True

print(is_consecutive([2, 3, 4, 5, 6, 7])) 
print(is_consecutive([1, 2, 4, 5]))        
print(is_consecutive([10, 11, 12, 13]))   
print(is_consecutive([5]))                
print(is_consecutive([]))                 

