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

class Employee:
    def __init__(self, name, experience, work_hours):
        self.name = name
        self.experience = experience
        self.work_hours = work_hours

    def get_name(self):
        # 查詢名字
        return self.name

    def get_experience(self):
        # 查詢年資
        return self.experience

    def get_work_hours(self):
        # 查詢工時
        return self.work_hours

    def calculate_salary(self):
        # 假設月薪計算為每小時工資乘以工作時數
        hourly_wage = 186.0  # 假設每小時工資為186元
        return hourly_wage * self.work_hours


employee1 = Employee("蛋寶", 5, 160)
employee2 = Employee("熱狗", 3, 140)
employee3 = Employee("ozi", 1, 120)

# 呼叫副函式
print("員工姓名:", employee1.get_name())
print("員工年資:", employee1.get_experience(), "年")
print("員工小時數:", employee1.get_work_hours(), "小時")
print("員工月薪:", employee1.calculate_salary(), "元")
print("員工姓名:", employee2.get_name())
print("員工年資:", employee2.get_experience(), "年")
print("員工小時數:", employee2.get_work_hours(), "小時")
print("員工月薪:", employee2.calculate_salary(), "元")
print("員工姓名:", employee3.get_name())
print("員工年資:", employee3.get_experience(), "年")
print("員工小時數:", employee3.get_work_hours(), "小時")
print("員工月薪:", employee3.calculate_salary(), "元")