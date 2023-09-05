class Student:
    def __init__(self,name:str,chinese:int,english:int,math:int):
        #實體的attribute
        self.name = name
        self.chinese = chinese
        self.english = english
        self.math = math 

    #實體方法method
    def total(self)->int:
        return self.chinese + self.english + self.math
    
    #建立property->類似method,沒有參數,一定傳出一個值
    @property
    def average(self)->float:
        return self.total() / 3.0
    
    def __repr__(self):
        return f'我是student實體,我的name:{self.name}'