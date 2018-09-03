from tkinter import *
from sqlite3 import *
import time
from tkinter import messagebox as ms
import random

localtime=time.asctime(time.localtime(time.time()))

class Log:
    
    def login(sf):
        try:
            sf.scr1.destroy()
        except:
            pass
        
        sf.scr=Tk()
        sf.scr.geometry("1600x800+0+0")
        sf.scr.title("Pizza Management system")
        sf.scr.config(bg='#DE5135')

        sf.Tops = Frame(sf.scr,width=1600,height=50,relief="sunken",bg='#DE5135')
        sf.Tops.pack(side=TOP)

        sf.f1=Frame(sf.scr,width=500,height=700,relief="sunken",bg='#DE5135')
        sf.f1.pack(side=LEFT)
        sf.f2=Frame(sf.scr,width=550,height=700,relief="sunken",bg='#DE5135').place(x=500,y=200)

        sf.f3=Frame(sf.scr,width=500,height=700,relief="sunken")
        sf.f3.pack(side=RIGHT)
        sf.l1=Label(sf.Tops,font=('Edwardian Script ITC',50,'bold'),text="Pizza Management System",
                    fg='black',bd=10,anchor='w',bg='#DE5135')
        sf.l1.grid(row=0,column=0)
        sf.l2=Label(sf.Tops,font=('arial',20,'bold'),text=localtime,fg="black",
                    bd=10,anchor='w',bg='#DE5135')
        sf.l2.grid(row=1,column=0)

        sf.img1 = PhotoImage(file="d:/Disk d/Python/pizza management system/1.png")
        #sf.img2 = PhotoImage(file="d:/Disk d/Python/pizza management system/2.png")
        sf.l3=Label(sf.f1,image=sf.img1,bg='#DE5135')
        sf.l3.grid(row=0,column=0)
        sf.l4=Label(sf.f3,image=sf.img1,bg='#DE5135')
        sf.l4.grid(row=0,column=0)
        sf.l5=Label(sf.f2,font=('arial',30,'bold','underline'),text="Login Page",
                    fg="white",bd=10,anchor='w',bg='#DE5135')
        sf.l5.place(x=570,y=300)
        sf.l6=Label(sf.f2,font=('arial',20,'bold'),text="User name :",fg="black",
                    bd=10,anchor='w',bg='#DE5135')
        sf.l6.place(x=570,y=400)
        sf.l7=Label(sf.f2,font=('arial',20,'bold'),text="Password :",
                    fg="black",bd=10,anchor='w',bg='#DE5135')
        sf.l7.place(x=570,y=450)
        sf.username=StringVar()
        sf.password=StringVar()
        sf.user1=Entry(sf.f2,bg="white",textvariable=sf.username,font=('arial',20,'bold'),
                      insertwidth=4,bd=7)
        sf.user1.place(x=750,y=410)
        sf.pasd1=Entry(sf.f2,bg="white",textvariable=sf.password,font=('arial',20,'bold'),
                          insertwidth=4,bd=7,show="*")
        sf.pasd1.place(x=750,y=460)
        
        sf.regi1=Button(sf.f2,padx=10,pady=10,bd=8,text="Register",font=('arial',20,'bold'),
                           fg="white",bg="#2C272E",command=sf.register)
        sf.regi1.place(x=570,y=600)
        sf.log1=Button(sf.f2,padx=10,pady=10,bd=8,text="Login",font=('arial',20,'bold'),
                        fg="white",bg="#2C272E",command =sf.login1)
        sf.log1.place(x=750,y=600)
        sf.scr.mainloop()

    def register(sf):
        try:
            sf.scr.destroy()
        except:
            pass
        sf.scr1=Tk()
        sf.scr1.geometry("1600x800+0+0")
        sf.scr1.title("Pizza Management system")
        sf.scr1.config(bg='#C42B32')

        sf.Tops = Frame(sf.scr1,width=1600,height=50,relief="sunken",bg='#C42B32')
        sf.Tops.pack(side=TOP)

        sf.f1=Frame(sf.scr1,width=500,height=700,relief="sunken")
        sf.f1.pack(side=LEFT)
        sf.f2=Frame(sf.scr1,width=550,height=700,relief="sunken",bg='#C42B32').place(x=500,y=200)

        sf.f3=Frame(sf.scr1,width=500,height=700,relief="sunken")
        sf.f3.pack(side=RIGHT)
        sf.l1=Label(sf.Tops,font=('Edwardian Script ITC',50,'bold'),text="Pizza Management System",
                    fg='black',bd=10,anchor='w',bg='#C42B32')
        sf.l1.grid(row=0,column=0)
        sf.l2=Label(sf.Tops,font=('arial',20,'bold'),text=localtime,fg="black",
                    bd=10,anchor='w',bg='#C42B32')
        sf.l2.grid(row=1,column=0)

        sf.img1 = PhotoImage(file="d:/Disk d/Python/pizza management system/3.png")
        #sf.img2 = PhotoImage(file="d:/Disk d/Python/pizza management system/4.png")
        sf.l3=Label(sf.f1,image=sf.img1,bg='#C42B32')
        sf.l3.grid(row=0,column=0)
        sf.l4=Label(sf.f3,image=sf.img1,bg='#C42B32')
        sf.l4.grid(row=0,column=0)
        sf.l5=Label(sf.f2,font=('arial',30,'bold','underline'),text="Register Page",
                    fg="white",bd=10,anchor='w',bg='#C42B32').place(x=570,y=300)
        sf.l6=Label(sf.f2,font=('arial',20,'bold'),text="User name :",fg="black",
                    bd=10,anchor='w',bg='#C42B32').place(x=570,y=400)
        sf.l7=Label(sf.f2,font=('arial',20,'bold'),text="Password :",
                    fg="black",bd=10,anchor='w',bg='#C42B32').place(x=570,y=450)
        sf.username1=StringVar()
        sf.password1=StringVar()
        sf.user2=Entry(sf.f2,bg="white",textvariable=sf.username1,font=('arial',20,'bold'),
                      insertwidth=4,bd=7)
        sf.user2.place(x=750,y=410)
        sf.pasd2=Entry(sf.f2,bg="white",textvariable=sf.password1,font=('arial',20,'bold'),
                          insertwidth=4,bd=7,show="*")
        sf.pasd2.place(x=750,y=460)
        sf.back=Button(sf.f2,padx=10,pady=10,bd=8,text="Back",font=('arial',20,'bold'),
                           fg="white",bg="#2C272E",command=sf.login).place(x=570,y=600)
        sf.regi2=Button(sf.f2,padx=10,pady=10,bd=8,text="Register",font=('arial',20,'bold'),
                        fg="white",bg="#2C272E",command=sf.register1).place(x=750,y=600)

        
        sf.scr1.mainloop()

    def login1(sf):
        try:
            sf.scr.destroy()
        except:
            pass
        sf.con=connect("d:/Disk d/Python/pizza management system/pizza.db")
        sf.cur=sf.con.cursor()
        
        sf.cur.execute("create table IF NOT EXISTS employe (user varchar(50) ,password varchar(50))")
        if sf.username.get()=="" or sf.password.get()=="":
            scrm=Tk()
            ms.showwarning("Information","Enter The valid Username and Password")
            scrm.destroy()
            sf.login()
        else:
            sf.cur.execute("SELECT * FROM employe WHERE user = ? AND password = ?",
                           (sf.username.get(), sf.password.get()))
            if sf.cur.fetchone() is not None:
                sf.username.set("")
                sf.password.set("")
                sf.main()
            else:
                sf.username.set("")
                sf.password.set("")
                scrm=Tk()
                ms.showinfo("Information","Enter The valid Username and Password!")
                scrm.destroy()
                sf.login()
                

    def register1(sf):
        try:
            sf.scr1.destroy()
        except:
            pass
        sf.con=connect("d:/Disk d/Python/pizza management system/pizza.db")
        sf.cur=sf.con.cursor()
        
        sf.cur.execute("create table IF NOT EXISTS employe (user varchar(50) ,password varchar(50))")
        if sf.username1.get()=="" or sf.password1.get()=="":
            scrm=Tk()    
            ms.showinfo("Information","Enter The valid Username and Password")
            scrm.destroy()
            sf.register()
        else:
            sf.cur.execute("SELECT * FROM employe WHERE user = ? AND password = ?",
                           (sf.username1.get(), sf.password1.get()))
            if sf.cur.fetchone() is not None:
                scrm=Tk() 
                ms.showinfo("Information","Username already taken")
                scrm.destroy()
                sf.username1.set("")
                sf.password1.set("")
                sf.register()
                
            else:
                sf.cur.execute("insert into employe values(%r,%r)"%(sf.username1.get(),sf.password1.get()))
                sf.username1.set("")
                sf.password1.set("")
                sf.con.commit()
                scrm=Tk() 
                ms.showinfo("Information","You Successfully Registered")
                scrm.destroy()
                sf.register()
                

    def clear(sf):
        sf.username1.set("")
        sf.password.set("")
    
    def main(sf):
        try:
            sf.scr.destroy()
        except:
            pass
        sf.scr2=Tk()
        sf.scr2.geometry("1600x800+0+0")
        sf.scr2.title("Pizza Management system")
        sf.scr2.config(bg='#6189A8')

        sf.Tops = Frame(sf.scr2,width=1600,height=50,relief="sunken",bg='#6189A8')
        sf.Tops.pack(side=TOP)

        sf.f1=Frame(sf.scr2,width=1000,height=700,relief="sunken",bg='#6189A8')
        sf.f1.pack(side=LEFT)
        sf.f2=Frame(sf.scr2,width=600,height=700,relief="sunken",bg='#6189A8')
        sf.f2.pack(side=RIGHT)
        sf.l1=Label(sf.Tops,font=('Edwardian Script ITC',50,'bold'),text="Pizza Management System",
                    fg='black',bd=10,anchor='w',bg='#6189A8')
        sf.l1.grid(row=0,column=0)
        sf.l2=Label(sf.Tops,font=('arial',20,'bold'),text=localtime,fg="black",
                    bd=10,anchor='w',bg='#6189A8')
        sf.l2.grid(row=1,column=0)

        #====================================================================================================
        sf.mar=StringVar()
        sf.cheese_mar=StringVar()
        sf.farm=StringVar()
        sf.peppy=StringVar()
        sf.greenwave=StringVar()
        sf.deluxeveggie=StringVar()
        sf.cheesecorn=StringVar()
        sf.bar=StringVar()
        sf.tikka=StringVar()
        sf.sausage=StringVar()
        sf.supreme=StringVar()
        sf.dominator=StringVar()
        sf.fiesta=StringVar()
        sf.peri=StringVar()
        sf.capsicum=StringVar()
        sf.onion=StringVar()
        sf.paneer=StringVar()
        sf.loaded=StringVar()
        sf.goldencorn=StringVar()
        sf.cocacola=StringVar()
        sf.pepsi=StringVar()
        sf.reference=StringVar()
        sf.costmeal=StringVar()
        sf.service=StringVar()
        sf.state=StringVar()
        sf.subtotal=StringVar()
        sf.totalcost=StringVar()
        option=(1,2,3,4,5,6,7,8,9,10)
        #====================================================================================================
        
        sf.vezpizzas=Label(sf.f1,font=('arial',16,'bold','underline','italic'),text="VEZ PIZZAS",
                           bd=10,anchor='w',bg='#6189A8')
        sf.vezpizzas.grid(row=0,column=0)
        sf.price=Label(sf.f1,font=('arial',16,'bold','underline','italic'),text="PRICE(Rs)",
                           bd=10,anchor='w',bg='#6189A8')
        sf.price.grid(row=0,column=1)
        sf.quantity=Label(sf.f1,font=('arial',16,'bold','underline','italic'),text="QUANTITY",
                           bd=10,anchor='w',bg='#6189A8')
        sf.quantity.grid(row=0,column=2)
        
        sf.mar1=Label(sf.f1,font=('arial',16,'bold'),text="MARGHERITA :",bd=10,anchor='w',bg='#6189A8')
        sf.mar1.grid(row=1,column=0)
        sf.mar1=Label(sf.f1,font=('arial',16,'bold'),text="195",
                           bd=10,anchor='w',bg='#6189A8')
        sf.mar1.grid(row=1,column=1)
        sf.mar_ot=OptionMenu(sf.f1,sf.mar,*option)
        sf.mar.set(0)
        sf.mar_ot.config(width=10)
        sf.mar_ot.grid(row=1,column=2)
        
        sf.cheesemar1=Label(sf.f1,font=('arial',16,'bold'),text="CHEESE MARGHERITA :",bd=10,anchor='w',bg='#6189A8')
        sf.cheesemar1.grid(row=2,column=0)
        sf.cheesemar1=Label(sf.f1,font=('arial',16,'bold'),text="180",
                           bd=10,anchor='w',bg='#6189A8')
        sf.cheesemar1.grid(row=2,column=1)
        sf.cheese_mar_ot=OptionMenu(sf.f1,sf.cheese_mar,*option)
        sf.cheese_mar.set(0)
        sf.cheese_mar_ot.config(width=10)
        sf.cheese_mar_ot.grid(row=2,column=2)
        
        sf.farm1=Label(sf.f1,font=('arial',16,'bold'),text="FARM HOUSE :",bd=10,anchor='w',bg='#6189A8')
        sf.farm1.grid(row=3,column=0)
        sf.farm1=Label(sf.f1,font=('arial',16,'bold'),text="210",
                           bd=10,anchor='w',bg='#6189A8')
        sf.farm1.grid(row=3,column=1)
        sf.farm_ot=OptionMenu(sf.f1,sf.farm,*option)
        sf.farm.set(0)
        sf.farm_ot.config(width=10)
        sf.farm_ot.grid(row=3,column=2)
        
        sf.peppy1=Label(sf.f1,font=('arial',16,'bold'),text="PEPPY PANEER :",bd=10,anchor='w',bg='#6189A8')
        sf.peppy1.grid(row=4,column=0)
        sf.peppy1=Label(sf.f1,font=('arial',16,'bold'),text="300",
                           bd=10,anchor='w',bg='#6189A8')
        sf.peppy1.grid(row=4,column=1)
        sf.peppy_ot=OptionMenu(sf.f1,sf.peppy,*option)
        sf.peppy.set(0)
        sf.peppy_ot.config(width=10)
        sf.peppy_ot.grid(row=4,column=2)
        
        sf.greenwave1=Label(sf.f1,font=('arial',16,'bold'),text="GREEN WAVE :",bd=10,anchor='w',bg='#6189A8')
        sf.greenwave1.grid(row=5,column=0)
        sf.greenwave1=Label(sf.f1,font=('arial',16,'bold'),text="400",
                           bd=10,anchor='w',bg='#6189A8')
        sf.greenwave1.grid(row=5,column=1)
        sf.greenwave_ot=OptionMenu(sf.f1,sf.greenwave,*option)
        sf.greenwave.set(0)
        sf.greenwave_ot.config(width=10)
        sf.greenwave_ot.grid(row=5,column=2)
        
        sf.deluxeveggie1=Label(sf.f1,font=('arial',16,'bold'),text="DELUXE VEGGIE :",bd=10,anchor='w',bg='#6189A8')
        sf.deluxeveggie1.grid(row=6,column=0)
        sf.deluxeveggie1=Label(sf.f1,font=('arial',16,'bold'),text="450",
                           bd=10,anchor='w',bg='#6189A8')
        sf.deluxeveggie1.grid(row=6,column=1)
        sf.deluxeveggie_ot=OptionMenu(sf.f1,sf.deluxeveggie,*option)
        sf.deluxeveggie.set(0)
        sf.deluxeveggie_ot.config(width=10)
        sf.deluxeveggie_ot.grid(row=6,column=2)
        
        sf.cheesecorn1=Label(sf.f1,font=('arial',16,'bold'),text="CHEESE N CORN :",bd=10,anchor='w',bg='#6189A8')
        sf.cheesecorn1.grid(row=7,column=0)
        sf.cheesecorn1=Label(sf.f1,font=('arial',16,'bold'),text="350",
                           bd=10,anchor='w',bg='#6189A8')
        sf.cheesecorn1.grid(row=7,column=1)
        sf.cheesecorn_ot=OptionMenu(sf.f1,sf.cheesecorn,*option)
        sf.cheesecorn.set(0)
        sf.cheesecorn_ot.config(width=10)
        sf.cheesecorn_ot.grid(row=7,column=2)
        
        sf.vezpizzas=Label(sf.f1,font=('arial',16,'bold','underline','italic'),text="NONVEZ PIZZAS",bd=10,anchor='w',bg='#6189A8')
        sf.vezpizzas.grid(row=8,column=0)
        
        sf.bar1=Label(sf.f1,font=('arial',16,'bold'),text="BARBECUE CHICKEN :",bd=10,anchor='w',bg='#6189A8')
        sf.bar1.grid(row=9,column=0)
        sf.bar1=Label(sf.f1,font=('arial',16,'bold'),text="250",
                           bd=10,anchor='w',bg='#6189A8')
        sf.bar1.grid(row=9,column=1)
        sf.bar_ot=OptionMenu(sf.f1,sf.bar,*option)
        sf.bar.set(0)
        sf.bar_ot.config(width=10)
        sf.bar_ot.grid(row=9,column=2)
        
        sf.tikka1=Label(sf.f1,font=('arial',16,'bold'),text="CHICKEN TIKKA :",bd=10,anchor='w',bg='#6189A8')
        sf.tikka1.grid(row=10,column=0)
        sf.tikka1=Label(sf.f1,font=('arial',16,'bold'),text="450",
                           bd=10,anchor='w',bg='#6189A8')
        sf.tikka1.grid(row=10,column=1)
        sf.tikka_ot=OptionMenu(sf.f1,sf.tikka,*option)
        sf.tikka.set(0)
        sf.tikka_ot.config(width=10)
        sf.tikka_ot.grid(row=10,column=2)
        
        sf.sausage1=Label(sf.f1,font=('arial',16,'bold'),text="CHICKEN SAUSAGE :",bd=10,anchor='w',bg='#6189A8')
        sf.sausage1.grid(row=11,column=0)
        sf.sausage1=Label(sf.f1,font=('arial',16,'bold'),text="500",
                           bd=10,anchor='w',bg='#6189A8')
        sf.sausage1.grid(row=11,column=1)
        sf.sausage_ot=OptionMenu(sf.f1,sf.sausage,*option)
        sf.sausage.set(0)
        sf.sausage_ot.config(width=10)
        sf.sausage_ot.grid(row=11,column=2)

        sf.supreme1=Label(sf.f1,font=('arial',16,'bold'),text="NON VEG SUPREME :",bd=10,anchor='w',bg='#6189A8')
        sf.supreme1.grid(row=12,column=0)
        sf.supreme1=Label(sf.f1,font=('arial',16,'bold'),text="450",
                           bd=10,anchor='w',bg='#6189A8')
        sf.supreme1.grid(row=12,column=1)
        sf.supreme_ot=OptionMenu(sf.f1,sf.supreme,*option)
        sf.supreme.set(0)
        sf.supreme_ot.config(width=10)
        sf.supreme_ot.grid(row=12,column=2)
        #====================================================================================================
        sf.price=Label(sf.f1,font=('arial',16,'bold','underline','italic'),text="PRICE(Rs)",
                           bd=10,anchor='w',bg='#6189A8')
        sf.price.grid(row=0,column=4)
        sf.quantity=Label(sf.f1,font=('arial',16,'bold','underline','italic'),text="QUANTITY",
                           bd=10,anchor='w',bg='#6189A8')
        sf.quantity.grid(row=0,column=5)
        
        sf.dominator1=Label(sf.f1,font=('arial',16,'bold'),text="CHICKEN DOMINATOR :",bd=10,anchor='w',bg='#6189A8')
        sf.dominator1.grid(row=1,column=3)
        sf.dominator1=Label(sf.f1,font=('arial',16,'bold'),text="350",
                           bd=10,anchor='w',bg='#6189A8')
        sf.dominator1.grid(row=1,column=4)
        sf.dominator_ot=OptionMenu(sf.f1,sf.dominator,*option)
        sf.dominator.set(0)
        sf.dominator_ot.config(width=10)
        sf.dominator_ot.grid(row=1,column=5)
        
        sf.fiesta1=Label(sf.f1,font=('arial',16,'bold'),text="CHICKEN FIESTA :",bd=10,anchor='w',bg='#6189A8')
        sf.fiesta1.grid(row=2,column=3)
        sf.fiesta1=Label(sf.f1,font=('arial',16,'bold'),text="450",
                           bd=10,anchor='w',bg='#6189A8')
        sf.fiesta1.grid(row=2,column=4)
        sf.fiesta_ot=OptionMenu(sf.f1,sf.fiesta,*option)
        sf.fiesta.set(0)
        sf.fiesta_ot.config(width=10)
        sf.fiesta_ot.grid(row=2,column=5)
        
        sf.peri1=Label(sf.f1,font=('arial',16,'bold'),text="PERI-PERI CHICKEN :",bd=10,anchor='w',bg='#6189A8')
        sf.peri1.grid(row=3,column=3)
        sf.peri1=Label(sf.f1,font=('arial',16,'bold'),text="600",
                           bd=10,anchor='w',bg='#6189A8')
        sf.peri1.grid(row=3,column=4)
        sf.peri_ot=OptionMenu(sf.f1,sf.peri,*option)
        sf.peri.set(0)
        sf.peri_ot.config(width=10)
        sf.peri_ot.grid(row=3,column=5)

        sf.pizzamenia=Label(sf.f1,font=('arial',16,'bold','underline','italic'),text="PIZZA MENIA",bd=10,anchor='w',bg='#6189A8')
        sf.pizzamenia.grid(row=4,column=3)
        
        sf.capsicum1=Label(sf.f1,font=('arial',16,'bold'),text="CAPSICUM :",bd=10,anchor='w',bg='#6189A8')
        sf.capsicum1.grid(row=5,column=3)
        sf.capsicum1=Label(sf.f1,font=('arial',16,'bold'),text="80",
                           bd=10,anchor='w',bg='#6189A8')
        sf.capsicum1.grid(row=5,column=4)
        sf.capsicum_ot=OptionMenu(sf.f1,sf.capsicum,*option)
        sf.capsicum.set(0)
        sf.capsicum_ot.config(width=10)
        sf.capsicum_ot.grid(row=5,column=5)

        sf.onion1=Label(sf.f1,font=('arial',16,'bold'),text="ONION :",bd=10,anchor='w',bg='#6189A8')
        sf.onion1.grid(row=6,column=3)
        sf.onion1=Label(sf.f1,font=('arial',16,'bold'),text="60",
                           bd=10,anchor='w',bg='#6189A8')
        sf.onion1.grid(row=6,column=4)
        sf.onion_ot=OptionMenu(sf.f1,sf.onion,*option)
        sf.onion.set(0)
        sf.onion_ot.config(width=10)
        sf.onion_ot.grid(row=6,column=5)

        sf.paneer1=Label(sf.f1,font=('arial',16,'bold'),text="PANEER & ONION :",bd=10,anchor='w',bg='#6189A8')
        sf.paneer1.grid(row=7,column=3)
        sf.paneer1=Label(sf.f1,font=('arial',16,'bold'),text="110",
                           bd=10,anchor='w',bg='#6189A8')
        sf.paneer1.grid(row=7,column=4)
        sf.paneer_ot=OptionMenu(sf.f1,sf.paneer,*option)
        sf.paneer.set(0)
        sf.paneer_ot.config(width=10)
        sf.paneer_ot.grid(row=7,column=5)
        
        sf.loaded1=Label(sf.f1,font=('arial',16,'bold'),text="VEG LOADED :",bd=10,anchor='w',bg='#6189A8')
        sf.loaded1.grid(row=8,column=3)
        sf.loaded1=Label(sf.f1,font=('arial',16,'bold'),text="115",
                           bd=10,anchor='w',bg='#6189A8')
        sf.loaded1.grid(row=8,column=4)
        sf.loaded_ot=OptionMenu(sf.f1,sf.loaded,*option)
        sf.loaded.set(0)
        sf.loaded_ot.config(width=10)
        sf.loaded_ot.grid(row=8,column=5)

        sf.goldencorn1=Label(sf.f1,font=('arial',16,'bold'),text="GOLDEN CORN :",bd=10,anchor='w',bg='#6189A8')
        sf.goldencorn1.grid(row=9,column=3)
        sf.goldencorn1=Label(sf.f1,font=('arial',16,'bold'),text="120",
                           bd=10,anchor='w',bg='#6189A8')
        sf.goldencorn1.grid(row=9,column=4)
        sf.goldencorn_ot=OptionMenu(sf.f1,sf.goldencorn,*option)
        sf.goldencorn.set(0)
        sf.goldencorn_ot.config(width=10)
        sf.goldencorn_ot.grid(row=9,column=5)

        sf.drinks=Label(sf.f1,font=('arial',16,'bold','underline','italic'),text="DRINKS",bd=10,anchor='w',bg='#6189A8')
        sf.drinks.grid(row=10,column=3)
        
        sf.cocacola1=Label(sf.f1,font=('arial',16,'bold'),text="COCACOLA :",bd=10,anchor='w',bg='#6189A8')
        sf.cocacola1.grid(row=11,column=3)
        sf.cocacola1=Label(sf.f1,font=('arial',16,'bold'),text="70",
                           bd=10,anchor='w',bg='#6189A8')
        sf.cocacola1.grid(row=11,column=4)
        sf.cocacola_ot=OptionMenu(sf.f1,sf.cocacola,*option)
        sf.cocacola.set(0)
        sf.cocacola_ot.config(width=10)
        sf.cocacola_ot.grid(row=11,column=5)

        sf.pepsi1=Label(sf.f1,font=('arial',16,'bold'),text="PEPSI :",bd=10,anchor='w',bg='#6189A8')
        sf.pepsi1.grid(row=12,column=3)
        sf.pepsi1=Label(sf.f1,font=('arial',16,'bold'),text="50",
                           bd=10,anchor='w',bg='#6189A8')
        sf.pepsi1.grid(row=12,column=4)
        sf.pepsi_ot=OptionMenu(sf.f1,sf.pepsi,*option)
        sf.pepsi.set(0)
        sf.pepsi_ot.config(width=10)
        sf.pepsi_ot.grid(row=12,column=5)
        #====================================================================================================
        sf.bill=Label(sf.f1,font=('arial',18,'bold','underline','italic'),text="BILL COUNTER",bd=10,anchor='w',bg='#6189A8')
        sf.bill.grid(row=0,column=6)
        
        sf.reference1=Label(sf.f1,font=('arial',16,'bold'),text="REFERENCE ID :",bd=10,anchor='w',bg='#6189A8')
        sf.reference1.grid(row=1,column=6)
        sf.reference_entry=Entry(sf.f1,font=('arial',16,'bold'),textvariable=sf.reference,bd=7,
                                 insertwidth=4,justify='right')
        sf.reference_entry.grid(row=1,column=7)
        
        sf.costmeal1=Label(sf.f1,font=('arial',16,'bold'),text="COST OF ORDER :",bd=10,anchor='w',bg='#6189A8')
        sf.costmeal1.grid(row=2,column=6)
        sf.costmeal_entry=Entry(sf.f1,font=('arial',16,'bold'),textvariable=sf.costmeal,bd=7,
                                 insertwidth=4,justify='right')
        sf.costmeal_entry.grid(row=2,column=7)
        
        sf.service1=Label(sf.f1,font=('arial',16,'bold'),text="SERVICE CHARGE :",bd=10,anchor='w',bg='#6189A8')
        sf.service1.grid(row=3,column=6)
        sf.service_entry=Entry(sf.f1,font=('arial',16,'bold'),textvariable=sf.service,bd=7,
                                 insertwidth=4,justify='right')
        sf.service_entry.grid(row=3,column=7)
        
        sf.state1=Label(sf.f1,font=('arial',16,'bold'),text="STATE TAX :",bd=10,anchor='w',bg='#6189A8')
        sf.state1.grid(row=4,column=6)
        sf.state_entry=Entry(sf.f1,font=('arial',16,'bold'),textvariable=sf.state,bd=7,
                                 insertwidth=4,justify='right')
        sf.state_entry.grid(row=4,column=7)
        
        sf.subtotal1=Label(sf.f1,font=('arial',16,'bold'),text="SUB TOTAL :",bd=10,anchor='w',bg='#6189A8')
        sf.subtotal1.grid(row=5,column=6)
        sf.subtotal_entry=Entry(sf.f1,font=('arial',16,'bold'),textvariable=sf.subtotal,bd=7,
                                 insertwidth=4,justify='right')
        sf.subtotal_entry.grid(row=5,column=7)
        
        sf.totalcost1=Label(sf.f1,font=('arial',16,'bold'),text="TOTAL COST :",bd=10,anchor='w',bg='#6189A8')
        sf.totalcost1.grid(row=6,column=6)
        sf.totalcost_entry=Entry(sf.f1,font=('arial',16,'bold'),textvariable=sf.totalcost,bd=7,
                                 insertwidth=4,justify='right')
        sf.totalcost_entry.grid(row=6,column=7)
        #====================================================================================================
        sf.btntotal=Button(sf.f1,padx=5,pady=5,fg="black",font=('arial',16,'bold'),
                           width=10,text="TOTAL",bg="powder blue",bd=5,command=sf.Ref)
        sf.btntotal.grid(row=8,column=6)
        
        sf.btnreset=Button(sf.f1,padx=5,pady=5,fg="black",font=('arial',16,'bold'),
                           width=10,text="RESET",bg="powder blue",bd=5,command=sf.Reset)
        sf.btnreset.grid(row=8,column=7)
        
        sf.btnexit=Button(sf.f1,padx=5,pady=5,fg="black",font=('arial',16,'bold'),
                          width=10,text="EXIT",bg="powder blue",bd=5,command=sf.qexit)
        sf.btnexit.grid(row=10,column=6)

        
        sf.scr2.mainloop()

    def Ref(sf):
        sf.x=random.randint(10000,99999)
        sf.reference_entry=str(sf.x)
        sf.reference.set(sf.reference_entry)
        #====================================================================================================

        sf.comar=(float(sf.mar.get()))*195.00
        sf.cocheese_mar=(float(sf.cheese_mar.get()))*180.00
        sf.cofarm=(float(sf.farm.get()))*210.00
        sf.copeppy=(float(sf.peppy.get()))*300.00
        sf.cogreenwave=(float(sf.greenwave.get()))*400.00
        sf.codeluxeveggie=(float(sf.deluxeveggie.get()))*450.00
        sf.cocheesecorn=(float(sf.cheesecorn.get()))*350.00
        sf.cobar=(float(sf.bar.get()))*250.00
        sf.cotikka=(float(sf.tikka.get()))*450.00
        sf.cosausage=(float(sf.sausage.get()))*500.00
        sf.cosupreme=(float(sf.supreme.get()))*450.00
        sf.codominator=(float(sf.dominator.get()))*350.00
        sf.cofiesta=(float(sf.fiesta.get()))*450.00
        sf.coperi=(float(sf.peri.get()))*600.00
        sf.cocapsicum=(float(sf.capsicum.get()))*80.00
        sf.coonion=(float(sf.onion.get()))*60.00
        sf.copaneer=(float(sf.paneer.get()))*110.00
        sf.coloaded=(float(sf.loaded.get()))*115.00
        sf.cogoldencorn=(float(sf.goldencorn.get()))*120.00
        sf.cococacola=(float(sf.cocacola.get()))*70.00
        sf.copepsi=(float(sf.pepsi.get()))*50.00
        sf.total=(sf.comar + sf.cocheese_mar + sf.cofarm + sf.copeppy + sf.cogreenwave + sf.codeluxeveggie +
               sf.cocheesecorn + sf.cobar + sf.cotikka + sf.cosausage + sf.cosupreme + sf.codominator +
               sf.cofiesta + sf.coperi + sf.cocapsicum + sf.coonion + sf.copaneer + sf.coloaded + sf.cogoldencorn +
               sf.cococacola + sf.copepsi)
        sf.paytax=(sf.total)*0.18
        sf.ser_charge=(sf.total)/99.0
        sf.cooforder="₹","{:.2f}".format(sf.total)
        sf.coservice="₹","{:.2f}".format(sf.ser_charge)
        sf.paidtax="₹","{:.2f}".format(sf.paytax)
        sf.overcost="₹","{:.2f}".format(sf.total + sf.paytax + sf.ser_charge)
        sf.costmeal.set(sf.cooforder)
        sf.service.set(sf.coservice)
        sf.state.set(sf.paidtax)
        sf.subtotal.set(sf.cooforder)
        sf.totalcost.set(sf.overcost)
        
        
        
        
    def qexit(sf):
        sf.scr2.destroy()
    def Reset(sf):
        sf.mar.set(0)
        sf.cheese_mar.set(0)
        sf.farm.set(0)
        sf.peppy.set(0)
        sf.greenwave.set(0)
        sf.deluxeveggie.set(0)
        sf.cheesecorn.set(0)
        sf.bar.set(0)
        sf.tikka.set(0)
        sf.sausage.set(0)
        sf.supreme.set(0)
        sf.dominator.set(0)
        sf.fiesta.set(0)
        sf.peri.set(0)
        sf.capsicum.set(0)
        sf.onion.set(0)
        sf.paneer.set(0)
        sf.loaded.set(0)
        sf.goldencorn.set(0)
        sf.cocacola.set(0)
        sf.pepsi.set(0)
        sf.reference.set("")
        sf.costmeal.set("")
        sf.service.set("")
        sf.state.set("")
        sf.subtotal.set("")
        sf.totalcost.set("")

            
if __name__=='__main__':
    x=Log()
    x.login()
