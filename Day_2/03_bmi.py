def bmi(weight, height):
    weight_as_int = int(weight)
    height_square_as_float = float(height) ** 2
    BMI = weight_as_int / height_square_as_float
    return int(BMI)

print(bmi(65, 1.67))