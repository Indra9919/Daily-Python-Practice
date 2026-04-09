import math
print("Choose your triangle types")
print("1. Equilateral triangle")
print("2. Right Angle triangle")
print("3. Isosceles triangle")
print("4. Scalene triaengle")
choice=int(input("Enter your choice from 1 to 4:"))
if choice==1:
    side=float(input("Enter the side of Equilateral Triangle:"))
    area=(math.sqrt(3)/4)*side*side
    print("The area of Equilateral Triangle will be",area)
elif choice==2:
    base=float(input("Enter the base of Right Angle Triangle"))
    height=float(input("Enter the height of Right Angle Triangle"))
    area=0.5*base*height
    print("The area of Right Angle Triangle will be ",area)
elif choice==3:
    base=float(input("Enter the base of Isosceles triangle Triangle"))
    height=float(input("Enter the height of Isosceles triangle Triangle"))
    area=0.5*base*height
elif choice==4:
    a=float(input("Enter first Side"))
    b=float(input("Enter second Side"))
    c=float(input("Enter third Side"))
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The Area of Scalene Triangle will be",area)
else:
    print("Invalid choice")
    
    
    
    
    
