import Tkinter 
WindowBox = Tkinter.Tk()
WindowBox.geometry("250x200")
WindowBox.title("Welcome to CODS")

getusername = Tkinter.StringVar()
getcontactno = Tkinter.StringVar()
getroomno = Tkinter.StringVar()
gethostelblock = Tkinter.IntVar()
username = getusername.get()

LabelName = Tkinter.Label (WindowBox, text="Username:")
LabelName.pack()
TxtBoxName = Tkinter.Entry (WindowBox, textvariable= getusername)
TxtBoxName.pack()

LabelName = Tkinter.Label (WindowBox, text="Contact number:")
LabelName.pack()
TxtBoxName = Tkinter.Entry (WindowBox, textvariable= getcontactno)
TxtBoxName.pack()

LabelName = Tkinter.Label (WindowBox, text="Room number:")
LabelName.pack()
TxtBoxName = Tkinter.Entry (WindowBox, textvariable= getroomno)
TxtBoxName.pack()




def userinput():
    HB = gethostelblock.get()
    if HB < 1 or HB > 3:
        labelShowName=Tkinter.Label(WindowBox, text="Invalid Hostel Block").pack()
        
    else:
        WindowBox.withdraw()
        MenuBox.deiconify()
    return

LabelName = Tkinter.Label (WindowBox, text="HB:")
LabelName.pack()
TxtBoxName = Tkinter.Entry (WindowBox, textvariable= gethostelblock)
TxtBoxName.pack()

MenuBox = Tkinter.Tk()
MenuBox.geometry("250x170")
MenuBox.title("Main Menu")
MenuBox.withdraw()

BtnName = Tkinter.Button (WindowBox, text="Proceed", command=userinput).pack()


LabelName= Tkinter.Label(MenuBox, text="Category", font=("Impact",20)).grid(row=0,column=2,sticky="new")

def rice():
    MenuBox.withdraw()
    ricebox.deiconify()
    return

def noodles():
    MenuBox.withdraw()
    noodlebox.deiconify()
    return

def western():
    MenuBox.withdraw()
    westernbox.deiconify()
    return

def drinks():
    MenuBox.withdraw()
    drinksbox.deiconify()
    return

def checkout():
    username=getusername.get()
    contactno=getcontactno.get()
    roomno=getroomno.get()
    HB = gethostelblock.get()
    
    LabelName=Tkinter.Label(checkbox,text="Thank you for using CODS, " + username, font="Arial").pack()
    LabelName=Tkinter.Label(checkbox,text="Contact number: " + contactno, font="Arial").pack()
    LabelName=Tkinter.Label(checkbox,text="Room number: " + roomno, font="Arial").pack()
    LabelName=Tkinter.Label(checkbox,text="Hostel block: " + `HB`, font="Arial").pack()
    
    prc_rice = (5*qty_pattaya.get()) + (5*qty_ayampenyet.get()) + (5*qty_nasiayam.get()) + (4*qty_nasigoreng.get()) + (5.50*qty_nasithai.get())
    prc_noodles = (4*qty_migoreng.get()) + (4.50*qty_maggie.get()) + (4*qty_mikari.get()) + (4*qty_misup.get()) + (5*qty_mihun.get())
    prc_western = (6.0*qty_chickenchop.get()) + (8*qty_fishandchip.get()) + (8*qty_pasta.get()) + (8*qty_chickengrill.get()) + (10*qty_lambchop.get())
    prc_drinks = (2.0*qty_miloais.get()) + (3*qty_juice.get()) + (2*qty_sirapbandung.get()) + (2*qty_softdrink.get()) + (2*qty_tehais.get())
    
    LabelName=Tkinter.Label(checkbox, text ="Total rice ordered = RM" + `prc_rice`).pack()
    LabelName=Tkinter.Label(checkbox, text ="Total noodles ordered = RM" + `prc_noodles`).pack()
    LabelName=Tkinter.Label(checkbox, text ="Total western ordered = RM" + `prc_western`).pack()
    LabelName=Tkinter.Label(checkbox, text ="Total drinks ordered = RM" + `prc_drinks`).pack()
    LabelName=Tkinter.Label(checkbox, text ="Orders above RM50.00 will get a 10% discount", font = "Calibri").pack(side="bottom")
    
    MenuBox.withdraw()
    checkbox.deiconify()
    return


ricebox = Tkinter.Toplevel()
ricebox.geometry("290x260")
ricebox.title("Rice")
ricebox.withdraw()


b1 = Tkinter.Button (MenuBox, text="Rice", command=rice,height=1,width=7).grid(row=1,column=1,sticky="e",pady=5,padx=5)
b1 = Tkinter.Button (MenuBox, text="Noodles", command=noodles,height=1,width=7).grid(row=1,column=3,sticky="w",pady=5,padx=5)
b1 = Tkinter.Button (MenuBox, text="Western", command=western,height=1,width=7).grid(row=2,column=1,sticky="e",pady=5,padx=5)
b1 = Tkinter.Button (MenuBox, text="Drinks", command=drinks,height=1,width=7).grid(row=2,column=3,sticky="w",pady=5,padx=5)
b1 = Tkinter.Button (MenuBox, text="Checkout", command=checkout,height=1,width=7).grid(row=3,column=2,sticky="sew",pady=5)

qty_pattaya=Tkinter.IntVar()
qty_ayampenyet=Tkinter.IntVar()
qty_nasiayam=Tkinter.IntVar()
qty_nasigoreng=Tkinter.IntVar()
qty_nasithai=Tkinter.IntVar()

def pattaya():
    qty_pattaya.set(qty_pattaya.get()+1)
    return
def pattaya2():
    if qty_pattaya.get() >0:
        qty_pattaya.set(qty_pattaya.get()-1)
    else:
        qty_pattaya.set(0)
    return
def ayampenyet():
    qty_ayampenyet.set(qty_ayampenyet.get()+1)
    return
def ayampenyet2():
    if qty_ayampenyet.get() >0:
        qty_ayampenyet.set(qty_ayampenyet.get()-1)
    else:
        qty_ayampenyet.set(0)
    return
def nasiayam():
    qty_nasiayam.set(qty_nasiayam.get()+1)
    return
def nasiayam2():
    if qty_nasiayam.get() >0:
        qty_nasiayam.set(qty_nasiayam.get()-1)
    else:
        qty_nasiayam.set(0)
    return

def nasigoreng():
    qty_nasigoreng.set(qty_nasigoreng.get()+1)
    return
def nasigoreng2():
    if qty_nasigoreng.get() >0:
        qty_nasigoreng.set(qty_nasigoreng.get()-1)
    else:
        qty_nasigoreng.set(0)
    return

def nasithai():
    qty_nasithai.set(qty_nasithai.get()+1)
    return
def nasithai2():
    if qty_nasithai.get() >0:
        qty_nasithai.set(qty_nasithai.get()-1)
    else:
        qty_nasithai.set(0)
    return

def ricemenu():
    ricebox.withdraw()
    MenuBox.deiconify()
    
    return


LabelName= Tkinter.Label(ricebox, text="Rice", font=("Impact",20))
LabelName.grid(row =0, column =2)


LabelName = Tkinter.Label(ricebox, text = "Nasi Pattaya, RM5.00")
LabelName.grid(row =2, column =1,pady=7)
TxtBoxName=Tkinter.Label (ricebox, textvariable = qty_pattaya)
TxtBoxName.grid(row=2, column = 4,pady=7)

LabelName = Tkinter.Label(ricebox, text = "Ayam Penyet, RM5.00")
LabelName.grid(row =4, column =1,pady=7)
TxtBoxName=Tkinter.Label (ricebox, textvariable = qty_ayampenyet)
TxtBoxName.grid(row=4, column = 4,pady=7)

LabelName = Tkinter.Label(ricebox, text = "Nasi Ayam, RM5.00")
LabelName.grid(row =6, column =1,pady=7)
TxtBoxName=Tkinter.Label (ricebox, textvariable = qty_nasiayam)
TxtBoxName.grid(row=6, column = 4,pady=7)

LabelName= Tkinter.Label(ricebox, text = "Nasi Goreng, RM4.00")
LabelName.grid(row =8, column =1,pady=7)
TxtBoxName=Tkinter.Label (ricebox, textvariable = qty_nasigoreng)
TxtBoxName.grid(row=8, column = 4,pady=7)

LabelName= Tkinter.Label(ricebox, text = "Nasi Thai, RM5.50")
LabelName.grid(row =10, column =1,pady=7)
TxtBoxName=Tkinter.Label (ricebox, textvariable = qty_nasithai)
TxtBoxName.grid(row=10, column = 4,pady=7)

B3a=Tkinter.Button(ricebox, text = "+", command=pattaya).grid(row=2, column=5)
B3a=Tkinter.Button(ricebox, text = "-", command=pattaya2).grid(row=2, column=3)

B3b=Tkinter.Button(ricebox, text = "+", command=ayampenyet).grid(row=4, column=5)
B3b=Tkinter.Button(ricebox, text = "-", command=ayampenyet2).grid(row=4, column=3)

B3c=Tkinter.Button(ricebox, text = "+", command=nasiayam).grid(row=6, column=5)
B3c=Tkinter.Button(ricebox, text = "-", command=nasiayam2).grid(row=6, column=3)

B3d=Tkinter.Button(ricebox, text = "+", command=nasigoreng).grid(row=8, column=5)
B3d=Tkinter.Button(ricebox, text = "-", command=nasigoreng2).grid(row=8, column=3)

B3e=Tkinter.Button(ricebox, text = "+", command=nasithai).grid(row=10, column=5)
B3e=Tkinter.Button(ricebox, text = "-", command=nasithai2).grid(row=10, column=3)

B3=Tkinter.Button(ricebox, text = "Main Menu", command=ricemenu).grid(row=14, column=4,pady=7)


noodlebox = Tkinter.Toplevel()
noodlebox.geometry("320x260")
noodlebox.title("Noodle")
noodlebox.withdraw()

qty_migoreng = 0
qty_maggie = 0
qty_mikari = 0
qty_misup = 0
qty_mihun = 0

qty_migoreng=Tkinter.IntVar()
qty_maggie=Tkinter.IntVar()
qty_mikari =Tkinter.IntVar()
qty_misup =Tkinter.IntVar()
qty_mihun =Tkinter.IntVar()

def migoreng():
    qty_migoreng.set(qty_migoreng.get()+1)
    return
def migoreng2():
    if qty_migoreng.get() >0:
        qty_migoreng.set(qty_migoreng.get()-1)
    else:
        qty_migoreng.set(0)
    return
def maggie():
    qty_maggie.set(qty_maggie.get()+1)
    return
def maggie2():
    if qty_maggie.get() >0:
        qty_maggie.set(qty_maggie.get()-1)
    else:
        qty_maggie.set(0)
    return
def mikari():
    qty_mikari.set(qty_mikari.get()+1)
    return
def mikari2():
    if qty_mikari.get() >0:
        qty_mikari.set(qty_mikari.get()-1)
    else:
        qty_mikari.set(0)
    return

def misup():
    qty_misup.set(qty_misup.get()+1)
    return
def misup2():
    if qty_misup.get() >0:
        qty_misup.set(qty_misup.get()-1)
    else:
        qty_misup.set(0)
    return

def mihun():
    qty_mihun.set(qty_mihun.get()+1)
    return

def mihun2():
    if qty_mihun.get() >0:
        qty_mihun.set(qty_mihun.get()-1)
    else:
        qty_mihun.set(0)
    return

def noodlemenu():
    noodlebox.withdraw()
    MenuBox.deiconify()
    
    return    

LabelName= Tkinter.Label(noodlebox, text="Noodles", font=("Impact",20))
LabelName.grid(row =0, column =2)


LabelName = Tkinter.Label(noodlebox, text = "Mi Goreng, RM4.00")
LabelName.grid(row =2, column =1,pady=7)
TxtBoxName=Tkinter.Label (noodlebox, textvariable = qty_migoreng)
TxtBoxName.grid(row=2, column = 4,pady=7)

LabelName = Tkinter.Label(noodlebox, text = "Maggie, RM4.50")
LabelName.grid(row =4, column =1,pady=7)
TxtBoxName=Tkinter.Label (noodlebox, textvariable = qty_maggie)
TxtBoxName.grid(row=4, column = 4,pady=7)

LabelName = Tkinter.Label(noodlebox, text = "Mi Kari, RM4.00")
LabelName.grid(row =6, column =1,pady=7)
TxtBoxName=Tkinter.Label (noodlebox, textvariable = qty_mikari)
TxtBoxName.grid(row=6, column = 4,pady=7)

LabelName = Tkinter.Label(noodlebox, text = "Mi Sup, RM4.00")
LabelName.grid(row =8, column =1,pady=7)
TxtBoxName=Tkinter.Label (noodlebox, textvariable = qty_misup)
TxtBoxName.grid(row=8, column = 4,pady=7)

LabelName = Tkinter.Label(noodlebox, text = "Mi Hun, RM5.00")
LabelName.grid(row =10, column =1)
TxtBoxName=Tkinter.Label (noodlebox, textvariable = qty_mihun)
TxtBoxName.grid(row=10, column = 4,pady=7)



B3a=Tkinter.Button(noodlebox, text = "+", command=migoreng).grid(row=2, column=5)
B3a=Tkinter.Button(noodlebox, text = "-", command=migoreng2).grid(row=2, column=3)

B3b=Tkinter.Button(noodlebox, text = "+", command=maggie).grid(row=4, column=5)
B3b=Tkinter.Button(noodlebox, text = "-", command=maggie2).grid(row=4, column=3)

B3c=Tkinter.Button(noodlebox, text = "+", command=mikari).grid(row=6, column=5)
B3c=Tkinter.Button(noodlebox, text = "-", command=mikari2).grid(row=6, column=3)

B3d=Tkinter.Button(noodlebox, text = "+", command=misup).grid(row=8, column=5)
B3d=Tkinter.Button(noodlebox, text = "-", command=misup2).grid(row=8, column=3)

B3e=Tkinter.Button(noodlebox, text = "+", command=mihun).grid(row=10, column=5)
B3e=Tkinter.Button(noodlebox, text = "-", command=mihun2).grid(row=10, column=3)

B3=Tkinter.Button(noodlebox, text = "Main Menu", command=noodlemenu).grid(row=14, column=4)

westernbox = Tkinter.Toplevel()
westernbox.geometry("340x260")
westernbox.title("Western")
westernbox.withdraw()

qty_chickenchop = 0
qty_fishandchip = 0
qty_pasta = 0
qty_lambchop = 0
qty_chickengrill = 0

qty_chickenchop=Tkinter.IntVar()
qty_fishandchip=Tkinter.IntVar()
qty_pasta =Tkinter.IntVar()
qty_lambchop =Tkinter.IntVar()
qty_chickengrill =Tkinter.IntVar()

def chickenchop():
    qty_chickenchop.set(qty_chickenchop.get()+1)
    return
def chickenchop2():
    if qty_chickenchop.get() >0:
        qty_chickenchop.set(qty_chickenchop.get()-1)
    else:
        qty_chickenchop.set(0)
    return
def fishandchip():
    qty_fishandchip.set(qty_fishandchip.get()+1)
    return
def fishandchip2():
    if qty_fishandchip.get() >0:
        qty_fishandchip.set(qty_fishandchip.get()-1)
    else:
        qty_fishandchip.set(0)
    return
def pasta():
    qty_pasta.set(qty_pasta.get()+1)
    return
def pasta2():
    if qty_pasta.get() >0:
        qty_pasta.set(qty_pasta.get()-1)
    else:
        qty_pasta.set(0)
    return

def lambchop():
    qty_lambchop.set(qty_lambchop.get()+1)
    return
def lambchop2():
    if qty_lambchop.get() >0:
        qty_lambchop.set(qty_lambchop.get()-1)
    else:
        qty_lambchop.set(0)
    return

def chickengrill():
    qty_chickengrill.set(qty_chickengrill.get()+1)
    return
def chickengrill2():
    if qty_chickengrill.get() >0:
        qty_chickengrill.set(qty_chickengrill.get()-1)
    else:
        qty_chickengrill.set(0)
    return

def menuwestern():
    westernbox.withdraw()
    MenuBox.deiconify()
    
    return

LabelName= Tkinter.Label(westernbox, text="Western", font=("Impact",20))
LabelName.grid(row =0, column =2)


LabelName = Tkinter.Label(westernbox, text = "Chicken Chop, RM6.00")
LabelName.grid(row =2, column =1,pady=7)
TxtBoxName=Tkinter.Label (westernbox, textvariable = qty_chickenchop)
TxtBoxName.grid(row=2, column=4,pady=7)

LabelName = Tkinter.Label(westernbox, text = "Fish and Chip, RM 8.00")
LabelName.grid(row =4, column =1,pady=7)
TxtBoxName=Tkinter.Label (westernbox, textvariable = qty_fishandchip)
TxtBoxName.grid(row=4, column = 4,pady=7)

LabelName = Tkinter.Label(westernbox, text = "Pasta, RM8.00")
LabelName.grid(row =6, column =1,pady=7)
TxtBoxName=Tkinter.Label (westernbox, textvariable = qty_pasta)
TxtBoxName.grid(row=6, column = 4,pady=7)

LabelName = Tkinter.Label(westernbox, text = "Lamb Chop, RM10.00")
LabelName.grid(row =8, column =1,pady=7)
TxtBoxName=Tkinter.Label (westernbox, textvariable = qty_lambchop)
TxtBoxName.grid(row=8, column = 4,pady=7)

LabelName = Tkinter.Label(westernbox, text = "Chicken Grill, RM8.00")
LabelName.grid(row =10, column =1,pady=7)
TxtBoxName=Tkinter.Label (westernbox, textvariable = qty_chickengrill)
TxtBoxName.grid(row=10, column = 4,pady=7)

B3a=Tkinter.Button(westernbox, text = "+", command=chickenchop).grid(row=2, column=5)
B3a=Tkinter.Button(westernbox, text = "-", command=chickenchop2).grid(row=2, column=3)

B3b=Tkinter.Button(westernbox, text = "+", command=fishandchip).grid(row=4, column=5)
B3b=Tkinter.Button(westernbox, text = "-", command=fishandchip2).grid(row=4, column=3)

B3c=Tkinter.Button(westernbox, text = "+", command=pasta).grid(row=6, column=5)
B3c=Tkinter.Button(westernbox, text = "-", command=pasta2).grid(row=6, column=3)

B3d=Tkinter.Button(westernbox, text = "+", command=lambchop).grid(row=8, column=5)
B3d=Tkinter.Button(westernbox, text = "-", command=lambchop2).grid(row=8, column=3)

B3e=Tkinter.Button(westernbox, text = "+", command=chickengrill).grid(row=10, column=5)
B3e=Tkinter.Button(westernbox, text = "-", command=chickengrill2).grid(row=10, column=3)

B3=Tkinter.Button(westernbox, text = "Main Menu", command=menuwestern).grid(row=14, column=4)

drinksbox = Tkinter.Toplevel()
drinksbox.geometry("320x260")
drinksbox.title("Drinks")
drinksbox.withdraw()

qty_miloais = 0
qty_juice = 0
qty_sirapbandung = 0
qty_softdrink = 0
qty_tehais = 0

qty_miloais=Tkinter.IntVar()
qty_juice=Tkinter.IntVar()
qty_sirapbandung =Tkinter.IntVar()
qty_softdrink =Tkinter.IntVar()
qty_tehais =Tkinter.IntVar()

def miloais():
    qty_miloais.set(qty_miloais.get()+1)
    return
def miloais2():
    if qty_miloais.get() >0:
        qty_miloais.set(qty_miloais.get()-1)
    else:
        qty_miloais.set(0)
    return
def juice():
    qty_juice.set(qty_juice.get()+1)
    return
def juice2():
    if qty_juice.get() >0:
        qty_juice.set(qty_juice.get()-1)
    else:
        qty_juice.set(0)
    return
def sirapbandung():
    qty_sirapbandung.set(qty_sirapbandung.get()+1)
    return
def sirapbandung2():
    if qty_sirapbandung.get() >0:
        qty_sirapbandung.set(qty_sirapbandung.get()-1)
    else:
        qty_sirapbandung.set(0)
    return

def softdrink():
    qty_softdrink.set(qty_softdrink.get()+1)
    return
def softdrink2():
    if qty_softdrink.get() >0:
        qty_softdrink.set(qty_softdrink.get()-1)
    else:
        qty_softdrink.set(0)
    return

def tehais():
    qty_tehais.set(qty_tehais.get()+1)
    return
def tehais2():
    if qty_tehais.get() >0:
        qty_tehais.set(qty_tehais.get()-1)
    else:
        qty_tehais.set(0)
    return

def menudrinks():
    drinksbox.withdraw()
    MenuBox.deiconify()
    
    return

LabelName= Tkinter.Label(drinksbox, text="Drinks", font=("Impact",20))
LabelName.grid(row =0, column =2)


LabelName = Tkinter.Label(drinksbox, text = "Milo Ais, RM2.00")
LabelName.grid(row =2, column =1,pady=7)
TxtBoxName=Tkinter.Label(drinksbox, textvariable = qty_miloais)
TxtBoxName.grid(row=2, column=4,pady=7)

LabelName = Tkinter.Label(drinksbox, text = "Juice, RM3.00")
LabelName.grid(row =4, column =1,pady=7)
TxtBoxName=Tkinter.Label(drinksbox, textvariable = qty_juice)
TxtBoxName.grid(row=4, column = 4,pady=7)

LabelName = Tkinter.Label(drinksbox, text = "Sirap Bandung, RM2.00")
LabelName.grid(row =6, column =1,pady=7)
TxtBoxName=Tkinter.Label(drinksbox, textvariable = qty_sirapbandung)
TxtBoxName.grid(row=6, column = 4,pady=7)

LabelName = Tkinter.Label(drinksbox, text = "Soft Drink, RM2.00")
LabelName.grid(row =8, column =1,pady=7)
TxtBoxName=Tkinter.Label(drinksbox, textvariable = qty_softdrink)
TxtBoxName.grid(row=8, column = 4,pady=7)

LabelName = Tkinter.Label(drinksbox, text = "Teh Ais, RM2.00")
LabelName.grid(row =10, column =1,pady=7)
TxtBoxName=Tkinter.Label(drinksbox, textvariable = qty_tehais)
TxtBoxName.grid(row=10, column = 4,pady=7)

B3a=Tkinter.Button(drinksbox, text = "+", command=miloais).grid(row=2, column=5)
B3a=Tkinter.Button(drinksbox, text = "-", command=miloais2).grid(row=2, column=3)

B3b=Tkinter.Button(drinksbox, text = "+", command=juice).grid(row=4, column=5)
B3b=Tkinter.Button(drinksbox, text = "-", command=juice2).grid(row=4, column=3)

B3c=Tkinter.Button(drinksbox, text = "+", command=sirapbandung).grid(row=6, column=5)
B3c=Tkinter.Button(drinksbox, text = "-", command=sirapbandung2).grid(row=6, column=3)

B3d=Tkinter.Button(drinksbox, text = "+", command=softdrink).grid(row=8, column=5)
B3d=Tkinter.Button(drinksbox, text = "-", command=softdrink2).grid(row=8, column=3)

B3e=Tkinter.Button(drinksbox, text = "+", command=tehais).grid(row=10, column=5)
B3e=Tkinter.Button(drinksbox, text = "-", command=tehais2).grid(row=10, column=3)

B3=Tkinter.Button(drinksbox, text = "Main Menu", command=menudrinks).grid(row=14, column=4)

from tkMessageBox import *
checkbox = Tkinter.Toplevel()
checkbox.geometry("350x230")
checkbox.title("Checkout")
checkbox.withdraw()


def totaloverall():
    prc_rice = (5*qty_pattaya.get()) + (5*qty_ayampenyet.get()) + (5*qty_nasiayam.get()) + (4*qty_nasigoreng.get()) + (5.50*qty_nasithai.get())
    prc_noodles = (4*qty_migoreng.get()) + (4.50*qty_maggie.get()) + (4*qty_mikari.get()) + (4*qty_misup.get()) + (5*qty_mihun.get())
    prc_western = (6*qty_chickenchop.get()) + (8*qty_fishandchip.get()) + (8*qty_pasta.get()) + (8*qty_chickengrill.get()) + (10*qty_lambchop.get())
    prc_drinks = (2*qty_miloais.get()) + (3*qty_juice.get()) + (2*qty_sirapbandung.get()) + (2*qty_softdrink.get()) + (2*qty_tehais.get())
    total_overall = prc_rice + prc_noodles + prc_western + prc_drinks +0.50
    if total_overall <=5:
        showinfo('Error', 'Not enough minimum order of RM5.00')
        checkbox.withdraw()
        MenuBox.deiconify()
    elif total_overall>=50:
        disc_overall=total_overall*90/100
        showinfo('Thank You', 'Your total order with discount is RM'+`disc_overall`+'. Your order will arrive soon')
        checkbox.destroy()
    else:
        showinfo('Thank You', ' Your total order is RM'+`total_overall`+'. Your order will arrive soon')
        checkbox.destroy()
    return

btntotal=Tkinter.Button(checkbox,text="Checkout", command=totaloverall).pack(side="bottom")
WindowBox.mainloop()


