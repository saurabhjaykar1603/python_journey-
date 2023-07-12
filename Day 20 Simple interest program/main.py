# write a program to find simple interest using function all cases
# HINT : simple interest = (P * T * R)*100 P is the Principle amount T is time and R is the rate 

# no argument and no return - solution no. 1
def cal_si():
    p = int(input("Enter Principle : "))
    r = int(input("Enter rate of interest : "))
    t = int(input("Enter Time of period : "))
    si = p*r*t/100
    print(si)
cal_si()

#  fellow use google colab link 
# https://colab.research.google.com/drive/1gi3oa3hGNSUXjjfuenS8z9sN2QwwTK1c?usp=sharing


# Argument but no return solution no . 2

def cal_si(p,r,t):
    si = (p*r*t)/100
    print(si)
Amount = int(input("Enter Amount : "))
Rate = int(input("Enter Rate : "))
Time = int(input("Enter Time : "))

#  fellow use google colab link 
# https://colab.research.google.com/drive/1gi3oa3hGNSUXjjfuenS8z9sN2QwwTK1c?usp=sharing

# no argument but return solution no . 3
def cal_si():
    p = int(input("Enter Principle : "))
    r = int(input("Enter Rate : "))
    t = int(input("Enter time : "))
    si = p*r*t/100
    return si
ans = cal_si()
print(ans)

# argument and return 
def cal_si(p,r,t):
    si = p*r*t/100
    return si
Amount = int(input("Enter Amount : "))
Rate = int(input("Enter Rate : "))
Time = int(input("Enter Time : "))

ans = cal_si(Amount,Rate,Time)
print(ans)


#  fellow use google colab link 
# https://colab.research.google.com/drive/1gi3oa3hGNSUXjjfuenS8z9sN2QwwTK1c?usp=sharing

