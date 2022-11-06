n = int(input())
p = int(input())
d = int(input())
input_arr = []
for i in range(0,n):
    arr = int(input())
    input_arr.append(arr)
print(input_arr)
num = input_arr.index(input_arr[p])
new_arr = []
if d == 0:
    new_arr = input_arr[num:]+input_arr[0:num]
    print(new_arr)
elif d == 1:
    new_arr = input_arr[0:num] + input_arr[num:]
    print(new_arr)
    
    
    