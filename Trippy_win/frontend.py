'''
Front end for bookStore program:
Requirements:
1) show list of current rrecors
2) Search for an entry
3) update database
4) delete selected
5) Close
6) have spaces to input all categories (title, author, year, isbn)

'''
#import backend
from tkinter import *
from tkinter import messagebox
import cv2

video = cv2.VideoCapture(0) # use default camera
frame1 = None
if frame1 is None:
    check, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame1 = gray
    video.release()
    cv2.destroyAllWindows()
cv2.imshow('my frame', frame1)
cv2.

input('wait here')

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()
        selected_tuple = list1.get(index)
        # Display current selection on top
        for idx, entry in enumerate([entry1, entry2, entry3, entry4]):
            entry.delete(0,END)
            entry.insert(END, selected_tuple[idx+1])
        print(selected_tuple)
    except:
        pass


def view_command():
    list1.delete(0,END)
    for idx, entry in enumerate([entry1, entry2, entry3, entry4]):
        entry.delete(0,END)

    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(e_title.get(),e_author.get(),e_year.get(), e_isbn.get()):
        list1.insert(END,row)

# using the insert() function
def add_entry():
    list1.delete(0,END)
    backend.insert(title=e_title.get(), author=e_author.get(), year=e_year.get(), isbn=e_isbn.get())
    view_command()
    messagebox.showinfo("Bookstore Change", f"You added {e_title.get()} to the bookstore!")

# use the get_selected_row and retrieve index '0' which is the ID. Pass that to backend
def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0], title=e_title.get(), author=e_author.get(), year=e_year.get(), isbn=e_isbn.get())
    view_command()


###
window = Tk()


# First function - use buttons
window.wm_title("Trippy")

## Will have buttons!
b1 = Button(window, text="Gauss", width=15) #,command=gauss_filter)
b1.grid(row=3, column=13)

b2 = Button(window, text="Laplace", width=15)#, command=laplace_filter)
b2.grid(row=3, column=17)

b3 = Button(window, text="Delta", width=15)#,  command=delta_filter)
b3.grid(row=6, column=13)

b4 = Button(window, text="Threshold", width=15)#, command=threshold_filter)
b4.grid(row=6, column=17)

# note, add sobel filters to the same button, multiple clicks
b5 = Button(window, text="Sobel-x, y, xy", width=15)#,command=sobelx_filter)
b5.grid(row=9, column=13)

b6 = Button(window, text="Snap Picture!", width = 15)#, command = snap_picture)
b6.grid(row=9, column= 17)

b7 = Button(window, text="Close", width=10, command=window.destroy)
b7.grid(row=11, column=5)
'''
## Will have Labels boxes
label1 = Label(window,text="Title")
label1.grid(row=0,column=0)

label2 = Label(window, text="Author")
label2.grid(row=0,column=2)

label3 = Label(window,text="Year")
label3.grid(row=1,column=0)

label4 = Label(window, text="ISBN")
label4.grid(row=1,column=2)

## Will take entry values!
e_title = StringVar()
entry1 = Entry(window, textvariable=e_title)
entry1.grid(row=0,column=1)

e_author = StringVar()
entry2 = Entry(window, textvariable=e_author)
entry2.grid(row=0,column=3)

e_year = StringVar()
entry3 = Entry(window, textvariable=e_year)
entry3.grid(row=1,column=1)

e_isbn = StringVar()
entry4 = Entry(window, textvariable=e_isbn)
entry4.grid(row=1,column=3)
'''
## Create a canvas to display the video
canvas = Canvas(window, width=640,height=480)
canvas.grid(row=1, rowspan=10, column=1, columnspan=10)
canvas.create_image(0,0, image=frame1)
#list1 = Listbox(window, height=10, width=50)
#list1.grid(row=20, rowspan=6, column=0, columnspan=2)

# Create a scrollbar. Attach it to the window, and then tell it which widget to scroll
sb1 = Scrollbar(window)
sb1.grid(row=2, column=13, columnspan=7)

# configure list and scrollbar to affect each other:
canvas.configure(xscrollcommand=sb1.set)
sb1.configure(command=canvas.xview)

# Add method to select id by clicking on an item in the listbox. This needs an
#     extra function called get_selected_row that returns the selected tuple
canvas.bind('<<ListboxSelect>>', get_selected_row)


window.mainloop()
