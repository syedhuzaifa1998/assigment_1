def reverse_name(n):
    if len(n) == 0:
        return n
    else:
        return reverse_name(n[1:]) + n[0]
    
print("Enter First Name")
first=input()
print("Enter Last Name")
last=input()
print("After Reverse")
print(reverse_name(first))
print(reverse_name(last))