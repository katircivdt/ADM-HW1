#1 -)EXCEPTIONS

# if any error occur do not stop the process and after printing the error continue
for i in range(int(input())):
    try:
        number1 = input().split()
        print(int(number1[0]) // int(number1[1]))
    except ZeroDivisionError as c:
        print("Error Code:", c)

    except ValueError as v:
        print("Error Code:", v)
