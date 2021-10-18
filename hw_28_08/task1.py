

def BTI_func(weight, height)->bool:
    BMI = weight / (height * height)
    if 18.5 < BMI < 25:
        return True
    else:
        return False

a = BTI_func(63, 1.68)
print(f'Your BMI is normal: {a}')