# Problem
'''
A program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.
'''

#Solution:

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# Calculation:
H = float(height)
W = float(weight)
BMI = float(W / (H**2))
# Conditions to be checked
if BMI < 18.5:
  print (f"Your BMI is {BMI}, you are underweight.")
elif 18.5 <= BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25 <= BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif 30 <= BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")

# Example Input :
'''
1.75
80
'''
# Example Output:
'''
Your BMI is 26.122448979591837, you are slightly overweight.
'''