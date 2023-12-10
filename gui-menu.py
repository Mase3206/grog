import tkinter
from tkinter import ttk


# start automated transcode




# initialize the window
root = tkinter.Tk()


# add a label widget
root.title('HandBrake Auto Transcode')
# set window size
root.geometry('400x300')





try:
    # this code prevents the text from becoming blurry on windows
	# it will fail on non-windows devices, so it's in a `try` statement
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
	# show the window by running .mainloop()
    root.mainloop()

