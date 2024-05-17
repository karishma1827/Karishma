from chef import Chef
class Continental_chef(Chef):
    def __init__ (self,name,veg_dish,nonveg_dish,spl_dish):
        super().__init__(name,veg_dish,nonveg_dish)
        self.spl_dish=spl_dish