import tkinter as tk
from get_stocks import functionality
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Test",
                                  prompt="Which product do you want to buy?:")

create_stocks = functionality(USER_INP)
create_stocks.stocks()


