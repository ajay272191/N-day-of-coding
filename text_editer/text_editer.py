from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()

# Title of Text editor window
root.title("Sarthi's space")

# Setting up default window size
root.geometry('1000x600')

# status of current opened file
global open_status_name
open_status_name = False


# To create a new file
def new_file():
    #delete previus text
    my_text.delete("1.0", END)

    #upadte status bar
    root.title('New file text file')
    status_bar.config(text="New File...")

    global open_status_name
    open_status_name = False


# opening new file
def open_file():
    #delete previus text
    my_text.delete("1.0", END)

    #grab filename
    text_file = filedialog.askopenfilename(initialdir='', title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.y"), ("All Files", "*.*")))

    #check if file get seleceted
    if text_file:
        # making filename global so we can access it later
        global open_status_name
        open_status_name = text_file

    #update satus bar
    name = text_file
    status_bar.config(text=f'{name}        ')
    # name = name.replace("","")
    root.title(f'{name}')

    #open fileids
    text_file = open(text_file, 'r')
    stuff = text_file.read()

    #add file to text file
    my_text.insert(END, stuff)

    #close the text file
    text_file.close()


# saving file with desired filename
def save_as_file():
    from tkinter.filedialog import asksaveasfilename
    global text_file
    text_file = asksaveasfilename()
    open_status_name = text_file
    if text_file:
        #save the file
        f = open(text_file, 'a')
        f.write(my_text.get(1.0, END))
        status_bar.config(text=f'{text_file} :saved       ')
        #close the file
        f.close()


# Saving file
def save_file():
    global open_status_name
    # open_status_name = text_file
    if open_status_name:
        #save the file
        f = open(open_status_name, 'w')
        f.write(my_text.get(1.0, END))
        #status update and popup code
        status_bar.config(text=f'{open_status_name} :saved       ')
        #close the file
        f.close()
    else:
        save_as_file()


#create main frame
my_frame = Frame(root)
my_frame.pack(pady = 5)

#create scrollbar for text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#create Text Box
my_text = Text(my_frame, width = 97, height = 25, font=("Helvetica", 16), selectbackground="Yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

#create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add file Menu
file_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#add edit menu
edit_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

#add status bar to bottom of app
status_bar = Label(root, text="Ready        ", anchor=E)#east = E
status_bar.pack(fill=X, side=BOTTOM, ipady=5 )

#configure scrollbar
text_scroll.config(command=my_text.yview)
root.mainloop()
