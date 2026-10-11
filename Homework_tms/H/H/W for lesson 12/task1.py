class Product:
    def __init__(self, name_product:str, name_shop:str, price:int):
        self.__name_product = name_product
        self.__name_shop = name_shop
        self.__price = price
        
    def get_name (self):
        return self.__name_product,
    
    def get_shop (self):
        return self.__name_shop
        
    def get_price(self):   
        return self.__price
    
    def print_info(self):
        print(f'товар{self.__name_product}, магазин {self.__name_shop}, цена {self.__price} руб')
    
    def __add__(self, other):
       return  self.__price + other.get_price()
   
class Warehouse:
    def  __init__(self):
        self.__products = []
    
    def add_product (self,prod):
        self.__products.append(prod)
        
    def search_for_index (self, index):
        tovar = self.__products[index]
        tovar.print_info()
        
    def search_for_name(self, name):
        for tovar in self.__products:
            if tovar.get_name()==name:
                tovar.print_info()
                
    def sort_for_name (self):
    
        def take_name(tovar):
            return tovar.get_name()
        
        self.__products.sort(key=take_name)
        
    def sort_for_shop(self):
        
        def take_shop(tovar):
            return tovar.get_shop()
        self.__products.sort(key=take_shop)
        
    def sort_for_price(self):
        
        def take_price(tovar):
            return tovar.get_price()
        self.__products.sort(key=take_price)
    
    def all(self):
        for tovar in self.__products:
            tovar.print_info()
        
p1 = Product("Яблоко", "Пятерочка", 100'руб')
p2 = Product("Банан", "Магнит", 80'руб')
p3 = Product("Груша", "Перекресток", 150'руб')

Summa = p1+p2
print (f'Сумма за яблоки и бананы: {Summa}')

apple = Warehouse ()
apple.add_product(p1)
apple.add_product(p2)

print('Товар под индексом 1 это: ')
apple.search_for_index(1)

print(' ищем: Груша')
apple.search_for_name('Груша') 

print('сортировка по цене товара: ')
apple.sort_for_price()
apple.all()
        