import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import mysql.connector
import menuPage

class EventPage:
    def __init__(self, window):
        self.window = window
        self.window.title('Event Page')
        self.window.geometry('1600x700')
        self.window.configure(bg="#262626")
        self.window.resizable(0,0)
        #self.window.state('zoomed')
        
        # ================= BEFORE TRYING OUT CODE ON A PERSONAL PC, PLEASE CHANGE THE DATA BELLOW ACCORDING TO YOUR DATABASE'S INFORMATION FOR mysql.connector LINE ==========================
        hostData = "localhost"
        userData = "root"
        passwordData = "s4nsSQLch3n$o"
        databaseData = "eveo"

        # ------------------- AUTO-WRITE the row data into input box --------------------
        # --- after user double clicks (see line 171 or " listBox.bind('<Double-Button-1>', GetValue) "), it copies and pastes the selected row into the input box ------------
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
            e8.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0,select['Event ID'])
            e2.insert(0,select['Event Name'])
            e3.insert(0,select['Organizer ID'])
            e4.insert(0,select['Event Start'])
            e5.insert(0,select['Event End'])
            e6.insert(0,select['Venues'])
            e7.insert(0,select['Total Capacity'])
            e8.insert(0,select['Total Sales'])

        def clearBox():
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
            e8.delete(0, END)

        #------------ def add() INSERTS new data into the column

        def add():
            eventID = e1.get() # get the input 
            eventName = e2.get()
            organID = e3.get()
            eventStart = e4.get()
            eventEnd = e5.get()
            venNum = e6.get()
            capTotal = e7.get()
            saleTotal = e8.get()
            mysqldb = mysql.connector.connect(host = hostData, user = userData, password = passwordData, database = databaseData) # connect the database
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  event (EventId, EventName, OrganizerId, EventStart, EventEnd, Venues, TotalCapacity, TotalSales) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (eventID, eventName, organID, eventStart, eventEnd, venNum, capTotal, saleTotal)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("Information", "Event inserted successfully...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)
                e7.delete(0, END)
                e8.delete(0, END)
                e1.focus_set()
                
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
                messagebox.showinfo("Information", "Invalid input, please try again.")


        #---------- def update() UPDATES the existing data in a column after selecting the desired row--------------

        def update():
            eventID = e1.get()
            eventName = e2.get()
            organID = e3.get()
            eventStart = e4.get()
            eventEnd = e5.get()
            venNum = e6.get()
            capTotal = e7.get()
            saleTotal = e8.get()
            mysqldb=mysql.connector.connect(host=hostData,user=userData,password=passwordData,database=databaseData)
            mycursor=mysqldb.cursor()
        
            try:
                sql = "Update event set EventName = %s, OrganizerId = %s, EventStart = %s, EventEnd = %s, Venues = %s, TotalCapacity = %s, TotalSales = %s where EventId = %s"
                val = (eventName, organID, eventStart, eventEnd, venNum, capTotal, saleTotal, eventID)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("Information", "Record Updated successfully...")
            
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)
                e7.delete(0, END)
                e8.delete(0, END)
                e1.focus_set()
                
        
            except Exception as e:
        
                print(e)
                mysqldb.rollback()
                mysqldb.close()
                messagebox.showinfo("Information", "Invalid input, please try again.")


        # --------------- def delete() DELETES the selected row of data ------------------


        def delete():
            eventID = e1.get()
            eventName = e2.get()
            organID = e3.get()
            eventStart = e4.get()
            eventEnd = e5.get()
            venNum = e6.get()
            capTotal = e7.get()
            saleTotal = e8.get()
            mysqldb=mysql.connector.connect(host=hostData,user=userData,password=passwordData,database=databaseData)
            mycursor=mysqldb.cursor()
        
            try:
                sql = "delete from event where EventId = %s"
                val = (eventID,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("Information", "Record Deleted successfully...")
            
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)
                e7.delete(0, END)
                e8.delete(0, END)
                e1.focus_set()
            
            except Exception as e:
            
                print(e)
                mysqldb.rollback()
                mysqldb.close()
                messagebox.showinfo("Information", "Invalid input, please try again.")


        #----------- def show() only DISPLAYS the available data from the column [specified in code] into the column/row box in the UI -----------------------

        def show():
                mysqldb = mysql.connector.connect(host=hostData, user=userData, password=passwordData, database=databaseData)
                mycursor = mysqldb.cursor()
                mycursor.execute("SELECT EventId, EventName, OrganizerId, EventStart, EventEnd, Venues, TotalCapacity, TotalSales FROM event")
                records = mycursor.fetchall()
                print(records)

                for i, (eventID, eventName, organID, eventStart, eventEnd, venNum, capTotal, saleTotal) in enumerate(records, start=1):
                    listBox.insert("", "end", values=(eventID, eventName, organID, eventStart, eventEnd, venNum, capTotal, saleTotal))
                    mysqldb.close()

        #-------- function to move to main menu
        def go_pageMenu(): 
            win = Toplevel()
            menuPage.MenuPage(win)
            self.window.withdraw()
            win.deiconify()
            #self.window.destroy()

        #------- function to refresh page
        def refreshing():
            self.window.destroy()
            if __name__ == '__main__':
                eventPage()

 
        # ========================== UI ====================================================


        e1 = ''
        e2 = ''
        e3 = ''
        e4 = ''
        e5 = ''
        e6 = ''
        e7 = ''
        e8 = ''

        # ------------- set up labels ----------------
        tk.Label(self.window, text = "Event Record", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 30, 'bold')).place(x = 80, y = 80)
        
        tk.Label(self.window, text = "Double-click on a desired row to automatically fill the text boxes.",
                 fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 12)).place(x = 80, y = 140)

        tk.Label(self.window, text = "Event ID", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 11)).place(x=80, y=240)
        Label(self.window, text =  "Event Name", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 11)).place(x = 80, y = 280)
        Label(self.window, text =  "Organizer ID", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 11)).place(x = 80, y = 320)
        Label(self.window, text =  "Event Start", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 11)).place(x = 80, y = 360)
        Label(self.window, text =  "Event End", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 11)).place(x = 80, y = 400)
        Label(self.window, text =  "Venues", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 11)).place(x = 80, y = 440)
        Label(self.window, text =  "Total Capacity", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 11)).place(x = 80, y = 480)
        Label(self.window, text =  "Total Sales", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 11)).place(x = 80, y = 520)

        # ---------- set up the input box ----------------
        
        # -------------------------
        e1 = Entry(self.window, width = 61, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e1.place(x = 210, y = 240)
        Frame(self.window, width=491, height=2, bg='white').place(x=210, y=265)

        # -------------------------
        e2 = Entry(self.window, width = 61, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e2.place(x = 210, y = 280)
        Frame(self.window, width=491, height=2, bg='white').place(x=210, y=305)

        # -------------------------
        e3 = Entry(self.window, width = 61, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e3.place(x = 210, y = 320)
        Frame(self.window, width=491, height=2, bg='white').place(x=210, y=345)

        # -------------------------
        e4 = Entry(self.window, width = 61, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e4.place(x = 210, y = 360)
        Frame(self.window, width=491, height=2, bg='white').place(x=210, y=385)

        # -------------------------
        e5 = Entry(self.window, width = 61, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e5.place(x = 210, y = 400)
        Frame(self.window, width=491, height=2, bg='white').place(x=210, y=425)

        # -------------------------
        e6 = Entry(self.window, width = 61, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e6.place(x = 210, y = 440)
        Frame(self.window, width=491, height=2, bg='white').place(x=210, y=465)
        
        # -------------------------
        e7 = Entry(self.window, width = 61, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e7.place(x = 210, y = 480)
        Frame(self.window, width=491, height=2, bg='white').place(x=210, y=505)

        # -------------------------
        e8 = Entry(self.window, width = 61, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e8.place(x = 210, y = 520)
        Frame(self.window, width=491, height=2, bg='white').place(x=210, y=542)

        #----------- buttons set up ----------------------
        Button(self.window, text = "Add", command = add, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 9)).place(x=900, y = 420)
        Button(self.window, text = "Update", command = update, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 9)).place(x=900, y = 470)
        Button(self.window, text = "Delete", command = delete, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 9)).place(x=900, y = 520)
        Button(self.window, text = "Refresh Page", command = refreshing, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 9)).place(x=900, y = 570)
        Button(self.window, text = "Main Menu", command = go_pageMenu, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 9)).place(x=900, y = 620)

        Button(self.window, text = "Clear", command = clearBox, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 9)).place(x=80, y = 620)


        # ------------------set up the columns/rows box in the UI ---------------------------


        cols = ('Event ID', 'Event Name', 'Organizer ID', 'Event Start', 'Event End', 'Venues', 'Total Capacity', 'Total Sales')
        listBox = ttk.Treeview(self.window, columns = cols, show = 'headings')



        #------ editing the look ------
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', 
                        background = '#454545', 
                        foreground = '#F8F8FF',
                        relief = 'flat', 
                        rowheight = 25,
                        highlightcolor = '#404040',
                        fieldbackground = '#454545',
                        font = ('Microsoft Yahei UI Light', 11),
                        
                        )
        style.configure('Treeview.Heading',
                        background = '#454545',
                        foreground = '#F8F8FF',
                        font = ('Microsoft Yahei UI Light', 11),
                        relief = 'flat'
                        )

        style.map('Treeview',
                    background=[('selected', '#808080')]
                    )
        style.map("Treeview.Heading",
                    background = [('active', '#545454')]
                )

        # style.configure('Vertical.Tscrollbar', 
        #         background = 'black',
        #         bordercolor = 'red',
        #         arrowcolor = 'white'
        #         )

        #------ scrollbar --------
        scrollbarx = Scrollbar(self.window, orient = HORIZONTAL)
        scrollbary = Scrollbar(self.window, orient = VERTICAL)
        listBox.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        listBox.configure(selectmode="extended")

        scrollbarx.configure(command=listBox.xview)
        scrollbary.configure(command=listBox.yview)

        scrollbarx.place(relx=0.563, rely=0.519, width=600, height=22)
        scrollbary.place(relx=0.939, rely=0.114, width=22, height=304)


        for col in cols:
            listBox.heading(col, text = col)
            listBox.grid(row = 1, column = 3, columnspan = 3, padx=5, pady=5, sticky='nsew')
            listBox.place(relx=0.563, rely=0.114, width=602, height=284)


        # --- run show() ------
        show()
        listBox.bind('<Double-Button-1>', GetValue) # double click one of the rows in the column/row box in UI, run GetValue


def eventPage():
    window = Tk()
    EventPage(window)
    window.mainloop()

if __name__ == '__main__':
    eventPage()