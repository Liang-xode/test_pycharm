class Student:
    sum_122=0
    @staticmethod
    def menu():
        print("-------------")
        print("1.显示学生信息")
        print("2.修改学号")
        print("3.修改学院")
        print("4.学生总数")
        print("5.退出")
        print("-------------")
    def __init__(self,name_122,id_122,college_122):
        self.name=name_122
        self.id=id_122
        self.college=college_122
        Student.sum_122+=1
    def modify_id(self):
        self.id=input("请输入修改后的学号：")
    def modify_college(self):
        self.college=input("请输入修改后的学院：")
    def display(self):
        print("姓名：",self.name,"  学号：",self.id,"  学院：",self.college)
    @classmethod
    def display_122(cls):
        print("学生总人数：",cls.sum_122)
student1=Student('祥梁',202400502122,'计算机学院')
student2=Student('向量',202400502128,'计算机学院')
student3=Student('梁玖',202400502129,'人工智能学院')
Student.menu()
while True:
    choice=int(input("请输入选项："))
    if choice==1:
        print("学生信息如下：")
        student1.display()
        student2.display()
        student3.display()
    elif choice==2:
        student1.modify_id()
        print("修改后信息如下：")
        student1.display()
    elif choice==3:
        student1.modify_college()
        print("修改后信息如下：")
        student1.display()
    elif choice==4:
        Student.display_122()
    elif choice==5:
        break
    else:
        print("请输入对应选项！")
        continue

class Student:
    def __init__(self,name_122,age_122):
        self.__name=name_122
        self.__age=self.set(age_122)
    def set(self,age):
        if age<6 or age>30:
            print("输入不合法，将年龄置为6岁！")
            return 6
        else:
            return age
    def modify_age(self):
        new_age=int(input("请输入修改年龄:"))
        self.__age=self.set(new_age)
    def get_age(self):
        print("年龄：",self.__age)
    def display(self):
        print("学生信息如下：")
        print("姓名：",self.__name,"  年龄：",self.__age)
student1=Student('向量',99)
print("获取年龄：")
student1.get_age()
student1.modify_age()
student1.display()

