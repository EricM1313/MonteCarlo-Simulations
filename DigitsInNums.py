
def x2(number):
    # Convert the number to a string to work with individual digits
    
    num_str = str(number)
    if len(num_str) < 5:
        n = 5-len(num_str)
        num_str = n*'0' + num_str
    
    char_count = {}
    
    for char in num_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    num = 0
    for i in char_count.values():
        if i>2:
            return False
        if i ==2:
            num += 1
    

    return num == 1


count = 0

for i in range(100000):
    if (x2(i)):
        count += 1

print(count)

   
   
  