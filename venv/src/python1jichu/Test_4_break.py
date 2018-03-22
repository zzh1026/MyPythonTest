# -*- coding: utf-8 -*-

# break
# 在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：

n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    # print(n)
    n = n + 1
print('END')



# continue
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

n = 0
while n >= 0:
    print(n)
