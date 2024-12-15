import re

def find_min_number_in_string (string_have_number):
    list_str_has_number = re.findall(r'\d+', string_have_number)
    list_num = []
    
    for tmp in list_str_has_number:
        list_num.append(int(tmp))
    return max(list_num)

n = int(input())

for _ in range(n): 
    s = str(input())
    min_num = find_min_number_in_string(s.strip())

    print(min_num)
