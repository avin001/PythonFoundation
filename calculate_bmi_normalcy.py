def is_bmi_normal(weight_in_kg, height_in_m):
    if 18.5 <= weight_in_kg / (height_in_m)**2 < 25:
        print("Your BMI is considered 'normal'.")
    else:
        print("Your BMI is not considered 'normal'.")


is_bmi_normal(75, 1.8)
