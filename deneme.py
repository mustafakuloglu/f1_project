from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from main import sinif



class App(Frame):
    def __init__(self, parent):
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        print(filename)
        Frame.__init__(self, parent)
        self.CreateUI()

        sinifa = sinif()
        asd = sinifa.getHtmlList(filename)
        self.LoadTable(asd)
        self.grid(sticky=(N, S, W, E))
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)


    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('pazartesi', 'sali', 'carsamba', 'persembe', 'cuma', 'cumartesi', 'pazar')
        tv.heading("#0", text='Saatler', anchor='w')
        tv.column("#0", anchor="center", width=80)
        tv.heading('pazartesi', text='Pazartesi')
        tv.column('pazartesi', anchor='center', width=180)
        tv.heading('sali', text='Salı')
        tv.column('sali', anchor='center', width=180)
        tv.heading('carsamba', text='Çarşamba')
        tv.column('carsamba', anchor='center', width=180)
        tv.heading('persembe', text='Perşembe')
        tv.column('persembe', anchor='center', width=180)
        tv.heading('cuma', text='Cuma')
        tv.column('cuma', anchor='center', width=180)
        tv.heading('cumartesi', text='Cumartesi')
        tv.column('cumartesi', anchor='center', width=180, )
        tv.heading('pazar', text='Pazar')
        tv.column('pazar', anchor='center', width=180)
        tv.grid(sticky=(N, S, W, E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def LoadTable(self, asd):
        a = 1
        while a < 17:

            self.treeview.insert('', 'end', text=asd[a][0],
                                 values=(str(asd[a][1])[2:-2], str(asd[a][2])[2:-2], str(asd[a][3])[2:-2], str(asd[a][4])[2:-2], str(asd[a][5])[2:-2], str(asd[a][6])[2:-2], str(asd[a][7])[2:-2]))
            a = a + 1


def main():
    root = Tk()
    App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
