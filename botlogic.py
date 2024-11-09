import random

def generatePassword(passwordLen):
    elements = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    password = ""
    for i in range(passwordLen):
        password += random.choice(elements)
    return password
