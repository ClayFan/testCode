class Car():
    def __init__(self,color,neishi,luntai,zuowei):
        self.color = color
        self.neishi = neishi
        self.luntai = luntai
        self.zuowei = zuowei
    
    def bianxing(self):
        print("变成大黄蜂")

wode = Car("红色","豪华","四轮","三座")
print(wode.color)
wode.bianxing()