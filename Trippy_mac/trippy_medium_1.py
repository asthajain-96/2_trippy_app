import tkinter
import cv2
import PIL.Image,	PIL.ImageTk
import time
import os


# Begin the app
class	App:
    def	__init__(self,	window,	window_title,	video_source=0):
        self.window	= window
        self.window.title(window_title)
        self.video_source =	video_source


        # Labels
        label1 = tkinter.Label(window,text="Filters")
        label1.grid(row=0,column=13, columnspan=5)

        label2 = tkinter.Label(window, text="Saving")
        label2.grid(row=8,column=13, columnspan=5)

        #	Create	a	canvas	that	can	fit	the	above	video	source	size
        self.canvas	= tkinter.Canvas(window, width = 600, height	= 400)
        self.canvas.grid(row=0, column=1, rowspan=15, columnspan=5)

        #	Button	that	lets	the	user	take	a	snapshot
        self.b_snap=tkinter.Button(window, text="Snapshot", width=50)#	command=self.snapshot)
        self.b_snap.grid(row=12, column=3, rowspan=7)

        # Button for applying the other filters!
        self.b1 = tkinter.Button(window, text="Gauss", width=15)# command=self.gauss_filter)
        self.b1.grid(row=1, column=13)

        self.b2 = tkinter.Button(window, text="Laplace", width=15)#, command=self.laplace_filter)
        self.b2.grid(row=1, column=17)

        self.b3 = tkinter.Button(window, text="Delta", width=15)#,  command=self.delta_filter)
        self.b3.grid(row=3, column=13)

        self.b3_2 = tkinter.Button(window,text="Delta +", width = 10)#, command=self.delta_filter_plus)
        self.b3_2.grid(row=4, column=13)

        self.b4 = tkinter.Button(window, text="Threshold", width=15)#, command=self.threshold_filter)
        self.b4.grid(row=3, column=17)

        # note, sobel filters use the same button, multiple clicks
        self.b5 = tkinter.Button(window, text="Sobel-x, y, xy", width=15)#, command=self.sobel_filter)
        self.b5.grid(row=5, column=13)

        self.b6 = tkinter.Button(window, text="I'm Blue!", width = 15)#, command = self.blue_filter)
        self.b6.grid(row=5, column= 17)

        self.b7 = tkinter.Button(window, text="Gray", width=15)#, command=self.gray_filter)
        self.b7.grid(row=7, column=13)

        self.b8 = tkinter.Button(window, text="Color/No Filter", width=15)#, command=self.no_filter)
        self.b8.grid(row=7, column=17)

        self.b9 = tkinter.Button(window, text="Snap Dat!")#,command=self.snapshot)
        self.b9.grid(row=9, rowspan=2, column = 13, columnspan=4)

        self.b10= tkinter.Button(window, text="Close Program")#,  command=window.destroy)
        self.b10.grid(row=9, rowspan=2, column=17, columnspan=2)

        #	After	it	is	called	once,	the	update	method	will	be	automatically	called	every loop

        self.window.mainloop()


App(tkinter.Tk(), 'Trippy')
