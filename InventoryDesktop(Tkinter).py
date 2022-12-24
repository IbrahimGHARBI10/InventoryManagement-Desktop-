import datetime
from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import datetime

class Inventory:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='powder blue')

############################Frame#################################################################################
        MainFrame = Frame(self.root , bd=20 , width=1350 , height=700 ,bg='cadet blue',relief=RIDGE)
        MainFrame.grid()
        LeftFraime = Frame(MainFrame,bd=10 , width=750 , height=600,padx=10 ,bg='cadet blue', relief=RIDGE)
        LeftFraime.pack(side=LEFT)

        RightFrame = Frame(MainFrame, bd=10 , width=560 , height=600,padx=10 ,bg='cadet blue',relief=RIDGE)
        RightFrame.pack(side=RIGHT)
############################Frames for the following widget,labels,Entry widget#########################
        LeftFraime0 = Frame(LeftFraime, bd=5, width=712, height=143, padx=5, bg='powder blue', relief=RIDGE)
        LeftFraime0.grid(row=0,column=0)
        LeftFraime1 = Frame(LeftFraime, bd=5, width=712, height=170, padx=5, bg='powder blue', relief=RIDGE)
        LeftFraime1.grid(row=1, column=0)
        LeftFraime2 = Frame(LeftFraime, bd=5, width=712, height=168, padx=5, bg='powder blue', relief=RIDGE)
        LeftFraime2.grid(row=2, column=0)
        LeftFraime3 = Frame(LeftFraime, bd=5, width=712, height=95, padx=5, bg='powder blue', relief=RIDGE)
        LeftFraime3.grid(row=3, column=0)

        RightFrame0 = Frame(RightFrame, bd=5, width=522, height=200, padx=5, bg='powder blue', relief=RIDGE)
        RightFrame0.grid(row=0,column=0)
        RightFrame1 = Frame(RightFrame, bd=5, width=522, height=280, padx=5, bg='powder blue', relief=RIDGE)
        RightFrame1.grid(row=1, column=0)
        RightFrame2 = Frame(RightFrame, bd=5, width=522, height=95, padx=5, bg='powder blue', relief=RIDGE)
        RightFrame2.grid(row=2, column=0)
        Acctopen= StringVar()
        AppDate= StringVar()
        NextCreditReview=StringVar()
        DateRev=StringVar()
        LaCRev=StringVar()
        prodcode=StringVar()
        prodtype=StringVar()
        nodays=StringVar()
        costpday=StringVar()
        crelimit=StringVar()
        crecheck=StringVar()
        settdyeday=StringVar()
        payement=StringVar()
        discount=StringVar()
        deposit=StringVar()
        paydueday=StringVar()
        payementm=StringVar()
        var1=IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5=IntVar()
        tax=StringVar()
        subtotal=StringVar()
        total=StringVar()
        receipt_ref=StringVar()


        def Reset():
            Acctopen.set("")
            AppDate.set("")
            NextCreditReview.set("")
            DateRev.set("")
            LaCRev.set("")
            prodcode.set("")
            prodtype.set("")
            nodays.set("")
            costpday.set("")
            crelimit.set("")
            crecheck.set("")
            settdyeday.set("")
            payement.set("")
            discount.set("")
            deposit.set("")
            paydueday.set("")
            payementm.set("")
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            tax.set(0)
            subtotal.set("")
            total.set("")
            self.txtinfo.delete("1.0",END)
            self.txtinfo2.delete("1.0",END)
            return

        def iExit():
            iExit=tkinter.messagebox.askyesno("Inventory Systems", "Confirm if you want to exit")
            if iExit >0:
                root.destroy()
                return

        def Prod(evt1):
            values=str(self.cboproducttyper.get())
            pType = values
            if pType=="Lawnmower":
                prodcode.set("Lam981")
                costpday.set("12")
                crecheck.set("no")
                settdyeday.set("10")
                payement.set("no")
                deposit.set("no")
                payementm.set("cash")
                n = float(LaCRev.get())
                s = float(settdyeday.get())
                price = (s * n)
                tk = "£", str('%.2f' % (price))
                paydueday.set(tk)
            elif pType=="Pickup van":
                prodcode.set("Lam981")
                costpday.set("12")
                crecheck.set("no")
                settdyeday.set("12")
                payement.set("no")
                deposit.set("no")
                payementm.set("cash")
                n = float(LaCRev.get())
                s = float(settdyeday.get())
                price = (s * n)
                tk = "£", str('%.2f' % (price))
                paydueday.set(tk)
            elif pType=="Cement Mixer":
                prodcode.set("Lam981")
                costpday.set("12")
                crecheck.set("no")
                settdyeday.set("12")
                payement.set("no")
                deposit.set("no")
                payementm.set("cash")
                n = float(LaCRev.get())
                s = float(settdyeday.get())
                price = (s * n)
                tk = "£", str('%.2f' % (price))
                paydueday.set(tk)
            elif pType=="elec generator":
                prodcode.set("elect721")
                costpday.set("£15")
                crecheck.set("no")
                settdyeday.set("15")
                payement.set("no")
                deposit.set("no")
                payementm.set("Master Card")
                n = float(LaCRev.get())
                s = float(settdyeday.get())
                price = (s * n)
                tk = "£", str('%.2f' % (price))
                paydueday.set(tk)
        def totale():
            n = float(LaCRev.get())
            s = float(settdyeday.get())
            price = (s * n)
            st = "£", str('%.2f' % (price))
            itax="£", str('%.2f' % ((price)*0.15))
            tax.set(itax)
            subtotal.set(st)
            tc="£", str('%.2f' % (((price)*0.15)+price))
            total.set(tc)
            self.txtinfo2.delete("1.0", END)
            x=random.randint(10908,500876)
            randomRef=str(x)
            receipt_ref.set("Bill"+randomRef)
            self.txtinfo2.insert(END, 'Receipt ref:  ' + receipt_ref.get() + ' ' + AppDate.get() + "\n")
            self.txtinfo2.insert(END, 'product type:   ' + prodtype.get() + "\n")
            self.txtinfo2.insert(END, 'oriduct code:   ' + prodcode.get() + "\n")
            self.txtinfo2.insert(END, 'no of days:   ' + nodays.get() + "\n")
            self.txtinfo2.insert(END, 'account open:   ' + Acctopen.get() + "\n")
            self.txtinfo2.insert(END, 'nextcreditRev:   ' + NextCreditReview.get() + "\n")
            self.txtinfo2.insert(END, 'lastcreditreview:   ' + LaCRev.get() + "\n")
            self.txtinfo2.insert(END, 'Tax:  ' + tax.get() + "\n")
            self.txtinfo2.insert(END, 'Sub total:  ' + str(subtotal.get()) + "\n")
            self.txtinfo2.insert(END, 'totale cost :  ' + str(total.get()) + "\n")

        def checkcredit():
            if (var1.get()==1):
                self.txtinfo.insert(END, "\tCheck credit\n")
            if (var1.get() == 0):
                self.txtinfo.delete("1.0",END)
        def termagreed():
            if (var2.get()==1):
                self.txtinfo.insert(END,"\tCheck Term agreed\n")
            if (var2.get() == 0):
                self.txtinfo.delete("1.0",END)
        def acctonhold():
            if (var3.get()==1):
                self.txtinfo.insert(END,"\tCheck acount on hold\n")

            if (var3.get() == 0):
                self.txtinfo.delete("1.0",END)
        def restrictedmails():
            if (var4.get()==1):
                self.txtinfo.insert(END,"\tCheck\n")
            if (var4.get() == 0):
                self.txtinfo.delete("1.0",END)
        def iDates(evt):
            values=str(self.cbonodays.get())
            ndays=values
            if ndays=="1-30":
                d1=datetime.date.today()
                d2=datetime.timedelta(days=30)
                d3=(d1+d2)
                AppDate.set(d1)
                NextCreditReview.set(d3)
                LaCRev.set(30)
                DateRev.set(d3)
                crelimit.set("£150")
                discount.set("%5")
                Acctopen.set("yes")
            elif ndays=="31-90":
                d1=datetime.date.today()
                d2=datetime.timedelta(days=90)
                d3=(d1+d2)
                AppDate.set(d1)
                NextCreditReview.set(d3)
                LaCRev.set(90)
                DateRev.set(d3)
                crelimit.set("£200")
                discount.set("%10")
                Acctopen.set("yes")
            elif ndays=="91-270":
                d1=datetime.date.today()
                d2=datetime.timedelta(days=270)
                d3=(d1+d2)
                AppDate.set(d1)
                NextCreditReview.set(d3)
                LaCRev.set(270)

                crelimit.set("£250")
                discount.set("%15")
                Acctopen.set("yes")
            elif ndays=='270-365':
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=360)
                d3 = (d1 + d2)
                AppDate.set(d1)
                NextCreditReview.set(d3)
                LaCRev.set(360)

                crelimit.set("£300")
                discount.set("%20")
                Acctopen.set("yes")
            elif nodays=='0':
                tkinter.messagebox.showinfo("Zero Selected","You choose zero?")
                Reset()

        ############################LeftFrame0#############################################################

        self.lblnodays=Label(LeftFraime0,font=('arial',18,'bold'),text="No of days:",padx=2,pady=2,
                           bg="powder blue").grid(row=0,column=2, sticky=W)

        self.cbonodays =ttk.Combobox(LeftFraime0,textvariable=nodays,state='readonly',
                                       font=('arial',18 ,'bold'),width=12)
        self.cbonodays.bind("<<ComboboxSelected>>", iDates)
        self.cbonodays['value']=('0','1-30','31-90','91-270','270-365')
        self.cbonodays.current(0)
        self.cbonodays.grid(row=0,column=3)


        self.lblproducttyper = Label(LeftFraime0, font=('arial', 18, 'bold'), text="No of days:", padx=2, pady=2,
                               bg="powder blue").grid(row=0, column=0, sticky=W)

        self.cboproducttyper = ttk.Combobox(LeftFraime0, textvariable=prodtype, state='readonly',
                                      font=('arial', 18, 'bold'), width=12)
        self.cboproducttyper.bind("<<ComboboxSelected>>", Prod)
        self.cboproducttyper['value'] = ('','Lawnmower','Pickup van','Cement Mixer','elec generator')
        self.cboproducttyper.current(0)
        self.cboproducttyper.grid(row=0, column=1)

        self.lblprodcode = Label(LeftFraime0, font=('arial', 18, 'bold'), text="product code", padx=14, pady=4,
                                 bg="powder blue").grid(row=1, column=0, sticky=W)
        self.txtprodcode=Entry(LeftFraime0,textvariable=prodcode,font=('arial', 16, 'bold'),bd=8,fg="black",
                          width=14,justify=LEFT).grid(row=1,column=1,padx=23,pady=5)

        self.lblcostpday = Label(LeftFraime0, font=('arial', 18, 'bold'), text="cost p day", padx=14, pady=4,
                                 bg="powder blue").grid(row=1, column=2, sticky=W)
        self.txtcostpday=Entry(LeftFraime0,textvariable=costpday,font=('arial', 16, 'bold'),bd=8,fg="black",
                          width=14,justify=LEFT).grid(row=1,column=3,padx=23,pady=5)



        ############################LeftFrame1#############################################################

        self.lblcrelimit = Label(LeftFraime1, font=('arial', 18, 'bold'), text="Credit Limit", padx=2, pady=2,
                                    bg="powder blue").grid(row=0, column=0, sticky=W)
        self.cbocrelimit = ttk.Combobox(LeftFraime1, textvariable=crelimit, state='readonly',
                                           font=('arial', 18, 'bold'), width=10)
        self.cbocrelimit['value'] = ('', 'Select an option', '£150', '£200','£250','£300')
        self.cbocrelimit.current(0)
        self.cbocrelimit.grid(row=0, column=1)

        self.lblcrecheck = Label(LeftFraime1, font=('arial', 18, 'bold'), text="Credit check:", padx=2, pady=2,
                               bg="powder blue").grid(row=0, column=2, sticky=W)
        self.cbocrecheck = ttk.Combobox(LeftFraime1, textvariable=crecheck, state='readonly',
                                      font=('arial', 18, 'bold'), width=12)
        self.cbocrecheck['value'] = ('', 'Student', 'Lecture', 'Admin staff')
        self.cbocrecheck.current(0)
        self.cbocrecheck.grid(row=0, column=3)

        self.lblsetdueday = Label(LeftFraime1, font=('arial', 18, 'bold'), text="Sett.due", padx=14, pady=4,
                                 bg="powder blue").grid(row=1, column=0, sticky=W)
        self.txtsetdueday = Entry(LeftFraime1, textvariable=settdyeday, font=('arial', 16, 'bold'), bd=8, fg="black",
                                 width=14, justify=LEFT).grid(row=1, column=1, padx=23, pady=5)

        self.lblpayementd = Label(LeftFraime1, font=('arial', 18, 'bold'), text="payament due:", padx=1, pady=2,
                                 bg="powder blue").grid(row=1, column=2, sticky=W)
        self.cbopayementd = ttk.Combobox(LeftFraime1, textvariable=payement, state='readonly',
                                        font=('arial', 18, 'bold'), width=12)
        self.cbopayementd['value'] = ('', 'Select an option', 'yes', 'No')
        self.cbopayementd.current(0)
        self.cbopayementd.grid(row=1, column=3)

        self.lbldiscount = Label(LeftFraime1, font=('arial', 18, 'bold'), text="Discount:", padx=2, pady=2,
                                 bg="powder blue").grid(row=2, column=0, sticky=W)
        self.cbodiscount = ttk.Combobox(LeftFraime1, textvariable=discount, state='readonly',
                                        font=('arial', 18, 'bold'), width=10)
        self.cbodiscount['value'] =('0', '5', '10', '15','20')
        self.cbodiscount.current(0)
        self.cbodiscount.grid(row=2, column=1,pady=2)

        self.lbldeposit = Label(LeftFraime1, font=('arial', 18, 'bold'), text="deposit:", padx=2, pady=2,
                                 bg="powder blue").grid(row=2, column=2, sticky=W)
        self.cbodeposit = ttk.Combobox(LeftFraime1, textvariable=deposit, state='readonly',
                                        font=('arial', 18, 'bold'), width=10)
        self.cbodeposit['value'] =  ('', 'Select an option', 'yes', 'No')
        self.cbodeposit.current(0)
        self.cbodeposit.grid(row=2, column=3,pady=2)

        self.lblpaydueday = Label(LeftFraime1, font=('arial', 18, 'bold'), text="Pay due day", padx=14, pady=4,
                                 bg="powder blue").grid(row=3, column=0, sticky=W)
        self.txtpaydueday = Entry(LeftFraime1, textvariable=paydueday, font=('arial', 16, 'bold'), bd=8, fg="black",
                                 width=14, justify=LEFT).grid(row=3, column=1, padx=23, pady=5)

        self.lblpayementm = Label(LeftFraime1, font=('arial', 18, 'bold'), text="payment methode:", padx=1, pady=2,
                                  bg="powder blue").grid(row=3, column=2, sticky=W)
        self.cbopayementm = ttk.Combobox(LeftFraime1, textvariable=payementm, state='readonly',
                                         font=('arial', 18, 'bold'), width=12)
        self.cbopayementm['value'] = ('', 'Select an option', 'Visa card', 'Cash','Master Card')
        self.cbopayementm.current(0)
        self.cbopayementm.grid(row=3, column=3)

        ############################LeftFrame2#############################################################

        LeftFraime2LL=Frame(LeftFraime2,bd=5,width=300,height=160,padx=5,bg="powder blue",relief=RIDGE)
        LeftFraime2LL.grid(row=0,column=0)
        LeftFraime2LR = Frame(LeftFraime2, bd=5, width=300, height=160, padx=5, bg="cadet blue", relief=RIDGE)
        LeftFraime2LR.grid(row=0, column=1)


        self.checkcredit= Checkbutton(LeftFraime2LL,text="Check Credit",variable=var1, onvalue=1,
                                      offvalue=0,font=('arial',16 ,'bold'),bg="powder blue",command=checkcredit).grid(row=0,sticky=W)

        self.checktermagreed = Checkbutton(LeftFraime2LL, text="Term Agreed", variable=var2, onvalue=1,
                                       offvalue=0, font=('arial', 16, 'bold'), bg="powder blue",command=termagreed).grid(row=1, sticky=W)

        self.checkacconhand = Checkbutton(LeftFraime2LL, text="Account On hold", variable=var3, onvalue=1,
                                       offvalue=0, font=('arial', 16, 'bold'), bg="powder blue",command=acctonhold).grid(row=2, sticky=W)

        self.checkrestmaili = Checkbutton(LeftFraime2LL, text="Restrict Mailing", variable=var4, onvalue=1,
                                       offvalue=0, font=('arial', 16, 'bold'), bg="powder blue",command=restrictedmails).grid(row=3, sticky=W)

        self.txtinfo=Text(LeftFraime2LR,height=9,width=43,font=('arial', 16, 'bold'))
        self.txtinfo.grid (row=0,column=0,pady=2)

        ############################LeftFrame3#############################################################
        self.lbltax = Label(LeftFraime3, font=('arial', 18, 'bold'), text="Tax", padx=14, pady=4,
                                 bg="powder blue").grid(row=0, column=0, sticky=W)
        self.txttax=Entry(LeftFraime3,textvariable=tax,font=('arial', 16, 'bold'),bd=8,fg="black",
                          width=14,justify=LEFT).grid(row=1,column=0,padx=23,pady=5)

        self.lblsub = Label(LeftFraime3, font=('arial', 18, 'bold'), text="Sub Total", padx=14, pady=4,
                            bg="powder blue").grid(row=0, column=1, sticky=W)
        self.txtsub = Entry(LeftFraime3, textvariable=subtotal, font=('arial', 16, 'bold'), bd=8, fg="black",
                            width=14, justify=LEFT).grid(row=1, column=1, padx=23, pady=5)

        self.lbltotal = Label(LeftFraime3, font=('arial', 18, 'bold'), text="Total", padx=14, pady=4,
                            bg="powder blue").grid(row=0, column=2, sticky=W)
        self.txttax = Entry(LeftFraime3, textvariable=total, font=('arial', 16, 'bold'), bd=8, fg="black",
                            width=14, justify=LEFT).grid(row=1, column=2, padx=23, pady=5)

        ############################RightFrame0############################################################

        self.lblAcctopen=Label(RightFrame0,font=('arial',18,'bold'),text="Account Opended",padx=2,pady=2,
                           bg="powder blue").grid(row=0,column=0, sticky=W)
        self.cboAcctopen =ttk.Combobox(RightFrame0,textvariable=Acctopen,state='readonly',
                                       font=('arial',18 ,'bold'),width=19)
        self.cboAcctopen['value']=('','Select an option','yes','No')
        self.cboAcctopen.current(0)
        self.cboAcctopen.grid(row=0,column=1)

        self.lblAppDate=Label(RightFrame0,font=('arial',18,'bold'),text="Application Date:",padx=2,pady=2,
                           bg="powder blue").grid(row=1,column=0, sticky=W)
        self.cboAppDate =ttk.Combobox(RightFrame0,textvariable=AppDate,state='readonly',
                                       font=('arial',18 ,'bold'),width=19)
        self.cboAppDate['value']=('','Student','Lecture','Admin staff')
        self.cboAppDate.current(0)
        self.cboAppDate.grid(row=1,column=1)

        self.lblNcreR=Label(RightFrame0,font=('arial',18,'bold'),text="Next credit Review",padx=2,pady=2,
                           bg="powder blue").grid(row=2,column=0, sticky=W)
        self.cboNcreR =ttk.Combobox(RightFrame0,textvariable=NextCreditReview,state='readonly',
                                       font=('arial',18 ,'bold'),width=19)
        self.cboNcreR['value']=('','Student','Lecture','Admin staff')
        self.cboNcreR.current(0)
        self.cboNcreR.grid(row=2,column=1)

        self.lblLaCRev = Label(RightFrame0, font=('arial', 18, 'bold'), text="Last Credit Review", padx=2, pady=2,
                                bg="powder blue").grid(row=3, column=0, sticky=W)
        self.cboLaCRev = ttk.Combobox(RightFrame0, textvariable=LaCRev, state='readonly',
                                       font=('arial', 18, 'bold'), width=19)
        self.cboLaCRev['value'] = ('', 'Student', 'Lecture', 'Admin staff')
        self.cboLaCRev.current(0)
        self.cboLaCRev.grid(row=3, column=1)

        self.lblDateRev=Label(RightFrame0,font=('arial',18,'bold'),text="Account Opended",padx=2,pady=2,
                           bg="powder blue").grid(row=4,column=0, sticky=W)
        self.cboDateRev =ttk.Combobox(RightFrame0,textvariable=DateRev,state='readonly',
                                       font=('arial',18 ,'bold'),width=19)
        self.cboDateRev['value']=('','Student','Lecture','Admin staff')
        self.cboDateRev.current(0)
        self.cboDateRev.grid(row=4,column=1)


        ####################Text,labels,Entry widget,RightFrame1###########################################
        self.txtinfo2 = Text(RightFrame1, height=13, width=29, font=('arial', 16, 'bold'))
        self.txtinfo2.grid(row=0, column=0,sticky=W)
        ####################Button,RightFrame2#############################################################
        self.btnTotal= Button(RightFrame2, padx=18,pady=2,bd=4,fg="black",font=('arial',9,'bold'),
                               width=9,bg="powder blue",text="Total",command=totale).grid(row=0, column=0)
        
        self.btnReset = Button(RightFrame2, padx=18, pady=2, bd=4, fg="black", font=('arial', 9, 'bold'),
                               width=9, bg="powder blue", text="Reset",command=Reset).grid(row=0, column=1)

        self.btnExit = Button(RightFrame2, padx=20, pady=2, bd=4, fg="black", font=('arial', 9, 'bold'),
                               width=9, bg="powder blue", text="Exit",command=iExit).grid(row=0, column=2)



















if __name__=='__main__':
    root = Tk()
    application = Inventory(root)
    root.mainloop()