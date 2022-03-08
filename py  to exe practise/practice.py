#Git test.

data=[{'name':'tom','age':'18','city':'SZ'},
      {'name':'micky','age':'12','city':'SH'}]


class Student:
    def __init__(self,name,age,city):
         self.name=name
         self.age=age
         self.city=city


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
            elif op=='3':
                self.search()
            elif op=='4':
                self.modifystu()
            elif op=='5':
                self.rmdata()
            elif op == '0':
                break


            else:
                print('输入正确序号')

    def printdata(self,printdata):
        for index, student in enumerate(printdata):
            print(f'No.{index + 1}', end='\t')
            print(f'姓名：{student.name}', end='\t')
            print(f'年龄：{student.age}', end='\t')
            print(f'城市：{student.city}')


    def adddata(self):
        name= input('输入姓名:')
        age=input('输入年龄:')
        city=input('输入城市:')
        student=Student(name,age,city)
        self.data.append(student)

    def rmdata(self):
        rmname=self.searchbyname()
        if rmname:
           self.printdata(rmname)
           num = int(input('chose no. for modify:'))
           rmlist=rmname[num-1]
           self.data.remove(rmlist)



    def search(self):
        result=self.searchbyname()
        if result:
           self.printdata(result)

    def modifystu(self):
        newname = self.searchbyname()
        if newname:
           self.printdata(newname)
           num=int(input('chose no. for modify:'))
           student = newname[num-1]
           name = input('输入姓名:')
           age = input('输入年龄:')
           city = input('输入城市:')
           if name :
              student.name = name
              student.age=age
              student.city==city

    def searchbyname(self):
        stulist=[]
        keyword = input('Input search name:')
        for stu in self.data:
            if keyword.lower() in stu.name.lower():
               stulist.append(stu)

        if stulist:
            return  stulist
        else:
            print(f'NO message about {keyword}.')

    def showall(self):
      #  for student in self.data:
       #     print(student.name,student.age,student.city)
         self.printdata(self.data)

if __name__=='__main__':
    student_sys=System('学生信息系统')
    student_sys.run()