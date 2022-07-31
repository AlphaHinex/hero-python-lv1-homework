class People():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


people = People('李磊', '10岁', '男生')
print(people.age + '的' + people.gender + people.name)
