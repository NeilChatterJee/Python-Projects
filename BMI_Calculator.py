def BMI_Calculator():
    print("Hello Human! This Tool Will Tell You Your BMI Based On Weight and Height!")
    Weight = int(input("Please Input Your Weight In Kilograms: "))
    Height = int(input("Please Input Your Height In Meters: "))
    Height_Squared = Height * Height
    if float((Weight / Height_Squared)) < 18.5:
        print("Underweight")
    elif float((Weight / Height_Squared)) > 18.5 and float((Weight / Height_Squared)) < 25:
        print("Normal Weight")
    elif float((Weight / Height_Squared)) > 24.9 and float((Weight / Height_Squared)) < 30:
        print("Overweight")
    elif float((Weight / Height_Squared)) > 30: 
        print("You Have Obesity, Eat Less")

BMI_Calculator()