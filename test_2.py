def count_substring(string,sub_string):
    l=len(sub_string)
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string ):      
            count+=1
    return count  

print(count_substring("palindrom", "ind"))
print(count_substring("ababab", "aba"))
print(count_substring("abakadabra", "ab"))
print(count_substring("aaaaaa", "aa"))
print(count_substring("hello", " "))
print(count_substring("hell", "hello"))