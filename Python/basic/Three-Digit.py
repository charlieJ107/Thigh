
print("Enter a three digit number:")
number = int(input())
ones = int(number%10)
tens = int((number-ones)%100/10)
hundreds=int((number-ones-tens)%1000/100)
print("The hundreds digit is", hundreds)
print("The tens digit is", tens)
print("The ones digit is", ones)
