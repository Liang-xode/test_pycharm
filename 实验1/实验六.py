# class General122:
#     def __init__(self,breed,name,age):
#         self.breed=breed
#         self.name=name
#         self.age=age
#     def run(self):
#         return f"，{self.name} 正在奔跑去"
#
# class Cat(General122):
#     def __init__(self,b,n,a,color):
#         super().__init__(b,n,a)
#         self.color=color
#     def catch_mouse(self):
#         return "抓老鼠"
#
# class Dog(General122):
#     def __init__(self,b,n,a,fur):
#         super().__init__(b,n,a)
#         self.fur=fur
#     def catch_rabbit(self):
#         return "去抓兔子"
# try:
#     cat=Cat("布偶猫","小一",2,"白色")
#     print(cat.name,cat.age,cat.color,cat.run(),cat.catch_mouse())
# except Exception as err:
#     print(f"出现了错误：{err}")
# try:
#     dog=Dog("牧羊犬","小七",3,"长毛")
#     print(dog.name,dog.age,dog.fur,dog.run(),dog.catch_rabbit())
# except Exception as err:
#     print(f"出现了错误：{err}")
 # 第二题
class Person122:
        def __init__(self,name,gender,age,phone):
            self.name=name
            self.gender=gender
            self.age=age
            self.phone=phone
class Teacher(Person122):
    def __init__(self,n,g,a,p,course):
        super().__init__(n,g,a,p)
        self.course=course
    def show1(self):
        print(f"教师信息如下")
        print(f"姓名：{self.name}")
        print(f"性别：{self.gender}")
        print(f"年龄：{self.age}")
        print(f"电话：{self.phone}")
        print(f"所教授的课程：{self.course}")

    def amend(self,name=None,gender=None,age=None,phone=None,course=None):
        if name:
            self.name=name
        if gender:
            self.gender=gender
        if age:
            self.age=age
        if phone:
            self.phone=phone
        if course:
            self.course=course

class Student(Person122):
    def __init__(self,n,g,a,p,grade):
        super().__init__(n,g,a,p)
        self.grade=grade

    def show2(self):
        print(f"学生信息如下")
        print(f"姓名：{self.name}")
        print(f"性别：{self.gender}")
        print(f"年龄：{self.age}")
        print(f"电话：{self.phone}")
        print(f"成绩：{self.grade}")
    def mean(self):
        print('平均成绩',sum(self.grade)/len(self.grade))

try:
    teacher=Teacher("文杰","男",34,888,course=("数学","物理"))
    teacher.show1()
    print("修改手机号以及年龄")
    teacher.amend(age=36,phone=666)
    teacher.show1()
    student=Student("小宁","女",18,777,grade=(90,78))
    student.show2()
    student.mean()
except Exception as e:
    print(f"出现了错误：{e}")
#
# try:
#     teacher=Teacher("da ","男",34,155,course=("数学","物理"))
#     teacher.show1()
#     teacher.amend(phone=4)
#     teacher.show1()
#     student=Student("李四","男",19,148,grade=(90,78))
#     student.show2()
#     student.mean()
# except Exception as e:
#     print(f"出现了错误：{e}")