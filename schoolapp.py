from tkinter import *
from tkinter.messagebox import *
import mysql.connector as sq


def main1():
      def  empda():
            def datate():
                  Ans = int(num1.get())
                  Ans1=(num2.get())
                  Ans2=(num3.get())
                  Ans3=int(num4.get())
                  Ans4=(num5.get())
                  Ans5=(num6.get())
                  Ans6=(num7.get())
                  Ans7=int(num8.get())
                  i="insert into employee_data ( employee_no,employee_name,date_of_birth,age,gender,designation ,data_of_joining,salary) values({},'{}','{}',{},'{}','{}','{}',{})".format(Ans,Ans1,Ans2,Ans3,Ans4,Ans5,Ans6,Ans7)
                  c.execute(i )
                  a.commit()
                  num1.delete(0, 'end')
                  num2.delete(0, 'end')
                  num3.delete(0, 'end')
                  num4.delete(0, 'end')
                  num5.delete(0, 'end')
                  num6.delete(0, 'end')
                  num7.delete(0, 'end')
                  num8.delete(0, 'end')
            main = Tk()
            Label(main, text = "employee no:").grid(row=0)
            Label(main, text = "employee name:").grid(row=1)
            Label(main, text = "date of birth(dd/mm/yyyy):").grid(row=2)
            Label(main, text = "age:").grid(row=3)
            Label(main, text = "gender:").grid(row=4)
            Label(main, text = "designation:").grid(row=5)
            Label(main, text = "data of joining(dd/mm/yyyy):").grid(row=6)
            Label(main, text = "salary:").grid(row=7)
            num1 = Entry(main)
            num2 = Entry(main)
            num3 = Entry(main)
            num4=Entry(main)
            num5=Entry(main)
            num6=Entry(main)
            num7 = Entry(main)
            num8=Entry(main)
            num1.grid(row=0, column=1)
            num2.grid(row=1, column=1)
            num3.grid(row=2, column=1)
            num4.grid(row=3, column=1)
            num5.grid(row=4, column=1)
            num6.grid(row=5, column=1)
            num7.grid(row=6,column=1)
            num8.grid(row=7,column=1)
            Button(main, text='Quit', command=main.destroy).grid(row=8, column=0, sticky=W, pady=4)
            Button(main, text='enter', command=datate).grid(row=8, column=1, sticky=W, pady=4)
      def  main3():
            def dis():
                  print(num)
                  rf=int(num.get())
                  ad=()
                  print(data)
                  sw=0
                  for x in data:
                        if x[0]==rf :
                              ad=data[sw]
                              print(ad)
                              break
                        else:
                              ad=()
                              sw+=1
                  print(ad)
                  if ad!=():
                        main= Tk()
                        Label(main, text = "employee no:").grid(row=0)
                        Label(main, text = "employee name:").grid(row=1)
                        Label(main, text = "date of birth(dd/mm/yyyy):").grid(row=2)
                        Label(main, text = "age:").grid(row=3)
                        Label(main, text = "gender:").grid(row=4)
                        Label(main, text = "designation:").grid(row=5)
                        Label(main, text = "data of joining(dd/mm/yyyy):").grid(row=6)
                        Label(main, text = "salary:").grid(row=7)
                        num1 = Entry(main)
                        num2 = Entry(main)
                        num3 = Entry(main)
                        num4=Entry(main)
                        num5=Entry(main)
                        num6=Entry(main)
                        num7 = Entry(main)
                        num8=Entry(main)
                        num1.grid(row=0, column=1)
                        num2.grid(row=1, column=1)
                        num3.grid(row=2, column=1)
                        num4.grid(row=3, column=1)
                        num5.grid(row=4, column=1)
                        num6.grid(row=5, column=1)
                        num7.grid(row=6,column=1)
                        num8.grid(row=7,column=1)
                        Button(main, text='Quit', command=main.destroy).grid(row=8, column=0, sticky=W, pady=4)
                        num1.insert(0,ad[0])
                        num2.insert(0,ad[1])
                        num3.insert(0,ad[2])
                        num4.insert(0,ad[3])
                        num5.insert(0,ad[4])
                        num6.insert(0,ad[5])
                        num7.insert(0,ad[6])   
                        num8.insert(0,ad[7])     
                            
                       
                  else:
                        maine= Tk()
                        Label(maine, text = "no entry found!!!!!!!",width=15,height=5).grid(row=1)
                        Button(maine, text='back', command=maine.destroy).grid(row=10,column=1)
                        
                  
                              
            i='select * from employee_data'                              
            c.execute(i )
            data=list(c.fetchall())
            maind = Tk()
            Label(maind, text ='employee no:').pack()
            num = Entry(maind)
            num.pack()
            Button(maind, text='show', command=dis).pack()
            Button(maind, text='back', command=maind.destroy).pack()
            
      def choice():
             mainc = Tk()
             Label(mainc, text = "SELECT ").grid(row=1,column=1)
             Button(mainc, text='ENTER VALUES', command= empda,width=20).grid(row=3,column=1)
             Button(mainc, text='DISPLAY TABLE', command=main3,width=20).grid(row=5,column=1)
             Label(mainc, text = "").grid(row=0,column=0)
             for i in range(2,7,2):
                   Label(mainc, text = "").grid(row=i,column=2)
      def passw():
                Ans = str(num1.get())
                global a
                a=sq.connect(host='localhost',user='root',passwd=Ans)
                if a.is_connected:
                        print("yes")
                global c
                c=a.cursor()
                e=c.execute("create database if not exists  admin")
                print("yes")
                f=c.execute("use admin")
                i=c.execute("create table if not exists employee_data (employee_no int(10) primary key,employee_name varchar(30),date_of_birth varchar(10),age int(2),gender char(1),designation varchar(30),data_of_joining varchar(10),salary int(7))")
                choice()
      #entry for password of mysql database
      main = Tk()
      Label(main, text = "enter password:").grid(row=1)
      num1 = Entry(main,show='*')
      num1.grid(row=1, column=1)
      Button(main, text='ENTER', command= passw,width=20).grid(row=3, column=1, sticky=W, pady=5)
      Label(main, text = "").grid(row=0,column=0)
      for i in range(2,5,2):
                   Label(main, text = "").grid(row=i,column=2)
      mainloop()
      
def main2():
      def main2():
            def show_answer():
                  Ans = int(num1.get())
                  Ans1=(num2.get())
                  Ans2=(num3.get())
                  Ans3=(num4.get())
                  Ans4=(num5.get())
                  Ans5=(num6.get())
                  Ans6=(num7.get())
                  Ans7=(num8.get())
                  Ans8=(num9.get())
                  Ans9=int(num10.get())
                  i="insert into  student_detail (admin_no ,name ,date_of_admin ,date_of_birth,gender ,category ,father_name,mother_name,address ,phone_no ) values({},'{}','{}','{}','{}','{}','{}','{}','{}',{})".format(Ans,Ans1,Ans2,Ans3,Ans4,Ans5,Ans6,Ans7,Ans8,Ans9)
                  c.execute(i )
                  a.commit()
                  num1.delete(0, 'end')
                  num2.delete(0, 'end')
                  num3.delete(0, 'end')
                  num4.delete(0, 'end')
                  num5.delete(0, 'end')
                  num6.delete(0, 'end')
                  num7.delete(0, 'end')
                  num8.delete(0, 'end')
                  num9.delete(0, 'end')
                  num10.delete(0, 'end')
                  

            main = Tk()
            Label(main, text = "admin no:").grid(row=0)
            Label(main, text = "name:").grid(row=1)
            Label(main, text = "date of admin(dd/mm/yyyy)").grid(row=2)
            Label(main, text = "date of birth:").grid(row=3)
            Label(main, text = "gender:").grid(row=4)
            Label(main, text = "category:").grid(row=5)
            Label(main, text = "father's name:").grid(row=6)
            Label(main, text = "mother's name:").grid(row=7)
            Label(main, text = "address:").grid(row=8)
            Label(main, text = "phone no:").grid(row=9)


            num1 = Entry(main)
            num2 = Entry(main)
            num3 = Entry(main)
            num4=Entry(main)
            num5=Entry(main)
            num6=Entry(main)
            num7 = Entry(main)
            num8 = Entry(main)
            num9 = Entry(main)
            num10 = Entry(main)
            


            num1.grid(row=0, column=1)
            num2.grid(row=1, column=1)
            num3.grid(row=2, column=1)
            num4.grid(row=3, column=1)
            num5.grid(row=4, column=1)
            num6.grid(row=5, column=1)
            num7.grid(row=6, column=1)
            num8.grid(row=7, column=1)
            num9.grid(row=8,column=1)
            num10.grid(row=9,column=1)


            Button(main, text='Quit', command=main.destroy).grid(row=10, column=0, sticky=W, pady=4)
            Button(main, text='enter', command=show_answer).grid(row=10, column=1, sticky=W, pady=4)

            mainloop()
      def  main3():
            def dis():
                  print(num)
                  rf=int(num.get())
                  ad=()
                  print(data)
                  sw=0
                  for x in data:
                        if x[0]==rf :
                              ad=data[sw]
                              print(ad)
                              break
                        else:
                              ad=()
                              sw+=1
                  print(ad)
                  if ad!=():
                        main= Tk()
                        Label(main, text = "admin no:").grid(row=0)
                        Label(main, text = "name:").grid(row=1)
                        Label(main, text = "date of admin(dd/mm/yyyy)").grid(row=2)
                        Label(main, text = "date of birth:").grid(row=3)
                        Label(main, text = "gender:").grid(row=4)
                        Label(main, text = "category:").grid(row=5)
                        Label(main, text = "father's name:").grid(row=6)
                        Label(main, text = "mother's name:").grid(row=7)
                        Label(main, text = "address:").grid(row=8)
                        Label(main, text = "phone no:").grid(row=9)
                        num1 = Entry(main)
                        num2 = Entry(main)
                        num3 = Entry(main)
                        num4=Entry(main)
                        num5=Entry(main)
                        num6=Entry(main)
                        num7 = Entry(main)
                        num8=Entry(main)
                        num9 = Entry(main)
                        num10 = Entry(main)
                        num1.grid(row=0, column=1)
                        num2.grid(row=1, column=1)
                        num3.grid(row=2, column=1)
                        num4.grid(row=3, column=1)
                        num5.grid(row=4, column=1)
                        num6.grid(row=5, column=1)
                        num7.grid(row=6,column=1)
                        num8.grid(row=7,column=1)
                        num9.grid(row=8,column=1)
                        num10.grid(row=9,column=1)
                        Button(main, text='Quit', command=main.destroy,width=20).grid(row=10, column=0, sticky=W, pady=4)
                        num1.insert(0,ad[0])
                        num2.insert(0,ad[1])
                        num3.insert(0,ad[2])
                        num4.insert(0,ad[3])
                        num5.insert(0,ad[4])
                        num6.insert(0,ad[5])
                        num7.insert(0,ad[6])   
                        num8.insert(0,ad[7])
                        num9.insert(0,ad[8])   
                        num10.insert(0,ad[9])   
                            
                       
                  else:
                        maine= Tk()
                        Label(maine, text = "no entry found!!!!!!!",width=15,height=10).grid(row=1)
                        Button(maine, text='back', command=maine.destroy,width=20).grid(row=10,column=1)
                        
                  
                              
            i='select * from student_detail'                              
            c.execute(i )
            data=list(c.fetchall())
            maind = Tk()
            Label(maind, text ='admin no').grid(row=1,column=0)
            num = Entry(maind)
            num.grid(row=1,column=1)
            Button(maind, text='show', command=dis,width=20).grid(row=3,column=1)
            Button(maind, text='back', command=maind.destroy,width=20).grid(row=5,column=1)
            Label(maind, text = "").grid(row=0,column=0)
            for i in range(2,9,2):
                   Label(maind, text = "").grid(row=i,column=2)
      def choice():
             mainc = Tk()
             Label(mainc, text ='SELECT ').grid(row=1,column=1)
             Button(mainc, text='ENTER VALUES', command= main2,width=20).grid(row=3,column=1)
             Button(mainc, text='DISPLAY TABLE', command=main3,width=20).grid(row=5,column=1)
             Label(mainc, text = "").grid(row=0,column=0)
             for i in range(2,9,2):
                   Label(mainc, text = "").grid(row=i,column=2)
      def passw():
          Ans = str(num2.get())
          global a
          a=sq.connect(host='localhost',user='root',passwd=Ans)
          if a.is_connected:
                  print("yes")
          global c
          c=a.cursor()
          Ans1= str(num1.get())
          Ans2=str(num3.get())
          c=a.cursor()
          e=c.execute("create database if not exists "+Ans1+Ans2+"")
          print("yes")
          f=c.execute("use "+Ans1+Ans2+"")
          i=c.execute("create table if not exists student_detail (admin_no int(5) primary key,name varchar(30),date_of_admin char(10),date_of_birth char(10),gender char(1),category  varchar(4),father_name varchar(30),mother_name varchar(30), address varchar(50), phone_no char(11))")
          choice()
      main = Tk()
      Label(main,text="enter class:").grid(row=1,column=0)
      Label(main,text="enter section:").grid(row=3,column=0)
      Label(main, text = "enter password:").grid(row=5,column=0)
      num1 = Entry(main)
      num1.grid(row=1, column=1)
      num3 = Entry(main)
      num3.grid(row=3, column=1)
      num2= Entry(main,show='*')
      num2.grid(row=5, column=1)
      for i in range(0,9,2):
            Label(main, text = "").grid(row=i,column=2)
      Button(main, text='ENTER', command=passw,width=20).grid(row=7, column=1, sticky=W,ipady=5)
      mainloop()

def main3():
      def main2():
            #inserting values into table
            def  insertans():
                        Ans = int(num1.get())
                        Ans1=(num2.get())
                        Ans2=int(num3.get())
                        Ans3=int(num4.get())
                        Ans4=int(num5.get())
                        Ans5=int(num6.get())
                        if cl<6:
                               i="insert into "+q+"(roll_no ,name ,evs,mathematics ,hindi ,english ) values({},'{}',{},{},{},{})".format(Ans,Ans1,Ans2,Ans3,Ans4,Ans5)
                        elif cl>5 :
                              Ans6=int(num7.get())
                              if cl<9:
                                    Ans7=int(num8.get())
                                    i="insert into "+q+"(roll_no ,name ,science,mathematics ,hindi ,english,social_studies,sanskrit ) values({},'{}',{},{},{},{},{},{})".format(Ans,Ans1,Ans2,Ans3,Ans4,Ans5,Ans6,Ans7)                              
                              elif cl<11:
                                    i="insert into "+q+"(roll_no ,name ,science,mathematics ,hindi ,english,social_studies ) values({},'{}',{},{},{},{},{})".format(Ans,Ans1,Ans2,Ans3,Ans4,Ans5,Ans6)                              
                              elif (se=='a'or se== 'b') and cl>10:
                                    i="insert into "+q+"(roll_no ,name ,physics,chemistry,mathematics ,computer_science ,english ) values({},'{}',{},{},{},{},{})".format(Ans,Ans1,Ans2,Ans3,Ans4,Ans5,Ans6)
                              elif se=='c' and cl>10:
                                    Ans7=int(num8.get())
                                    i="insert into "+q+"(roll_no ,name ,physics,chemistry,mathematics ,hindi,english,biology ) values({},'{}',{},{},{},{},{},{})".format(Ans,Ans1,Ans2,Ans3,Ans4,Ans5,Ans6,Ans7)                              
                              elif se=='d' and cl>10:
                                    i="insert into "+q+"(roll_no ,name ,business_studies,accountancy,mathematics ,economics ,english ) values({},'{}',{},{},{},{},{})".format(Ans,Ans1,Ans2,Ans3,Ans4,Ans5,Ans6)
                              elif se=='e' and cl>10:
                                    i="insert into "+q+"(roll_no ,name ,political_science,geography,history ,hindi ,english ) values({},'{}',{},{},{},{},{})".format(Ans,Ans1,Ans2,Ans3,Ans4,Ans5,Ans6)
                        c.execute(i)
                        a.commit()
                        #clearing all entries
                        num1.delete(0, 'end')
                        num2.delete(0, 'end')
                        num3.delete(0, 'end')
                        num4.delete(0, 'end')
                        num5.delete(0, 'end')
                        num6.delete(0, 'end')
                        if cl>5 :
                              num7.delete(0, 'end')
                              if cl<9:
                                    num8.delete(0, 'end')    
                              elif se=='c' and cl>10:
                                    num8.delete(0,'end')
            #entering values 
            mainb = Tk()
            Label(mainb, text = "roll no:").grid(row=0)
            Label(mainb, text = "name:").grid(row=1)
            Label(mainb, text = "Enter the marks scored").grid(row=2,column=1)
            num1 = Entry(mainb)
            num2 = Entry(mainb)
            num1.grid(row=0, column=1)
            num2.grid(row=1, column=1)
            if cl<6:
                  Label(mainb, text = "EVS:").grid(row=3)
                  Label(mainb, text = "mathematics:").grid(row=4)
                  Label(mainb, text = "hindi:").grid(row=5)
                  Label(mainb, text = "english:").grid(row=6)
                  num3 = Entry(mainb)
                  num4=Entry(mainb)
                  num5=Entry(mainb)
                  num6=Entry(mainb)
                  num3.grid(row=3, column=1)
                  num4.grid(row=4, column=1)
                  num5.grid(row=5, column=1)
                  num6.grid(row=6, column=1)
            elif cl>5 and cl<11:
                  Label(mainb, text = "science:").grid(row=3)
                  Label(mainb, text = "mathematics:").grid(row=4)
                  Label(mainb, text = "hindi:").grid(row=5)
                  Label(mainb, text = "english:").grid(row=6)
                  Label(mainb, text = "social st:").grid(row=7)
                  if cl<9:
                        Label(mainb, text = "sanskrit:").grid(row=8)
                        num8=Entry(mainb)
                        num8.grid(row=8,column=1)
                        
                  num3 = Entry(mainb)
                  num4=Entry(mainb)
                  num5=Entry(mainb)
                  num6=Entry(mainb)
                  num7 = Entry(mainb)
                  num3.grid(row=3, column=1)
                  num4.grid(row=4, column=1)
                  num5.grid(row=5, column=1)
                  num6.grid(row=6, column=1)
                  num7.grid(row=7,column=1)
                  
            elif cl>10:
                  if se=='a'or se=='b':
                        
                        Label(mainb, text = "physics:").grid(row=3)
                        Label(mainb, text = "chemistry:").grid(row=4)
                        Label(mainb, text = "mathematics:").grid(row=5)
                        Label(mainb, text = "computer Sc:").grid(row=6)
                        Label(mainb, text = "english:").grid(row=7)
                        num3 = Entry(mainb)
                        num4=Entry(mainb)
                        num5=Entry(mainb)
                        num6=Entry(mainb)
                        num7 = Entry(mainb)
                        num3.grid(row=3, column=1)
                        num4.grid(row=4, column=1)
                        num5.grid(row=5, column=1)
                        num6.grid(row=6, column=1)
                        num7.grid(row=7,column=1)
                  elif se=='c':
                        
                        Label(mainb, text = "physics:").grid(row=3)
                        Label(mainb, text = "chemistry:").grid(row=4)
                        Label(mainb, text = "mathematics:").grid(row=5)
                        Label(mainb, text = "hindi:").grid(row=6)
                        Label(mainb, text = "english:").grid(row=7)
                        Label(mainb, text = "biology:").grid(row=8)
                        num3 = Entry(mainb)
                        num4=Entry(mainb)
                        num5=Entry(mainb)
                        num6=Entry(mainb)
                        num7 = Entry(mainb)
                        num8=Entry(mainb)
                        num3.grid(row=3, column=1)
                        num4.grid(row=4, column=1)
                        num5.grid(row=5, column=1)
                        num6.grid(row=6, column=1)
                        num7.grid(row=7,column=1)
                        num8.grid(row=8,column=1)
                  elif se=='d':
                        
                        Label(mainb, text = "business studies:").grid(row=3)
                        Label(mainb, text = "acountancy:").grid(row=4)
                        Label(mainb, text = "mathematics:").grid(row=5)
                        Label(mainb, text = "economics:").grid(row=6)
                        Label(mainb, text = "english:").grid(row=7)
                        num3 = Entry(mainb)
                        num4=Entry(mainb)
                        num5=Entry(mainb)
                        num6=Entry(mainb)
                        num7 = Entry(mainb)
                        num3.grid(row=3, column=1)
                        num4.grid(row=4, column=1)
                        num5.grid(row=5, column=1)
                        num6.grid(row=6, column=1)
                        num7.grid(row=7,column=1)
                  elif se=='e':
                        
                        Label(mainb, text = "political sc:").grid(row=3)
                        Label(mainb, text = "geography:").grid(row=4)
                        Label(mainb, text = "history:").grid(row=5)
                        Label(mainb, text = "hindi:").grid(row=6)
                        Label(mainb, text = "english:").grid(row=7)
                        num3 = Entry(mainb)
                        num4=Entry(mainb)
                        num5=Entry(mainb)
                        num6=Entry(mainb)
                        num7 = Entry(mainb)
                        num3.grid(row=3, column=1)
                        num4.grid(row=4, column=1)
                        num5.grid(row=5, column=1)
                        num6.grid(row=6, column=1)
                        num7.grid(row=7,column=1)

            Button(mainb, text='Quit', command=mainb.destroy,width=12).grid(row=9, column=0, sticky=W, pady=4)
            Button(mainb, text='enter', command=insertans,width=12).grid(row=9, column=1, sticky=W, pady=4)

            mainloop()
      def  main3():
            def dis():
                  print(num1)
                  rf=int(num1.get())
                  ad=()
                  led=len(data)-1
                  print(data)
                  for x in range(rf):
                        if x <=led:
                              ad=data[x]
                              print(ad)
                        else:
                              ad=()
                              break
                  print(ad)
                  if ad!=():
                        maine= Tk()
                        Label(maine, text = "name:").grid(row=1)
                        Label(maine, text = " the marks scored by the student").grid(row=2,column=1)
                        num2 = Entry(maine)
                        num2.grid(row=1, column=1)
                        num2.insert(0,ad[1])
                        if cl<6:
                              Label(maine, text = "EVS:").grid(row=3)
                              Label(maine, text = "mathematics:").grid(row=4)
                              Label(maine, text = "hindi:").grid(row=5)
                              Label(maine, text = "english:").grid(row=6)
                              num3 = Entry(maine)
                              num4=Entry(maine)
                              num5=Entry(maine)
                              num6=Entry(maine)
                              num3.grid(row=3, column=1)
                              num4.grid(row=4, column=1)
                              num5.grid(row=5, column=1)
                              num6.grid(row=6, column=1)
                              num3.insert(0,ad[2])
                              num4.insert(0,ad[3])
                              num5.insert(0,ad[4])
                              num6.insert(0,ad[5])
                        elif cl>5 and cl<11:
                              Label(maine, text = "science:").grid(row=3)
                              Label(maine, text = "mathematics:").grid(row=4)
                              Label(maine, text = "hindi:").grid(row=5)
                              Label(maine, text = "english:").grid(row=6)
                              Label(maine, text = "social st:").grid(row=7)
                              if cl<9:
                                    Label(maine, text = "sanskrit:").grid(row=8)
                                    num8=Entry(maine)
                                    num8.grid(row=8,column=1)
                                    num8.insert(0,ad[7])
                              num3 = Entry(maine)
                              num4=Entry(maine)
                              num5=Entry(maine)
                              num6=Entry(maine)
                              num7 = Entry(maine)
                              num3.grid(row=3, column=1)
                              num4.grid(row=4, column=1)
                              num5.grid(row=5, column=1)
                              num6.grid(row=6, column=1)
                              num7.grid(row=7,column=1)
                              num3.insert(0,ad[2])
                              num4.insert(0,ad[3])
                              num5.insert(0,ad[4])
                              num6.insert(0,ad[5])
                              num7.insert(0,ad[6])
                        elif cl>10:
                              if se=='a'or se=='b':
                                    
                                    Label(maine, text = "physics:").grid(row=3)
                                    Label(maine, text = "chemistry:").grid(row=4)
                                    Label(maine, text = "mathematics:").grid(row=5)
                                    Label(maine, text = "computer Sc:").grid(row=6)
                                    Label(maine, text = "english:").grid(row=7)
                                    num3 = Entry(maine)
                                    num4=Entry(maine)
                                    num5=Entry(maine)
                                    num6=Entry(maine)
                                    num7 = Entry(maine)
                                    num3.grid(row=3, column=1)
                                    num4.grid(row=4, column=1)
                                    num5.grid(row=5, column=1)
                                    num6.grid(row=6, column=1)
                                    num7.grid(row=7,column=1)
                                    num3.insert(0,ad[2])
                                    num4.insert(0,ad[3])
                                    num5.insert(0,ad[4])
                                    num6.insert(0,ad[5])
                                    num7.insert(0,ad[6])    
                              elif se=='c':
                                    
                                    Label(maine, text = "physics:").grid(row=3)
                                    Label(maine, text = "chemistry:").grid(row=4)
                                    Label(maine, text = "mathematics:").grid(row=5)
                                    Label(maine, text = "hindi:").grid(row=6)
                                    Label(maine, text = "english:").grid(row=7)
                                    Label(maine, text = "biology:").grid(row=8)
                                    num3 = Entry(maine)
                                    num4=Entry(maine)
                                    num5=Entry(maine)
                                    num6=Entry(maine)
                                    num7 = Entry(maine)
                                    num8=Entry(maine)
                                    num3.grid(row=3, column=1)
                                    num4.grid(row=4, column=1)
                                    num5.grid(row=5, column=1)
                                    num6.grid(row=6, column=1)
                                    num7.grid(row=7,column=1)
                                    num8.grid(row=8,column=1)
                                    num3.insert(0,ad[2])
                                    num4.insert(0,ad[3])
                                    num5.insert(0,ad[4])
                                    num6.insert(0,ad[5])
                                    num7.insert(0,ad[6])
                                    num8.insert(0,ad[7])
                              elif se=='d':
                                    
                                    Label(maine, text = "business studies:").grid(row=3)
                                    Label(maine, text = "acountancy:").grid(row=4)
                                    Label(maine, text = "mathematics:").grid(row=5)
                                    Label(maine, text = "economics:").grid(row=6)
                                    Label(maine, text = "english:").grid(row=7)
                                    num3 = Entry(maine)
                                    num4=Entry(maine)
                                    num5=Entry(maine)
                                    num6=Entry(maine)
                                    num7 = Entry(maine)
                                    num3.grid(row=3, column=1)
                                    num4.grid(row=4, column=1)
                                    num5.grid(row=5, column=1)
                                    num6.grid(row=6, column=1)
                                    num7.grid(row=7,column=1)
                                    num3.insert(0,ad[2])
                                    num4.insert(0,ad[3])
                                    num5.insert(0,ad[4])
                                    num6.insert(0,ad[5])
                                    num7.insert(0,ad[6])
                              elif se=='e':
                                    
                                    Label(maine, text = "political sc:").grid(row=3)
                                    Label(maine, text = "geography:").grid(row=4)
                                    Label(maine, text = "history:").grid(row=5)
                                    Label(maine, text = "hindi:").grid(row=6)
                                    Label(maine, text = "english:").grid(row=7)
                                    num3 = Entry(maine)
                                    num4=Entry(maine)
                                    num5=Entry(maine)
                                    num6=Entry(maine)
                                    num7 = Entry(maine)
                                    num3.grid(row=3, column=1)
                                    num4.grid(row=4, column=1)
                                    num5.grid(row=5, column=1)
                                    num6.grid(row=6, column=1)
                                    num7.grid(row=7,column=1)
                                    num3.insert(0,ad[2])
                                    num4.insert(0,ad[3])
                                    num5.insert(0,ad[4])
                                    num6.insert(0,ad[5])
                                    num7.insert(0,ad[6])
                  else:
                        maine= Tk()
                        Label(maine, text = "no entry found!!!!!!!",width=15,height=5).grid(row=1)
                        Button(maine, text='back', command=maine.destroy,width=20).grid(row=10,column=1)
                        
                  
                              
            i='select * from '+q                              
            c.execute(i )
            data=list(c.fetchall())
            maind = Tk()
            Label(maind, text ='rollno').grid(row=1,column=0)
            num1 = Entry(maind)
            num1.grid(row=1,column=1)
            Button(maind, text='show', command=dis,width=20).grid(row=3,column=1)
            Button(maind, text='back', command=maind.destroy,width=20).grid(row=5,column=1)
            Label(maind, text = "").grid(row=0,column=0)
            for i in range(2,9,2):
                   Label(maind, text = "").grid(row=i,column=2)
      def choice():
             mainc = Tk()
             Label(mainc, text = "SELECT").grid(row=1,column=1)
             Button(mainc, text='ENTER VALUES', command= main2,width=20).grid(row=3,column=1)
             Button(mainc, text='DISPLAY TABLE', command=main3,width=20).grid(row=5,column=1)
             Label(mainc, text = "").grid(row=0,column=0)
             for i in range(2,7,2):
                   Label(mainc, text = "").grid(row=i,column=2)
             
      #entering class and exam name     
      def main1():
            #creating and using database /creating table
            def data():
                  print(num1)
                  Ans7 = str(num1.get())
                  Ans8=str(num2.get())
                  Ans9=str(num3.get())
                  c=a.cursor()
                  ei="create database if not exists "+Ans7+Ans8+""
                  e=c.execute(ei)
                  print("yes")
                  fi="use "+Ans7+Ans8+""
                  f=c.execute(fi)
                  global q
                  q=Ans9
                  global cl
                  cl=int(Ans7)
                  global se
                  se=Ans8
                  if cl<6: 
                        ii="create table if not exists "+Ans9+"(roll_no int(3) primary key,name varchar(30),evs int(3),mathematics int(3),hindi int(3),english int(3))"
                  elif cl>5 and cl<11:
                              if cl<9:
                                    ii="create table if not exists "+Ans9+"(roll_no int(3) primary key,name varchar(30),science int(3),mathematics  int(3),hindi  int(3),english int(3),social_studies int(3),sanskrit int(3) ) "
                              elif cl<11:
                                    ii="create table if not exists "+Ans9+"(roll_no int(3) primary key,name varchar(30),science int(3),mathematics  int(3),hindi  int(3),english int(3),social_studies int(3)) "
                  elif cl>10:
                        if (se=='a'or se== 'b') :
                              ii="create table if not exists "+Ans9+"(roll_no int(3) primary key,name varchar(30),physics int(3),chemistry  int(3),mathematics  int(3),computer_science int(3),english int(3) ) "
                        elif se=='c' :
                              ii="create table if not exists "+Ans9+"(roll_no int(3) primary key,name varchar(30),physics int(3),chemistry  int(3),mathematics  int(3),hindi int(3),english int(3),biology int(3) ) "
                        elif se=='d':
                              ii="create table if not exists "+Ans9+"(roll_no int(3) primary key,name varchar(30),business_studies int(3),accountancy  int(3),mathematics  int(3),economics int(3),english int(3) ) "
                        elif se=='e':
                              ii="create table if not exists "+Ans9+"(roll_no int(3) primary key,name varchar(30),political_science int(3),geography  int(3),history  int(3),hindi int(3),english int(3) ) "
                  i=c.execute(ii)
                  z=choice()                  
            maina=Tk()
            Label(maina,text="enter class").grid(row=1,column=0)
            Label(maina,text="enter section").grid(row=3,column=0)
            Label(maina,text="enter test").grid(row=5,column=0)
            num1 = Entry(maina)
            num2 = Entry(maina)
            num3 = Entry(maina)
            num1.grid(row=1, column=1)
            num2.grid(row=3, column=1)
            num3.grid(row=5,column=1)
            Button(maina,text='enter',command=data,width=20 ).grid(row=7,column=1)
            for i in range(0,9,2):
                  Label(maina, text = "").grid(row=i,column=2)
       #connecting to mysql database
      def passw():
                Ans = str(num1.get())
                global a
                a=sq.connect(host='localhost',user='root',passwd=Ans)
                if a.is_connected:
                        print("yes")
                global c
                c=a.cursor()
                main1()
      #entry for password of mysql database
      main = Tk()
      Label(main, text = "enter password:").grid(row=1)
      num1 = Entry(main,show='*')
      num1.grid(row=1, column=1)
      Button(main, text='ENTER', command= passw,width=20).grid(row=3, column=1, sticky=W, pady=5)
      for i in range(0,4,2):
            Label(main, text = "").grid(row=i,column=2)
      mainloop()
                  
co=Tk()
Label(co,text='SELECT ').grid(row=0,column=1)
for i in range(1,8,2):
      Label(co,text='').grid(row=i)
Button(co, text='employee', command=main1,width=20).grid(row=2, column=1,sticky=W)
Button(co, text='student details', command=main2,width=20).grid(row=4, column=1, sticky=W)
Button(co, text='student marks', command=main3,width=20).grid(row=6, column=1, sticky=W)
Label(co,text='').grid(row=3,column=2)
mainloop()
