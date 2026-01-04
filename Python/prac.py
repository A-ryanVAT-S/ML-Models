num = str(input("Enter the number :"))

i=0
j=len(num)-1

while i<j:
    if num[i]==num[j] :
        i+=1
        j-=1
        if i==j or j<i:
            print("palindrome")
    else:
        print("not a palindrome")
        break

    
