import random

caracteres = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

longitud_contra = int(input("Escribe la longitud de tu contraseña: "))
contraseña = ""

for i in range(longitud_contra):
    x = random.choice(caracteres)
    contraseña += x

print(contraseña)
