#!/usr/bin/python3.10.2

import random
min = 1
max = 100
target = random.randint(min, max)
print('====猜數字遊戲====')
count = 0

while True:
    guess = int(input(f'輸入數字({min}~{max}):'))
    count+=1
    if guess == target:
        print(f'賓果, 數字是{target},猜了{count}次')
        break
    elif guess < target:
        print('錯了,大一點')
        min = guess + 1
    elif guess > target:
        print('錯了,小一點')
        max = guess - 1    
    print(f'猜了{count}次')    
print(f'遊戲結束')















# #!/usr/bin/python3.10.2

# import random

# min = 1
# max = 10
# count = 0
# target = random.randint(min, max)
# print("=============猜數字遊戲================\n\n")

# while True:
#     keyin = int(input(f"猜數字範圍{min}~{max}:"))
#     count += 1
#     if(keyin == target):
#         print(f"賓果!猜對了,答案是:{target}")
#         print(f"您共猜了幾{count}次")
#         break
#     else:
#         print("猜錯了")
#         print(f"您已經猜了{count}次")
# print("遊戲結束")