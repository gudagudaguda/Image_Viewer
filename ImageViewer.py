from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.filename=Label(root)
myLabel=Label(root)
myLabel.grid(row=0, column=0, columnspan=3)

def resize(img):
	width = img.size[0]
	height = img.size[1]
	if img.size[1]>700:		
		img = img.resize((int(700*width/height),700), Image.ANTIALIAS)
		width = img.size[0]
		height = img.size[1]	
	if  img.size[0]>1920:
		img = img.resize((1600,int(1600*height/width)), Image.ANTIALIAS)
	ImageList.append(ImageTk.PhotoImage(img))

def load(num):
	img = Image.open(root.filename[num])
	resize(img)

def printImg(num):
	global myLabel
	myLabel.config(image=ImageList[num])
	status = Label(root,text="Image "+str(num+1)+" of "+str(len(root.filename))+"	", bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2,column=0,columnspan=3, sticky=W+E)

def inibutton():
	global button_forward
	global button_back
	button_back = Button(root, text="<<", state=DISABLED)
	button_exit = Button(root, text="OPEN", bg='#d97b7b', command=openfiles)
	button_forward = Button(root, text=">>", command=lambda:forward(1))
	if len(root.filename)==1:
		button_forward.config(state=DISABLED)

	button_back.grid(row=1, column=0)
	button_exit.grid(row=1, column=1)
	button_forward.grid(row=1, column=2)

def forward(num):
	if len(ImageList)<num+1:
		load(num)
	printImg(num)
	button_forward.config(command=lambda:forward(num+1))
	button_back.config(command=lambda:back(num-1), state=NORMAL)
	if num == (len(root.filename)-1):
		button_forward.config(state=DISABLED)

def back(num):
	printImg(num)
	button_forward.config(command=lambda:forward(num+1), state=NORMAL)
	button_back.config(command=lambda:back(num-1))
	if num == 0:
		button_back.config(state=DISABLED)
		
def openfiles():
	if root.filename:
		backup = root.filename
	del root.filename
	root.filename = filedialog.askopenfilenames(initialdir="/home/ruka/Anime&Manga", title="Select file", filetypes=(("all file",".*"), ("webp file",".webp"),("jpg file",".jpg"),("png file",".png")))
	if not root.filename:
		exitComfirm = messagebox.askyesno("Exit the Programme?","You didn't choose any file. Exit the programme?")
		if exitComfirm == 1:
			quit()
		else:
			root.filename = backup
	else:
		global ImageList
		ImageList=[]
		load(0)
		printImg(0)
		inibutton()

openfiles()
root.mainloop()