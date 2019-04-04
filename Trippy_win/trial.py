
import cv2
import tkinter
from tkinter import *
import PIL.Image, PIL.ImageTk


video = cv2.VideoCapture(0)
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

frame1 = None
if frame1 is None:
    check, frame1 = video.read()

    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    video.release()
    cv2.destroyAllWindows()

#cv2.imshow('frame1', frame1)
#key = cv2.waitKey(0)
#cv2.imwrite('first frame.jpg', frame1)

window = tkinter.Tk()

canvas = tkinter.Canvas(window, width=width, height=height)
canvas.grid(row=1, column=1, rowspan=10, columnspan=10)

# convert from numpy array to photo using pillow (PIL.ImageTk.PhotoImage)
photo1 = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame1))
canvas.create_image(0,0, image=photo1, anchor=tkinter.NW)

# buttons
## Will have buttons!
## Will have buttons!
b1 = Button(window, text="Gauss", width=15) #,command=gauss_filter)
b1.grid(row=1, column=13)

b2 = Button(window, text="Laplace", width=15)#, command=laplace_filter)
b2.grid(row=1, column=17)

b3 = Button(window, text="Delta", width=15)#,  command=delta_filter)
b3.grid(row=3, column=13)

b4 = Button(window, text="Threshold", width=15)#, command=threshold_filter)
b4.grid(row=3, column=17)

# note, add sobel filters to the same button, multiple clicks
b5 = Button(window, text="Sobel-x, y, xy", width=15)#,command=sobelx_filter)
b5.grid(row=5, column=13)

b6 = Button(window, text="Snap Picture!", width = 15)#, command = snap_picture)
b6.grid(row=5, column= 17)

b7 = Button(window, text="Gray", width=15)#, command=window.destroy)
b7.grid(row=7, column=13)

b8 = Button(window, text="Reset View", width=15)#, command=reset)
b8.grid(row=7, column=17)

b9 = Button(window, text="Snap Dat!", width = 15)
b9.grid(row=9, rowspan=2, column = 13, columnspan=4)

b10= Button(window, text="Close Program", width=15, command=window.destroy)
b10.grid(row=9, rowspan=2, column=17, columnspan=2)

sb1 = Scrollbar(window, orient='horizontal')
sb1.grid(row=12, column=1, columnspan=8)


canvas.configure(xscrollcommand=sb1.set)





window.mainloop()
