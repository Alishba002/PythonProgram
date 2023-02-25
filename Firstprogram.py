

        # ///variable type///


first_name = 'Alishba'
last_name = 'Abbas'
age = 21
age +=1
full_name = first_name +" "+ last_name
print(full_name)
print(age)
print(type(first_name))
print("Your age is: " + str(age))
print(type(age))
height = 750.5
print("your height is:" +str(height)+"cm")
print(type(height))
human = True
print("you are human :"+str(human))
print(type(human))


                # multiple assighnment


name="alishba"
age=21
attractive=True

name,age,arrtactive="alishba",21,True
print(name)
print(age)
print(arrtactive)

doraemon = nobita = jian = sunio = 10
print(doraemon)
print(nobita)
print(jian)
print(sunio)


            # string method


# STRING METHODS
# -------------------------------
name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")
name = "alishba abbas"
length = len(name)
index = name.find(" ")
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit() is string contain digits
result = name.isalpha() is string contain alphabetics
result = phone_number.count(" a")  how many words srting contain
print(name.count("a"))
phone_number = phone_number.replace("-", "")
print(name.replace("a","l"))
print("i love you"*100)
name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")

length = len(name)
index = name.find(" ")
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()
result = name.isalpha()
result = phone_number.count(" ")
phone_number = phone_number.replace("-", "")




# -------------------------------
#             Type casting
# convert data type of a value into another datatype
# -------------------------------



Type casting
Float
Int
string




                    # math function

#
import math

x  = 3
a = 16
b = 12.3455
y = [3,4,2,1,0]

p = a / x
z = a % x

print("a/x",round(p,3))
print("a%x",z)

print(pow(x,2))

print(math.sqrt(a))

print(round(b))

print(max(y))


#           ifelse statement

x = 5
z = 2
y = "alishba"

if x > 9:
    if y == "ali":
        print("Greater")
    else:
        print("not true")
elif z > 8:
    print("z")
else:
    print("Lesser")


          for statement

        for(int i = 1 ; i<5 ; i++)
        {
            print(i)
        # }
        x = int(input("Enter number => "))

        y = [1, "python", 2.3]

        for i in range(3):
            print(y[i])

        print("---------------")

        for i in y:
            print(i)
        print("---------------")
        for i in range(1, 5):
            print(i)
        print("---------------")
        for i in range(1, 5):
            for j in range(1, 3):
                print(i, j)

        print("---------------")
        while (x > 7):
            if x == 9:
                print | ("hello")
            # break;

            # x = x-1
            # continue;
            else:
                print("mavi")
            x = x - 1
        print("---------------")


#           user input


x = int(input("Enter the number =>"))

fact = 1

for i in range(2,x+1):
    fact = fact * i

print(fact)


           2D list

        1D
        x = [5, "mavi", 4.66]

        # for range 0 loop does not execute

        for i in range(0, 0)
        # for i in range(0,1)


        for i in x:
            print(i)

        # agar range() ==> indices
        for i in range(3):
            print(y[i])
        print("-----------------")
        # 2D  (Always traverse in nested)

        y = [[24, "mavi"], [3.6, "CS", 4], [5, "BSCS", 7]]

        full
        list
        for i in y:
            for j in range(0, len(i)):
                print(i[j])

        y[0][0] = 25

        for i in y:
            for j in range(0, len(i)):
                print(i[j])

        # for updation of any value you have to iterate loop as range()
        x = 0
        for i in range(len(y)):
            for j in range(i):
                y[i][0] = x + 1
        print(y)

#               Dictionary

honda = {
    "model" : "Rtype",
    "color" : "Black",
    "year" : 1990,
    "color" : "Blue",
    "features" : ["hybrid",2000]
}

print(honda["model"])
print(honda["year"])
print(honda["color"])

honda["year"] = 1991

print(honda["year"])

honda["features"][1] = 2100

print(honda["features"])
print(honda["features"][1])


              honda = {
            "model" : "Rtype",
            "color" : "Black",
            "year" : 1990,
            "color" : "Blue",
            "features" : ["hybrid",2000]
        }

        #full dictionary
        for i in honda:
            print(i , ":" , honda[i])

        print(honda["model"])
        print(honda["year"])
        print(honda["color"])

        #manipulations
        honda["year"] = 1991

        print(honda["year"])

        honda["features"][1] = 2100

        print(honda["features"])
        print(honda["features"][1])



#                   Return statement


        def Alishba(num):
            fact = 1

            for i in range(1, num + 1):
                fact = fact * i

            return fact, print("is fact"), "this"


        num = int(input("Enter the number => "))

        fact, p, done = Alishba(num)

        print(done, fact)


#               Nested function

        def Alishba(num):
            fact = 1

            for i in range(1, num + 1):
                fact = fact * i

            return fact


        def Input():
            print("Find Factorial of  Following Number:")
            num = int(input("Enter the number => "))
            fact = Alishba(num)
            return fact
            # this will not run
            print("code")
            print("done")


        fact = Input()

        print(fact)



#               Series sum


        # sum of the series
        # sum x^n / n!     n = 0--x    ;  x = user define
        def Alishba(num):
            fact = 1

            if (num == 0):
                return 1

            for i in range(1, num + 1):
                fact = fact * i

            return fact


        x = int(input("Enter the number => "))

        sum = 0
        for n in range(0, x + 1):
            sum = sum + pow(x, n) / Alishba(n)

        print(round(sum, 3))


#               String formating

x = "mavi"

y = "Alishba"
z = 4
q ="Apple"

print(f"{y} has {z} {q}")

print("{a} has {b} {c}".format(a = x,b=3,c="apples"))



#               Use of random function... Guess the number game


        import random

        num = random.randint(0, 100)

        tries = 0
        while (True):
            x = int(input("Enter the number => "))
            tries = tries + 1
            if x == num:
                print("you have won the game")
                break;

            elif x > num:
                print("your number is too high")

            elif x < num:
                print("your number is too low")

        if (tries > 7):
            print("Poor")
        elif (tries < 4):
            print("Excelent")
        elif (tries < 7 and tries > 4):
            print("Good")