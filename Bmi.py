#BMI Calculator
name1 = "Brian"
height_m1 = 2
weight_kg1 = 80

name2 = "Moo"
height_m2 = 1.5
weight_kg2 = 70

name3 = "Kevo"
height_m3 = 1.8
weight_kg3 = 150

#to calculate the BMI of the three people a function is created
def bmi_calculator (name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi : ")
    print(bmi)
    if bmi < 25:
        return name  +  "not overweight" #two strings can be concanated using +
    else:
        return name  +  "is overweight"
#syntax for showing the output
result1 = bmi_calculator (name1, height_m1, weight_kg1) 
result2 = bmi_calculator (name2, height_m2, weight_kg2)
result3 = bmi_calculator (name3, height_m3, weight_kg3)

print (result1)
print (result2)
print (result3)

