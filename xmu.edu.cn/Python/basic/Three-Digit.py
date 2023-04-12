def three_digit(number):

    ones = int(number%10)
    tens = int((number-ones)%100/10)
    hundreds=int((number-ones-tens)%1000/100)
    print("The hundreds digit is", hundreds)
    print("The tens digit is", tens)
    print("The ones digit is", ones)

print("Please input a three digit number or \"exit\" to quit")
number = input()
while number != "exit":
    if int(number) >= 100 and int(number) <=999:
        three_digit(int(number))
    else:
        print("Input Error! Please try again. ")
    number = input()