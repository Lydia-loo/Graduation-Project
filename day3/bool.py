# bool_1 = True
# bool_2 = False
# print(f"the content of bool_1 is: {bool_1},类型是：{type(bool_1)}")
#
# print("*********************")
# result = 5 > 8
# print(f"result is {result}, and the type is : {type(result)}")
#
# print("*********************")
# num1 = 10
# num2 = 10
# print(f"10 == 10 result:{num1 == num2}")
# print(f"10 >= 10 result:{num1 >= num2}")
# num1 = 10
# num2 = 15
# print(f"10 != 15 result:{num1 != num2}")
# print(f"10 > 15 result:{num1 > num2}")
# name1 = "iloveyou"
# name2 = "iloveit"
# print(f"name1 == name2 result:{name1 == name2}")
#
# # if
# print("*********************")
# age = int(input("your age is"))
# if age >= 18:
#     print("我已经成年")  # 缩进为四个空格
# print("时间过得真快")
# if else
# age = int(input("your age : "))
# if age >= 18:
#     print("you should buy the ticket")
# else:
#     print("free")
# print("wish you good luck")
#
# # 做练习
# print('欢迎来到小路奶茶店')
# money = int(input("你有多少钱："))
# vip = int(input("你的vip等级是："))
# if money >= 50:
#     print("恭喜大佬免费喝")
# elif vip >3:
#     print("由于您等级高免费喝")
# else:
#     print("请付款")
#
# print('欢迎来到小路奶茶店')
# if int(input("你有多少钱：")) >= 50:
#     print("恭喜大佬免费喝")
# elif int(input("你的vip等级是")) > 3:
#     print("由于您等级高免费喝")
# else:
#     print("请付款")
#
year = int(input("随意输入一个年份："))
date = int(input("再输入一个月份："))
# if (year % 100 != 0) & (year % 4 == 0):
#     if date == 2:
#         print("this month:28 days")
#     elif date == 1 or date == 3 or date == 5 or date == 7 or date == 8 or date == 10 or date == 12:
#         print("this month:31 days")
#     else:
#         print("this month:30 days")
# elif year % 400 == 0:
#     # if date == 2:
#     #     print("this month:28 days")
#     # elif date == 1 or date == 3 or date == 5 or date == 7 or date == 8 or date == 10 or date == 12:
#     #     print("this month:31 days")
#     # else:
#     #     print("this month:30 days")
# else:
#     if date == 2:
#         print("this month:29 days")
#     elif date == 1 or date == 3 or date == 5 or date == 7 or date == 8 or date == 10 or date == 12:
#         print("this month:31 days")
#     else:
#         print("this month:30 days")
if date == 2:
    if (year % 100 != 0) & (year % 4 == 0) | year % 400 == 0:
        print("this month: 28")
    else:
        print("this month:29")
elif date == 1 or date == 3 or date == 5 or date == 7 or date == 8 or date == 10 or date == 12:
    print("this month:31")
else:
    print("this month:30")

