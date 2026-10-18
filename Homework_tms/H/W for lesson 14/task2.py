def cyclicality(user_number:int):
    while True:
        for number in range(1,user_number,+1):
            yield number
user_number = int(input('Введите кол-во цифр: '))
my_cycla = cyclicality(user_number)

for num in my_cycla:
    print(num)

cyclicality(user_number)
