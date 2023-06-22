from tkinter import *
import requests
from tkinter import messagebox


root=Tk()
root.title("Currency Converter")
currency_label=Label(root, text = 'currency converted from').grid(row=0,column=0)
currency=Entry(root)
currency.grid(row=0, column=1)

convertto_Label=Label(root, text = 'currency converted to').grid(row=1,column=0)
convertto=Entry(root)
convertto.grid(row=1, column=1)

amount1_label=Label(root, text = 'Amount to convert').grid(row=2,column=0)
amount1=Entry(root)
amount1.grid(row=2, column=1)

def onclick():
    rate = requests.get(f"https://api.frankfurter.app/latest?amount={amount1.get()}&from={currency.get()}&to={convertto.get()}")
    if(rate.status_code==200):
        mylabel=Label(root,text=F"The converted ammount in {convertto.get()} is {rate.json()['rates'][convertto.get()]}").grid(row=4,column=1)
       #mylabel.grid(row=4,column=1)
    else:
        messagebox.showinfo("warning","you have entered wrong inputs,please correct it",bg="green")
mybutton=Button(root,text="covert now",command=onclick)
mybutton.grid(row=3, column=0)


root.mainloop()
