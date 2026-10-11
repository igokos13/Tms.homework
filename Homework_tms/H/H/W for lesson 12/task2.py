class Bus:
    def __init__(self,max_seets:int,max_speed:int,surnames:str,free_seets:bool):
        self.speed =0
        self.max_seets = max_seets
        self.max__speed = max_speed
        self.surnames = surnames
        self.free_seets = True
        self.seats = {}
    
    def update_free_seets(self):
        self.free_seets=len(self.surnames)<self.max_seets
        
    def board_passengers(self,*names):
        for name in names:
            if len(self.surnames)<self.max_seets:
                self.surnames.append(name)
                for seat_num in range(1, self.max_seets + 1):
                    if seat_num not in self.seats:
                        self.seats[seat_num]=name
                        break
                print(f' Пассажир {name} сел в автик') 
        else:
            print(f'нет свободного места для {name}')
        self.update_free_seets()
        
    def unboard_passengers(self, *names):
        for name in names:
            if name in self.surnames:
                self.surnames.remove(name)
            for seat_num, passenger in list(self.seats.items()):
                if passenger==name:
                    del self.seats[seat_num]
                    break
            print(f'Пассажир {name} вышел из автика')
        else:
            print(f'Пассажир {name} не найден')
        self.update_free_seets()
        
    def increase_speed(self,value):
        self.speed+=value
        if self.speed >self.max__speed:
            self.speed=self.max__speed
        print(f'Скорость увелична до {self.speed}')
    
    def decrease_speed(self, value):
        self.speed +=value
        if self.speed<0:
            self.speed=0
        print(f'Скорость уменьшена до {self.speed}')
        
    def __contains__(self, name):
        return name in self.surnames
    
    def __iadd__(self, name):
        self.board_passengers(name)
        return self
    
    def __isub__(self, name):
        self.unboard_passengers(name)
        return self
    
if __name__=='__main__':
    bus = Bus(max_seets=3, max_speed=120, surnames=[],free_seets=True)
    bus.board_passengers('Дима', 'Вася')
    bus +='Петя'
    print('Дима в автике?', 'Дима'in bus)
    print('Егор в автике?','Егор' in bus)
    bus +='Кузнецов'
    bus-='Вася'
    print('Есть свободные места ?', bus.free_seets)
    bus.increase_speed(20)
    bus.increase_speed(120)
    bus.increase_speed(60)
    print('Занятые места: ', bus.seats) #Было тяжело 
    