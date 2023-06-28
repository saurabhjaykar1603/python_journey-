# Write a Program ask user to Enter rate and quantity of a product your program should calculate and print the bill
# if bill is more thnan 500 then give 20% discount


rate, quantity = input("Enter rate and Quantity").split()
bill = int(rate)* int(quantity)
if bill >500:
    print("### 20 % Off ###")
    print("Actual Bill", bill)
    discount =(bill/100)*20
    print("discount :",discount)
    print("Payble Amount :",bill-discount)
else :
    print("### 5 % Off ###")
    print("Actual Bill", bill)
    discount =(bill/100)*5
    print("discount :",discount)
    print("Payble Amount :",bill-discount)
    
    
    # use fellow link to exicute the code 
    # https://colab.research.google.com/drive/1rvoD_NyH0f3C7mmO4dW_6_DpjzIIMcU5?usp=sharing


# code optimization 
rate, quantity = input("Enter rate and Quantity").split()
bill = int(rate)* int(quantity)
disc_per = 0
if bill >500:
    disc_per =20
else :
    disc_per =5

discount =(bill/100)*disc_per
paybleAmount = bill - discount
print("####{} OFF". format(disc_per))
print("Actual Bill", bill)
print("Discount",discount)
print("Payble Amount :", paybleAmount)



