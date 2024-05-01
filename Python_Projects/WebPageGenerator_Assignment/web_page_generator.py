import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=1, pady=(20,15))
        
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.get_data)
        self.btn.grid(row=2, column=2, padx=(20, 20), pady=(20,15))

        self.lbl = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.lbl.grid(row=0, column=0, padx=(20, 20), pady=(30, 0))
        self.txtEntry = Entry(width=75)
        self.txtEntry.grid(row=1, column=0, columnspan=3, padx=(20, 20), pady=(30, 20), sticky=('we'))
        
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing winter sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def get_data(self):
        htmlText = self.txtEntry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
