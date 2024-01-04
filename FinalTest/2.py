class Drinkstore:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

class Cold(Drinkstore):
    def __init__(self, name, size, price, ice_level, sugar_level):
        #用super父子繼承
        super().__init__(name, size, price)
        self.ice_level = ice_level
        self.sugar_level = sugar_level

    def __str__(self):
        # 返回包含冰品質和糖度的飲料描述
        return f"{self.name} (冷飲) - 大小: {self.size}, 價格: {self.price} 元, 冰量: {self.ice_level}, 糖度: {self.sugar_level}"

class Hot(Drinkstore):
    def __init__(self, name, size, price, sugar_level):
        super().__init__(name, size, price)
        self.sugar_level = sugar_level

    def __str__(self):
        # 返回包含糖度的熱飲描述
        return f"{self.name} (熱飲) - 大小: {self.size}, 價格: {self.price} 元, 糖度: {self.sugar_level}"

# 使用示例
cold_drink = Cold("Iced Tea", "大", 50.0, "少冰", "半糖")
hot_drink = Hot("Coffee", "中", 40.0, "微糖")
cold_drink1 = Cold("Juice", "小", 50.0, "微冰", "無糖")

print(cold_drink)
print(hot_drink)
print(cold_drink1)


