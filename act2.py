##height and weight
height =float(input('Please put your height in cm'))
weight =float(input('Please put your weight in kg'))

##Give the intruction
BMI= weight / (height)**2
print('your BMI is' , BMI)

if BMI <= 18.4:
    print('You are underweight')
elif BMI <= 24.9:
    print('You are healthy ')
elif BMI <= 28.9:
    print('You are overweight ')
elif BMI <= 34.9:
    print('You are obease ')