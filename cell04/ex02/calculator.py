#!/usr/bin/env python3

num1 = float(input("Give me the first number: "))
num2 = float(input("Give me the second number: "))

print("Thank you!")

display_num1 = int(num1) if num1.is_integer() else num1
display_num2 = int(num2) if num2.is_integer() else num2

add = num1 + num2
sub = num1 - num2
div = num1 / num2
mul = num1 * num2

display_add = int(add) if add.is_integer() else add
display_sub = int(sub) if sub.is_integer() else sub
display_div = int(div) if div.is_integer() else div
display_mul = int(mul) if mul.is_integer() else mul

print(f"{display_num1} + {display_num2} = {display_add}")
print(f"{display_num1} - {display_num2} = {display_sub}")
print(f"{display_num1} / {display_num2} = {display_div}")
print(f"{display_num1} * {display_num2} = {display_mul}")
