from yahoo_fin import stock_info as si
from tkinter import *



def get_stock_price():
    print('Retrieving live stock data...')
    try:
        price = si.get_live_price(stock.get())
        current_stock.set(price)
    except AssertionError as ae:
        print('No data for this stock. Try entering the correct symbol again!')
    except KeyError as ke:
        print('No data for this stock. Try entering the correct symbol again!')

root = Tk()
root.title('Stock Price Checker')
current_stock = StringVar()

Label(root, text="Company Symbol : ").grid(row=0, sticky=W)
Label(root, text="Stock Price: ").grid(row=3, sticky=W)

result2 = Label(root, text=" ",bg="white", fg="purple", textvariable=current_stock).grid(row=3,column=1,sticky=W)
stock = Entry(root)
stock.grid(row=0,column=1)

b = Button(root, text="Show", command=get_stock_price)

b.grid(row=0,column=2, columnspan=2,rowspan=2,padx=5,pady=5)

mainloop()
