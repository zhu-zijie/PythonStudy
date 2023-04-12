'''
学生信息管理系统
'''
import os

filename = 'student.txt'
student_list = []
def insert():

    id = input(("请输入学生的ID：（如1001）"))
    name = input("请输入学生的姓名：")
    if not id or not name:
        print("输入无效，请重新输入！")
        return
    with open(filename, mode='r', encoding='utf-8') as rfile:
        student = rfile.readlines()
        for item in student:
            dic = eval(item)
            if dic['id'] == id:
                print("该学生信息已存在，请重新输入！")
                return
    try:
        english = int(input("请输入学生的英语成绩："))
        java = int(input("请输入学生的Java成绩："))
        python = int(input("请输入学生的Python成绩："))
        c = int(input("请输入学生的C语言成绩："))
    except:
        print("输入无效，请重新输入！")
        return
    student = {"id":id, "name":name, "English":english, "Java":java, "Python":python, "C语言":c}
    if 0<=english<=100 and 0<=java<=100 and 0<=python<=100 and 0<=c<=100:
        student_list.append(student)
        print("添加成功！")
        answer = input("是否继续添加？（y/n)")
        if answer=='y' or answer=='Y':
            insert()
        else:
            return save(student_list)
    else:
        print("输入的成绩无效，请重新输入！")
        insert()

def search():
    student_query = []
    id = ""
    name = ""
    if os.path.exists(filename):
        mode = input("按ID查找请输入1；按姓名查找请输入2！")
        if mode == '1':
            id = input("请输入查询学生的ID：")
        elif mode == '2':
            name = input("请输入查询学生的姓名：")
        else:
            print("您输入的有误，请重新输入！")
            search()
        with open(filename, mode='r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            for item in student:
                dic = eval(item)
                if id != "":
                    if dic['id'] == id:
                        student_query.append(item)
                elif name != "":
                    if dic['name'] == name:
                        student_query.append(item)
        # 显示查询结果
        show_student(student_query)
        answer = input("是否继续查询？（y/n）")
        if answer == 'y' or answer == 'Y':
            search()
        else:
            return

def show_student(lists):
    if len(lists) == 0:
        print("没有查询到学生的信息！")
        return
    else:
        # 定义标题显示格式
        format_title = '{:^6}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
        print(format_title.format('ID', '姓名', '英语成绩', 'Java成绩', 'Python成绩', 'C语言成绩', '总成绩'))
        # 定义内容显示格式
        for list in lists:
            dic = eval(str(list))
            format_data = '{:^6}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
            print(format_data.format(dic['id'], dic['name'], dic['English'], dic['Java'], dic['Python'], dic['C语言'],
                                     int(dic['English'])+int(dic['Java'])+int(dic['Python'])+int(dic['C语言'])))

def modify():
    show()
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input("请输入要修改学生的ID：")
    flag = False
    with open(filename, mode='w', encoding='utf-8') as wfile:
        for item in student_old:
            dic = eval(item)
            if dic['id'] == student_id:
                print("已学生的信息，可以进行修改！")
                while True:
                    try:
                        dic['English'] = int(input("请输入学生的英语成绩："))
                        dic['Java'] = int(input("请输入学生的Java成绩："))
                        dic['Python'] = int(input("请输入学生的Python成绩："))
                        dic['C语言'] = int(input("请输入学生的C语言成绩："))

                    except:
                        print("您的输入有误，请重新输入！")
                    else:
                        break

                wfile.write(str(dic)+'\n')
                flag = True
            else:
                wfile.write(str(dic)+'\n')

    if flag:
        print("修改成功！")
    else:
        print(f"没有找到{student_id}学生信息！")
    answer = input("是否继续修改学生的信息？（y/n）")
    if answer == 'y' or answer == 'Y':
        modify()
    else:
        return

def delete():
    student_id = input("请输入要删除的学生ID：")
    if student_id != " ":
        if os.path.exists(filename):    #判断文件是否存在
            with open(filename, mode='r', encoding='utf-8') as rfile:
                student_old = rfile.readlines()
        else:
            student_old = []
        flag = False
        if student_old:
            with open(filename, mode='w', encoding='utf-8') as wfile:
                dic = {}
                for item in student_old:
                    dic = eval(item)
                    if dic['id'] != student_id:
                        wfile.write(str(dic)+'\n')
                    else:
                        flag = True
                if flag:
                    print("该学生的id已经被删除！")
                else:
                    print(f"没有找到{student_id}学生的信息！")
        else:
            print("无学生的信息，请录入学生信息！")
            return
        show()
        answer = input("是否继续删除学生信息？（y/n)")
        if answer=='y' or answer=='Y':
            delete()
        else:
            return

def sort():
    show()
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            student_list = file.readlines()
        student_new = []
        for student in student_list:
            student_new.append(eval(student))
    else:
        print("文件不存在！")
    choice = input("请选择排序方式：（0为升序；1为降序）")
    if choice == '0':
        choice_bool = False
    elif choice == '1':
        choice_bool = True
    else:
        print("您的输入有误，请重新输入！")
        sort()
    mode = input("请选择排序的模式：（1为按英语成绩排；2为按Java成绩排；3为按Python成绩排；4为按C语言成绩排；0为按总成绩排")
    if mode == '1':
        student_new.sort(key=lambda student: int(student['English']), reverse=choice_bool)
    elif mode == '2':
        student_new.sort(key=lambda student: int(student['Java']), reverse=choice_bool)
    elif mode == '3':
        student_new.sort(key=lambda student: int(student['Python']), reverse=choice_bool)
    elif mode == '4':
        student_new.sort(key=lambda student: int(student['C语言']), reverse=choice_bool)
    elif mode == '0':
        student_new.sort(key=lambda student: int(student['English'])+int(student['Java'])+int(student['Python'])+int(student['C语言']), reverse=choice_bool)
    else:
        print("您的选择有误，请重新尝试！")
        sort()
    show_student(student_new)

def total():
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            students = file.readlines()
            if students:
                print(f"一共有{len(students)}名学生！")
            else:
                print("没有学生的信息，请录入！")

    else:
        print("文件不存在！")

def show():
     if os.path.exists(filename):
         with open(filename, mode='r', encoding='utf-8') as file:
             students = file.readlines()
             student_list = []
             for student in students:
                 student_list.append(eval(student))
             if student_list:
                show_student(student_list)
             else:
                print("暂未查询到学生的信息！")
     else:
         print("文件不存在！")

def save(list):
    with open(filename, mode='a', encoding='utf-8') as file:
        for item in list:
            file.write(str(item)+'\n')

def menu():
    print("*************************学生信息管理系统*************************")
    print("*************************功能菜单*******************************")
    print("\t\t\t\t\t\t1.录用学生信息")
    print("\t\t\t\t\t\t2.查找学生信息")
    print("\t\t\t\t\t\t3.修改学生信息")
    print("\t\t\t\t\t\t4.删除学生信息")
    print("\t\t\t\t\t\t5.排序")
    print("\t\t\t\t\t\t6.统计学生总人数")
    print("\t\t\t\t\t\t7.显示所有的学生的信息")
    print("\t\t\t\t\t\t0.退出")

def main():
    while True:
        menu()
        try:
            choice = int(input("请输入你的选择："))
        except:
            print("请输入数字！")
            continue
        if choice==0:
            answer = input("您确定要退出系统吗？（y/n)")
            if answer=='y' or answer=='Y':
                print("谢谢您的使用！")
                break
            else:
                continue
        elif choice==1:
            insert()
        elif choice==2:
            search()
        elif choice==3:
            modify()
        elif choice==4:
            delete()
        elif choice==5:
            sort()
        elif choice==6:
            total()
        else:
            show()

if __name__ == '__main__':
    main()
