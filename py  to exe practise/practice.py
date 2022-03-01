
data=[{'name':'tom','age':'18','city':'SZ'},
      {'name':'micky','age':'12','city':'SH'}]

class Student:
    def __init__(self,name,age,city):
         self.name=name
         self.age=age
         self.city=city
1

class System:
    def __init__(self,name):
        self.name = name
        self.data=[]
    def showmenu(self):
        #f-string
        print(f"""
              **************************
              使用【{self.name}】
              1. 显示所有信息
              2. 新建
              3. 查询
              4. 修改
              5. 删除
              0. 退出
              **************************
        """)

    def loaddata(self):
        for item in data:
            student=Student(item['name'],item['age'],item['city'])
            self.data.append(student)

    def run(self):
        self.loaddata()
        while True:
            self.showmenu()
            op = input('选择操作编号:')
            if op=='1':
               self.showall()
            elif op=='2':
                self.adddata()


            elif op == '0':
                break

            else:
                print('输入正确序号')


    def adddata(self):
        name= input('输入姓名:')
        age=input('输入年龄:')
        city=input('输入城市:')
        student=Student(name,age,city)
        self.data.append(student)

    def showall(self):
      #  for student in self.data:
       #     print(student.name,student.age,student.city)
         for index,student in enumerate(self.data):
             print(f'No.{index+1}',end='\t')
             print(f'姓名：{student.name}',end='\t')
             print(f'年龄：{student.age}',end='\t')
             print(f'城市：{student.city}')

if __name__=='__main__':
    student_sys=System('学生信息系统')
    student_sys.run()