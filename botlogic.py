import random

def passwordGenerator(passwordLenght):
    elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"    
    password = ""
    for i in range(passwordLenght):
        password += random.choice(elements)
    return password
