import tkinter as tk
import webbrowser


class GUI:
    """Handles tasks involving GUI"""
    
    def __init__(self):
        self.links = {}
    
    
    def updateNewsList(self, news_list):
        """update the news_list"""

        for i in news_list:
            self.news_text.insert(tk.END, i["title"] + "\n", "hyperlink")
            self.links[i["title"]] = i["link"]
            self.news_text.insert(tk.END, "\n")

        

    
    def __openUrl(self, event):

        index = self.news_text.index(tk.CURRENT)

        start = index[:index.index(".")] + ".0"

        everything = self.news_text.get(start, tk.END)

        o = []
        for i in everything:
            if i == "\n":
                break

            o.append(i)
        
        full_link = self.links["".join(o)]

        webbrowser.open(full_link)


    def setup(self):
        """runs only at startup of program, creates widgets"""

        self.root = tk.Tk()
        self.root.title("The Latest News For You")

        self.root.rowconfigure(0, minsize=800, weight=1)
        self.root.columnconfigure(1, minsize=800, weight=1)

        self.ribbon = tk.Frame(relief=tk.RAISED, bd=3)

        self.news_text = tk.Text(font=("Arial", 10), cursor="hand2")
        self.news_text.tag_configure(tagName="hyperlink")
        self.news_text.tag_bind("hyperlink", "<Button-1>", self.__openUrl) #! needs work, convert mouse position of event by event.x and event.y to Text widget index (Use the code in ~/tests/tkinter_test.py). Then find some way to use that index to get the start idx and end idx of the whole str. Then use that in news_text.get() to get the url to be used by __openUrl()
        
        self.settings_button = tk.Button(self.ribbon, text="settings", command=self.__settingsPopup)
        
        self.settings_button.grid(row=0, column=0, sticky="ew", pady=5, padx=5)
        self.ribbon.grid(row=0, column=0, sticky="ns")
        self.news_text.grid(row=0, column=1, sticky="nsew")
        
    
    def __settingsPopup(self):
        """open new window on settings button click"""

        for k in self.root.children.copy().keys():
            if "!toplevel" in k:
                self.root.children[k].destroy()
                print(k, "destroyed")
         
        self.settingsPopup = tk.Toplevel(self.root)
        tk.Label(self.settingsPopup, text="bruh").pack()
        self.settingsPopup.mainloop()