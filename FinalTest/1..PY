class FriedChicken:
    def __init__(self, name, flavor, size, price, crispy_level):
        self.name = name
        self.flavor = flavor
        self.size = size
        self.price = price
        self.crispy_level = crispy_level

    def display_info(self):
        
        print(f"{self.name} - 口味: {self.flavor}, 尺寸: {self.size}, 價格: {self.price} 元, 酥脆程度: {self.crispy_level}")

    def increase_crispiness(self, level_increase):
        """
        增加炸雞的酥脆程度
        :param level_increase: 增加的酥脆程度值
        """
        self.crispy_level += level_increase
        print(f"{self.name} 的酥脆程度提升了 {level_increase} 級！")

    def change_flavor(self, new_flavor):
        
        self.flavor = new_flavor
        print(f"{self.name} 的口味變更為 {new_flavor}！")

# 建立4個炸雞物件
chicken1 = FriedChicken("香辣雞翅", "香辣", "小份", 50, 8)
chicken2 = FriedChicken("櫻花蝦鹽酥雞", "鹽酥", "中份", 80, 7)
chicken3 = FriedChicken("蜜汁照燒雞排", "蜜汁照燒", "大份", 120, 6)
chicken4 = FriedChicken("黑胡椒鹽酥雞", "黑胡椒", "特大份", 150, 9)

# 分別呼叫副函式
chicken1.display_info()
chicken1.increase_crispiness(1)
chicken1.change_flavor("辣味")
chicken1.display_info()
""""""
chicken2.display_info()
chicken2.increase_crispiness(2)
chicken2.change_flavor("芥末")
chicken2.display_info()
""""""
chicken3.display_info()
chicken3.increase_crispiness(2)
chicken3.change_flavor("梅粉")
chicken3.display_info()
""""""
chicken4.display_info()
chicken4.increase_crispiness(1)
chicken4.change_flavor("海苔")
chicken4.display_info()