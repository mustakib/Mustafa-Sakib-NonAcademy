# Variable and Datatypes: 
name = "Mustafa Saadman Sakib"
age = 26
student = False
print(type(name))
print(type(age))
print(type(student))

# Arithmatic Operator:
w = age * 3
print(w)
x = age + 3
print(x)
y = age / 3
print(y)
z = age - 3
print(z)

# Comparison Operator:
print(age > 18)
print(age == 23)
print(age != 23)
print(age < 23)

# Logical Operator:
a = 15
b = 65
print(a < 17 and b > 70)
print(a > 14 or b < 60)
print(not(a > 14 or b < 60))

# Assignment Operator:
m = 25
m += 25
print(m)
m -= 25
print(m)
m *= 2
print(m)
m /= 5
print(m)

# Identity Operator:
x = 32
y = 8
print(x is y)
print(x is not y)

# Membership Operator:
buy = ["car", "house", "phone"]
print("car" in buy)
print("hotel" not in buy)