# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# # range(start, stop, step) syntx
# for loop ar used to when you have a block of code which you want 
# to repeat a fixed number of time

for i in range(10):
    print("hello worls")

n = int(input("How many time do you want to print :"))
for i in range(n):
    print(i,"Hello World")

    # fellow use google colab link 
    # https://colab.research.google.com/drive/1BA_w_O88H7HPh6kQVfhTlQg5gQNpjWX4?usp=sharing

num = int(input("Enter Number : "))
for i in range(num):
    if i%2==0:
     print(i)
        # fellow use google colab link 
    # https://colab.research.google.com/drive/1BA_w_O88H7HPh6kQVfhTlQg5gQNpjWX4?usp=sharing

#    Write a program to reversed the Present Number.
num = int(input("Enter Any Number :"))
rev = 0
while num>0:
  rem = num % 10
  rev = (rev*10)+rem
  num = num // 10
print("Reversed Number : ",rev)

  # fellow use google colab link 
 # https://colab.research.google.com/drive/1BA_w_O88H7HPh6kQVfhTlQg5gQNpjWX4?usp=sharing
 
# Output

# Enter Any Number :483675
# Reversed Number : 576384