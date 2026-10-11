class Bus:
    def __init__(self,max_seets:int,max_speed:int,surnames:str,free_seets:bool):
        self.speed =0
        self.max_seets = max_seets
        self.max__speed = max_speed
        self.surnames = surnames
        self.free_seets = True
        self.seats = {}