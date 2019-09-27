import add
import sub
import mult
import div
import sys

global a, b


args = sys.argv
# print("enter operaton:\n1-add\n2-sub\n3-prod\n4-div\nchoice:\t")
choice, a, b = args[1], int(args[2]), int(args[3])
print(choice, a, b)

ans = 0
if choice=="1":
	print("Adding", a, b)
	ans = add.addition(a, b)
if choice=="2":
	print("Subtracting", a, b)
	ans = sub.subtraction(a, b)
if choice=="3":
	print("Multiplying", a, b)
	ans = mult.multiplication(a, b)
if choice=="4":
	print("Dividing", a, b)
	ans = div.divide(a, b)

print()
print(ans)