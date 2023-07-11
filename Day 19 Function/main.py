# function in python 
# function is a block of code which only run when its calls

# Example : 

def greeting():
    print("Good Morning Everyone")
    print("Good Evening Everyone")
    print("Good night Everyone")
greeting()
greeting()
greeting()

# example 2
def func(val1):
    print("input :", val1)
func(10)
func(20)
func(30)

# write a programm to find square of number using function 
def cal_square(num):
    square = num * num
    print("square : ",square)
cal_square(5)
cal_square(10)


# return values in python 
def cal_sq(num):
    sq = num *num
    return sq
ans = cal_sq(5)
print(ans)

# example using user input
def sqaure():
    num = int(input("enter num : "))
    sq = num *num
    return sq
ans = sqaure()
print(ans)

#  fellow use google colab link 
# https://colab.research.google.com/drive/1u3hc65cfyiT-xOWG3oOI61EKnMi3BKNh?usp=sharing
