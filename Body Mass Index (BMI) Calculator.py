#!/usr/bin/env python
# coding: utf-8

# # Body Mass Index (BMI) Calculator

# In[ ]:





# In[5]:


print("For Metric System, write down 1\n")
print("For English Metric System, write down 2\n")

while True:
    input_first = input("Select your metric system: \n")
    if input_first in ('1', '2'):
        input_first = int(input_first)
        break
    else:
        print("Please enter a valid option: 1 for Metric System, 2 for English Metric System.\n")

if input_first == 1:
    print("You selected the Metric System\n")
    while True:
        print("Now write the following information: \n")
        name = input("Name: \n")
        height = float(input("Enter your height in meters: \n"))
        weight = float(input("Enter your weight in kilograms: \n"))
        if height > 0 and weight > 0 and name.isalpha():
            break
        else:
            print("Invalid input. Name, height, and weight must be provided and positive numbers.\n")
            print("Invalid input. Name must contain only characters, no numbers.\n")
    
    BMI = weight / (height**2)
    if BMI < 18.5:
        print(name + ", you are underweight. Your BMI is: " + str(BMI))
    elif BMI <= 24.9:
        print(name + ", you are normal weight. Your BMI is: " + str(BMI))
    elif BMI < 29.9:
        print(name + ", you are overweight. Your BMI is: " + str(BMI))
    elif BMI < 34.9:
        print(name + ", you are obese. Your BMI is: " + str(BMI))
    elif BMI < 39.9:
        print(name + ", you are severely obese. Your BMI is: " + str(BMI))
    else:
        print(name + ", you are morbidly obese. Your BMI is: " + str(BMI))

elif input_first == 2:
    print("You selected the English System\n")
    while True:
        print("Now write the following information: \n")
        name = input("Name: \n")
        height = float(input("Enter your height in foot: \n"))
        weight = float(input("Enter your weight in pounds: \n"))
        if height > 0 and weight > 0 and name.isalpha():
            break
        else:
            print("Invalid input. Name, height, and weight must be provided and positive numbers.\n")
            print("Invalid input. Name must contain only characters, no numbers.\n")
    
    BMI = (weight / (height**2)) * 703  
    if BMI < 18.5:
        print(name + ", you are underweight. Your BMI is: " + str(BMI))
    elif BMI <= 24.9:
        print(name + ", you are normal weight. Your BMI is: " + str(BMI))
    elif BMI < 29.9:
        print(name + ", you are overweight. Your BMI is: " + str(BMI))
    elif BMI < 34.9:
        print(name + ", you are obese. Your BMI is: " + str(BMI))
    elif BMI < 39.9:
        print(name + ", you are severely obese. Your BMI is: " + str(BMI))
    else:
        print(name + ", you are morbidly obese. Your BMI is: " + str(BMI))

else:
    print("Please select an acceptable value: 1 or 2\n")


# In[ ]:




