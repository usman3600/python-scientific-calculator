from  tkinter import *
from tkinter.ttk  import *
import math
class Calculator:
                def __init__(self):
                    self.root = Tk()
                    self.root.geometry("322x500")
                    self.root.resizable(0, 0)
                    self.root.title("Calculator")
                    self.root.columnconfigure(0, weight=1)
                    self.number_pad_buttons()
                    self.bottom_number_pad()
                    self.symbols = ["(", ")", "+", "-", chr(247), "x" , "^", "="]
                    self.special_operators = {"±":"-", chr(247):"/","x":"*",  "^":"**"}
                    self.keys = ["Exit", "Clear", "⌫", "x²",  "x³", "10ˣ", "√ˣ", "n!",  "log", "sin", "cos", "tan"]
                    self.top_pad_buttons(self.keys, self.root)
                    self.functions_button(self.symbols)
                    self.collect_input = ""
                    self.user_type_keypad = ""
                    self.operand = ""
                    self.style = Style()
                    
                    self.user_input_display = Entry(master=self.root, state="readonly",   font="Verdana 13", width=53, justify="right")
                    self.inner_entry = Entry(master=self.root, state="readonly", style="style.TEntry",  width=53,  justify="right")
                    self.inner_entry.grid(row=1, in_=self.user_input_display)
                    self.user_input_display.grid(row=1, ipady= 28, rowspan=2, sticky="w")
                    self.label_text = Label(self.root, font="times 15", text="Scientific", width=32)
                    self.commandx = ["", "self.clear_display()", "self.back_space()", "self.square_root_2()", "self.cube_root()","self.base_ten_root()",
                    "self.square_root()", "self.factorial()", "self.log()", "self.sin()", "self.cos()", "self.tan()"]
                    self.style.configure("Tlabel", fg="white", bg="black")
                    self.label_text.grid(row=0, ipady="10",  columnspan=3, column=0, sticky="w")
                    self.style.configure(".",  foreground ="#900763",  background="blue")
            
                def top_pad_buttons(self, keys, root):
                    index = 0
                    frame = Frame()
                    frame.grid(row=3, rowspan=3, sticky="nw")
                    for x in range(3,7):
                        for o in range(3, 6):
                            button = Button(frame, text=keys[index], width=13, command= self.root.destroy if index == 0 else lambda x=index:eval(self.commandx[x]))
                            button.grid(row=x, column=o, ipady=11)
                            index+=1
            
                def number_pad_buttons(self):
                    count = 1
                    frame = Frame()
                    frame.grid(sticky="nw",  row=6, rowspan=9)
                    for x in range(4, 7):
                        for o in range(4, 7):
                            button = Button(frame, text=count, width=13, style="TButton", command=lambda  x=count:self.user_input(x))
                            button.grid(row=x, column=o, ipady=11)
                            count+=1
                
                def functions_button(self, lists):
                    frame = Frame()
                    frame.grid(rowspan=len(lists), row=3, sticky="ee")
                    row_count = 3
                    for x in range(len(lists)):
                        button = Button(frame, text=lists[x], width=8, command=(lambda:self.equal_to()) if x == len(lists)-1 else lambda x= x:self.user_input(lists[x]))
                        button.grid(row=row_count, ipady=11)
                        row_count += 1
                
                def bottom_number_pad(self):
                    signs  = ["±", "0", "."]
                    frame = Frame()
                    frame.grid(row=10, rowspan=2, sticky="nw") 
                    for o, x in enumerate(signs):
                        button = Button(frame, text=x, width=13, command=lambda x= o:self.user_input(signs[x]))
                        button.grid(row=0, column=o,  ipady=11)

                def user_input(self, key):
                        if  key in self.symbols:
                            self.inner_entry.configure(state="active")
                            self.collect_input = self.special_operators.get(str(key), str(key))
                            self.operand  += self.collect_input
                            self.inner_entry.insert(END, self.operand)
                            self.inner_entry.configure(state="readonly")
                            self.operand = ""
                        
                            self.user_input_display.configure(state="active")
                            self.user_input_display.delete(0, END)
                            self.user_input_display.configure(state="readonly")
                        else:
                            self.collect_input = self.special_operators.get(str(key), str(key))
                            self.user_type_keypad  += self.collect_input
                            self.operand += self.collect_input
                            self.user_input_display.configure(state="active")
                            self.user_input_display.insert(END, self.collect_input)
                            self.user_input_display.configure(state="readonly")
                            print(self.collect_input)
                            return self.user_type_keypad
                    
                def clear_display(self):
                        self.user_input_display.configure(state="active")
                        self.user_input_display.delete(0, END)
                        self.user_input_display.configure(state="readonly")
                        self.inner_entry.configure(state="active")
                        self.inner_entry.delete(0, END)
                        self.inner_entry.configure(state="readonly")

                def back_space(self):
                        self.user_input_display.configure(state="active")
                        self.user_input_display.delete(len(self.user_input_display.get())-1)
                        self.user_input_display.configure(state="readonly")

                def  factorial(self):
                    try:
                        if  float(self.user_input_display.get()) > 3000:
                           evaluate = "Overflow!"
                        else:
                            evaluate = math.factorial(int(self.user_input_display.get()))
                    except Exception :
                        evaluate = "Invalid Expression!"
                        
                    self.user_input_display.configure(state="active")
                    self.user_input_display.delete(0, END)
                    self.user_input_display.insert(END, evaluate)
                    self.user_input_display.configure(state="readonly")

                def square_root(self):
                    try:
                        evaluate = int(float(self.user_input_display.get()))**0.5
                    except Exception:
                        evaluate = "Invalid Expression!"
                    self.user_input_display.configure(state="active")
                    self.user_input_display.delete(0, END)
                    self.user_input_display.insert(END, evaluate)
                    self.user_input_display.configure(state="readonly")

                    
                def log(self):
                    try:
                        evaluate = math.log10(float(self.user_input_display.get()))
                    except Exception:
                        evaluate = "Invalid Expression!"
                    self.user_input_display.configure(state="active")
                    self.user_input_display.delete(0, END)
                    self.user_input_display.insert(END, evaluate)
                    self.user_input_display.configure(state="readonly")

                def sin(self):
                    try:
                        evaluate = math.sin(float(self.user_input_display.get()))
                    except Exception:
                        evaluate = "Invalid Expression!"
                    self.user_input_display.configure(state="active")
                    self.user_input_display.delete(0, END)
                    self.user_input_display.insert(END, evaluate)
                    self.user_input_display.configure(state="readonly")

                def cos(self):
                    try:
                        evaluate = math.cos(float(self.user_input_display.get()))
                    except Exception:
                        evaluate = "Invalid Expression!"
                    self.user_input_display.configure(state="active")
                    self.user_input_display.delete(0, END)
                    self.user_input_display.insert(END, evaluate)
                    self.user_input_display.configure(state="readonly")

                def tan(self):
                    try:
                        evaluate = math.tan(float(self.user_input_display.get()))
                    except Exception:
                        evaluate = "Invalid Expression!"
                    self.user_input_display.configure(state="active")
                    self.user_input_display.delete(0, END)
                    self.user_input_display.insert(END, evaluate)
                    self.user_input_display.configure(state="readonly")
                    
                def square_root_2(self):
                    try:
                        evaluate = float(self.user_input_display.get()) **2
                    except Exception:
                        evaluate = "Invalid Expression!"
                    self.user_input_display.configure(state="active")
                    self.user_input_display.delete(0, END)
                    self.user_input_display.insert(END, evaluate)
                    self.user_input_display.configure(state="readonly")

                def base_ten_root(self):
                    try:
                        evaluate = 10**(float(self.user_input_display.get()))
                    except Exception:
                        evaluate = "Invalid Expression!"
                    self.user_input_display.configure(state="active")
                    self.user_input_display.delete(0, END)
                    self.user_input_display.insert(END, evaluate)
                    self.user_input_display.configure(state="readonly")

                def cube_root(self):
                    try:
                        evaluate = (float(self.user_input_display.get())) **3
                    except Exception:
                        evaluate = "Invalid Expression!"
                    self.user_input_display.configure(state="active")
                    self.user_input_display.delete(0, END)
                    self.user_input_display.insert(END, evaluate)
                    self.user_input_display.configure(state="readonly")

                def equal_to(self):
                    try:
                        evaluate = eval(str(self.inner_entry.get()+self.user_input_display.get()))
                        
                    except Exception as error:
                        evaluate = f"Invalid Expression! {error}"
                    self.user_input_display.configure(state="active")
                    self.user_input_display.delete(0, END)
                    self.user_input_display.insert(END, evaluate)
                    self.user_input_display.configure(state="readonly")
                    self.inner_entry.configure(state="active")
                    self.inner_entry.delete(0, END)
                    self.inner_entry.configure(state="readonly")
                
                def run(self):
                    self.root.mainloop()

    
if __name__ == "__main__":
    cal = Calculator()
    cal.run()
