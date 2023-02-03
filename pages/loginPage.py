import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import menuPage

class LogInPage:
    def __init__(self, window):
        self.window = window
        self.window.title('Log In Page')
        self.window.geometry('1600x700')
        self.window.configure(bg="#262626")
        self.window.resizable(0,0)
        #self.window.state('zoomed')

        # ============= variables to set the username and password credentials =======================
        usernameData = 'admin'
        passData = '1234'

        # ============= go to main menu page function =========================
        def go_pageMenu(): 
            win = Toplevel()
            menuPage.MenuPage(win)
            self.window.withdraw()
            win.deiconify()

        # =========== sign in/log in function ================
        def signin():
            username = e1.get()
            password = e2.get()

            if username == usernameData and password == passData:
                go_pageMenu()

            elif username!= usernameData and password!= passData:
                messagebox.showerror("Invalid", "Invalid username and password, please try again.")

            elif password!= passData:
                messagebox.showerror("Invalid", "Invalid password, please try again.")      

            elif username!= usernameData:
                messagebox.showerror("Invalid", "Invalid username, please try again.")      

        # =============== username entry box ==============
        def on_enterE1(e):
            e1.delete(0, 'end')

        def on_leaveE1(e):
                name = e1.get()
                if name == '':
                    e1.insert(0, 'Username')

        e1 = Entry(self.window, width = 88, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e1.place(x = 450, y = 300)
        e1.insert(0, 'Username')
        e1.bind('<FocusIn>', on_enterE1)
        e1.bind('<FocusOut>', on_leaveE1)
        Frame(self.window, width=709, height=2, bg='white').place(x=450, y=325)


        # ================ password entry box ==============
        def on_enterE2(e):
            e2.delete(0, 'end')

        def on_leaveE2(e):
                name = e2.get()
                if name == '':
                    e2.insert(0, 'Password')

        e2 = Entry(self.window, width = 88, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e2.place(x = 450, y = 380)
        e2.insert(0, 'Password')
        e2.bind('<FocusIn>', on_enterE2)
        e2.bind('<FocusOut>', on_leaveE2)
        Frame(self.window, width=709, height=2, bg='white').place(x=450, y=405)


        # ================ Labels ==========================
        tk.Label(self.window, text = "Log In", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 30, 'bold')).place(x = 740, y = 80)

        tk.Label(self.window, text = "Please enter the correct credentials to access the Ticket Management System.",
                 fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 12)).place(x = 520, y = 170)

        # ================ Log In Button ================
        Button(self.window, text = "Log In", command = signin, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 10)).place(x=450, y = 550)

def logInPage():
    window = Tk()
    LogInPage(window)
    window.mainloop()

if __name__ == '__main__':
    logInPage()