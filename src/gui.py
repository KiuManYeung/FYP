import tkinter as tk
# from PIL import Image, ImageTk
from os import listdir
from os.path import isfile, join

img_path = "./png"

onlyfiles = [f for f in listdir(img_path) if isfile(join(img_path, f))]

index = 0

def next_img():
    global index
    if index < len(onlyfiles)-1:
        index += 1
        print(index)
        img = tk.PhotoImage(file=img_path+"/"+onlyfiles[index])
        lbl_right.configure(image=img)
        lbl_right.image=img

def previous_img():
    global index
    if index > 0:
        index -= 1
        print(index)
        img = tk.PhotoImage(file=img_path+"/"+onlyfiles[index])
        lbl_right.configure(image=img)
        lbl_right.image=img

window = tk.Tk()
window.minsize(1000,500)

window.columnconfigure(0, weight=1, minsize=500)
window.columnconfigure(1, weight=1, minsize=500)
window.rowconfigure(0, weight=1, minsize=500)

frm_left = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frm_left.grid(row=0,column=0, sticky="nswe")

frm_right = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frm_right.grid(row=0,column=1, sticky="nswe")

frm_left.columnconfigure(0, weight=1, minsize=250)
frm_left.columnconfigure(1, weight=1, minsize=250)
frm_left.rowconfigure(0, weight=1, minsize=470)
frm_left.rowconfigure(1, weight=0, minsize=30)

txt_edit = tk.Text(master=frm_left)
txt_edit.grid(row=0, column=0, columnspan=2, sticky="nsew")

btn_previous = tk.Button(master=frm_left, text="Previous", height=2, command=previous_img)
btn_next = tk.Button(master=frm_left, text="Next", height=2, command=next_img)
btn_previous.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
btn_next.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)


# lbl_right = tk.Label(master=frm_right, text="I'm in Frame Right")
# lbl_right.pack()

# c = tk.Canvas(frm_right, bg="white")
# c.create_polygon([30.6667, 5.3333, 5.3333, 5.3333, 5.3333, 45.3333, 30.6667, 45.3333], fill="white", width=0.5, outline="black", tags="1node0x1b27db79dc0")
# c.create_polygon([7.3333, 22.6667, 7.3333, 6.6667, 30, 6.6667, 30, 22.6667], fill="#fefecd", width=1, tags="0node0x1b27db79dc0")
# c.create_line([7.3333, 22.6667, 30, 22.6667], fill="black", tags="0node0x1b27db79dc0")
# c.create_text(14.6667, 15.05, text="0", fill="#444443", font="Helvetica 9", anchor="w", tags="0node0x1b27db79dc0")
# c.create_polygon([7.3333, 44, 7.3333, 22.6667, 30, 22.6667, 30, 44], fill="#fefecd", width=1, tags="0node0x1b27db79dc0")
# c.create_text(10, 33.95, text="'hi'", fill="#444443", font="Helvetica 11", anchor="w", tags="0node0x1b27db79dc0")
# c.pack(fill="both", expand=True)


# img has to be declared separately
img=tk.PhotoImage(file=img_path+"/"+onlyfiles[0])
lbl_right = tk.Label(frm_right,image=img)
lbl_right.pack()



window.state('zoomed')
window.mainloop()