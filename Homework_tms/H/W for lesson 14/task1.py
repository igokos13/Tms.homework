def digit_Finobachi(user_value:int)->int:
    a = 0
    b = 1
    
    for _ in range(user_value):
        yield a
        a, b = b, a + b
        
user_value = int(input('Введите значение: ')) 
my_list_generation = digit_Finobachi(user_value)
for number in my_list_generation:
    print(number)

digit_Finobachi(user_value)
    