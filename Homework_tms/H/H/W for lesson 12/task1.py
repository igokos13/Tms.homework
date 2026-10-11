class Product:
    def __init__(self, name_product:str, name_shop:str, price:int):
        self.__name_product = name_product
        self.__name_shop = name_shop
        self.__price = price
        
    def get_product (self):
        return self.__name_product, self.__name_shop, self.__price
shop = Product('Apple', 'Pyaterochka', 100)

print(shop.get_product())