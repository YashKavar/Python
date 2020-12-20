
a=10
b=5

try:
    print("Resource opend")
    print(a/b)
    k=int(input("Enter number"))
    print(k)

except ValueError as e:
    print("Invalid Input")

except ZeroDivisionError:
    print("You can not divide any value by zero")
except Exception as e:
    print("Something wrong....")

finally:
    print("Resource closed")
