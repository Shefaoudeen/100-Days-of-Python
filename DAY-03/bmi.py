height = float(input())
weight = float(input())

bmi = round(weight/(height**2), 2)

if bmi < 18.5:
    print("The person is underweight")
elif bmi < 25:
    print("The person is in normal weight")
elif bmi < 30:
    print("The person is slightly overweight")
elif bmi < 35:
    print("The  person is in obese")
else:
    print("The person is clinically obese")
