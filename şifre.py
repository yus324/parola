import random

harfler ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk =int(input("parola uzunluğunu giriniz"))

parola =""
for i in range(uzunluk):
    sembol =random.choice(harfler)
    parola=parola+sembol


print (parola)

