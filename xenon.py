from npyscreen import *
import npyscreen
import sys
import os




npyscreen.disableColor()






class Xenon(NPSApp):
    def __init__(self):
            self.filepath = ""
    def main(self):
        F  = FormBaseNewWithMenus(name ="Xenon v0.0.1")
        npyscreen.blank_terminal()
        t  = F.add(TitleFixedText, name = f"FILE : {self.filepath}", )

        self.menu = F.add_menu(name="Menu")
        self.menu.addItem("Exit Program", self.exit, "^E")
        self.menu.addItem("Save file", self.savefile, "^S")
        self.menu.addItem("Save file & Exit", self.savefileandexit, "^Q")

        with open(self.filepath, "r+") as fp:
            self.file_cnt = fp.read()
            fp.close()
        self.ml = F.add(MultiLineEdit, 
               value = self.file_cnt)
        F.edit()
        
    def exit(self):
        sys.exit(0)
    
    def savefile(self):
        with open(self.filepath, "r+") as fp:
            self.file_cnt = self.ml.value
            fp.write(self.file_cnt)
            fp.close()

    def savefileandexit(self):
        self.savefile()
        self.exit()
        


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file = sys.argv[1]
        if os.path.isfile(file) == True:
            App = Xenon()
            App.filepath = file
            App.run()  
        else:
            print("Error : Path doesn't exist")
