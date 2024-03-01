try:
    age = int(input('Age: '))
    income = 100
    risk = income/ age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Wrong nigga')