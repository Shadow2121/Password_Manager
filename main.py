import tkinter as tk

temp_list = []

def add_new():
    global e1,e2,e3,temp_list,wn

    if e2.get() == '' or e3.get() == '':
        return
    temp_list.append([e1.get(), e2.get(), e3.get()])
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)

    print(temp_list)
    for i in range(len(temp_list)):
        for j in range(3):
            l1 = tk.Label(wn, text = temp_list[i][j])
            l1.grid(row = (5+i), column = (j*2), )
            l1.grid(row = (5+i), column = (j*2), columnspan = 2)

def new_win():
    global e1,e2,e3, temp_list,wn
    print("new_win")
    wn = tk.Tk()

    l1 = tk.Label(wn, text = "Tag(name)")
    e1 = tk.Entry(wn)
    l1.grid(row = 0, column = 0, columnspan=2)
    e1.grid(row = 0, column = 2, columnspan=2)

    l2 = tk.Label(wn, text = "email id")
    e2 = tk.Entry(wn)
    l2.grid(row = 1, column = 0, columnspan=2)
    e2.grid(row = 1, column = 2, columnspan=2)

    l3 = tk.Label(wn, text = "Password")
    e3 = tk.Entry(wn)
    l3.grid(row = 2, column = 0, columnspan=2)
    e3.grid(row = 2, column = 2, columnspan=2)

    enter_new_button = tk.Button(wn, text = "New", command = add_new)
    enter_new_button.grid(row = 3,column = 0, columnspan=6)

    l1 = tk.Label(wn, text = "Tag(name)")
    l2 = tk.Label(wn, text = "Email ID")
    l3 = tk.Label(wn, text = "Password")
    l1.grid(row = 4, column = 0, columnspan = 2)
    l2.grid(row = 4, column = 2, columnspan = 2)
    l3.grid(row = 4, column = 4, columnspan = 2)

    wn.mainloop()


def get_password():
    passwed = entry.get()
    if passwed == "":  ## Enter your password in blank str
        print("correct")
        new_win()
    else:
        print("Incorrect")
        temp_lable = tk.Label(text = "Incorrect password!!")
        temp_lable.grid(row = 5, column = 0, columnspan=2)

win = tk.Tk()
lable = tk.Label(text = "Password")
entry = tk.Entry(win, show="*", width = 20)
enter_button = tk.Button(text = "Enter", command = get_password)
lable.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1)
enter_button.grid(row = 2, column = 0, columnspan=2)

win.mainloop()