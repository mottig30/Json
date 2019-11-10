import os,json
import tkinter as JsonFinder
from tkinter import filedialog

def getFolder():
    fileSecond = filedialog.askdirectory()
    fileSecond = str(fileSecond)
    entryFolder.insert(0,fileSecond)

def getFile1(flag):
    if flag == 1:
        fileOne = filedialog.askopenfile()
        fileOne = str(fileOne.name)
        entryFile1.insert(0,fileOne)
    elif flag == 0:
        return entryFile1.get()

def getFile2(flag):
   if flag == 1: 
       fileSecond = filedialog.askopenfile()
       fileSecond = str(fileSecond.name)
       entryFile2.insert(0,fileSecond)
   elif flag == 0:
         return entryFile2.get()

def clear(label,but):
    label.destroy()
    but.destroy()
    
def getKeys(data,ans):
  for k,v in data.items():
       if  isinstance(v,list):
          ans.append(k) 
          for item in v:
              getKeys(item,ans)
       elif not isinstance(v,list):
               ans.append(k)
               
               
def compare():
    if len(entryFile2.get())==0 or len(entryFile1.get())==0:
        JsonFinder.messagebox.showinfo("Error","One or more of the filds is missing")
    else:
        
      with open(getFile1(0),'r',errors='ignore') as t1:
          data1 = json.load(t1)
      with open(getFile2(0),'r',errors='ignore') as t2:
          data2 = json.load(t2)
      list1=[]   
      list2=[]
      getKeys(data1,list1)
      getKeys(data2,list2)
      ans=[]
      for i in list1:
          if i not in list2:
              ans.append(i)
      label3=JsonFinder.Entry(framehead2,text=str(ans))
      label3.place(relx=0,rely=0.7,relwidth=1,relheight=0.1)
      label3.insert(0,str(ans))
    
      buttonClearData = JsonFinder.Button(framehead2, text="clear", bg="#a6bab9",command=lambda:clear(label3,buttonClearData))
      buttonClearData.place(relx=0.79,rely=0.8,relwidth=0.2,relheight=0.1)
    


        
window=JsonFinder.Tk()
HEIGHT=800
WIDTH=800
canvas = JsonFinder.Canvas(window, height=HEIGHT,width=WIDTH)
canvas.pack()
dir_path = os.path.dirname(os.path.realpath(__file__))

def run(entry,path):
     counter=0
     dir_path = entryFolder.get()+"/"
     if len(entryFolder.get())==0 or len(entry) ==0 :
         JsonFinder.messagebox.showinfo("Error","One or more of the filds is missing")
         
     if len(entryFolder.get())!=0 and len(entry) !=0 :
         for filename in os.listdir(dir_path):
             if filename.endswith(".json"):
                 ans=openJson(dir_path+filename,entry)
                 if ans!=-1:
                     counter=counter+1                  
                     label2=JsonFinder.Entry(frameFinder)
                     label2.place(relx=0,rely=0.7,relwidth=1,relheight=0.1)
                     label2.insert(0,"your key word found here: "+filename)
                    
                     buttonClear = JsonFinder.Button(frameFinder, text="clear", bg="#a6bab9",command=lambda:clear(label2,buttonClear))
                     buttonClear.place(relx=0.79,rely=0.8,relwidth=0.2,relheight=0.1)
                     break
     if counter == 0 and len(entryFolder.get())!=0 and len(entry) !=0:
         label10=JsonFinder.Label(frameFinder,text="your key word is not found")
         label10.place(relx=0,rely=0.5,relwidth=1,relheight=0.3)
                  
         buttonClear10 = JsonFinder.Button(frameFinder, text="clear", bg="#a6bab9",command=lambda:clear(label10,buttonClear10))
         buttonClear10.place(relx=0.79,rely=0.8,relwidth=0.2,relheight=0.1)
            
                  
def openJson(fname,search):
          with open(fname,'r',errors='ignore') as f:
              data = json.load(f)
              str1=json.dumps(data)
              return str1.find(search)
          

frameTopLeft = JsonFinder.Frame(window)
frameTopLeft.place(relx=0.3,rely=0.05,relwidth=0.2,relheight=0.05)

frameButtom = JsonFinder.Frame(window)
frameButtom.place(relx=0.13,rely=0.2,relwidth=0.5,relheight=0.2)

frameTop = JsonFinder.Frame(window)
frameTop.place(relx=0.25,rely=0.001,relwidth=0.5,relheight=0.05)

frameFinderHeadline = JsonFinder.Frame(window)
frameFinderHeadline.place(relx=0,rely=0.1,relwidth=0.7,relheight=0.05)

frameComparerHeadline = JsonFinder.Frame(window)
frameComparerHeadline.place(relx=0,rely=0.52,relwidth=0.7,relheight=0.05)

frameFinder = JsonFinder.Frame(window,highlightbackground="#11cbcf",highlightcolor="#11cbcf",highlightthickness="1")
frameFinder.place(relx=0,rely=0.17,relwidth=1,relheight=0.3)

framehead2 = JsonFinder.Frame(window,highlightbackground="#11cbcf",highlightcolor="#11cbcf",highlightthickness="1")
framehead2.place(relx=0,rely=0.6,relwidth=1,relheight=0.3)

headlinefinder = JsonFinder.Label(frameFinderHeadline, text="JSON Finder", font=("calibri", 20))
headlinefinder.place(relx=0.1,rely=0.1,relwidth=0.5,relheight=0.8)

headlinecomparer = JsonFinder.Label(frameComparerHeadline, text="JSON Comparer", font=("calibri", 20))
headlinecomparer.place(relx=0.1,rely=0.1,relwidth=0.5,relheight=0.8)


headline = JsonFinder.Label(frameTop, text="JSON Helper 1.1", font=("Helvetica", 30),foreground="#11cbcf")
headline.pack()


entry = JsonFinder.Entry(frameFinder, bg="white")
entry.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.1)

label=JsonFinder.Label(frameFinder,text="Insert your word")
label.place(relx=0,rely=0.3,relwidth=0.2,relheight=0.1)

labelFolder=JsonFinder.Label(frameFinder,text="Insert your Folder")
labelFolder.place(relx=0,rely=0.1,relwidth=0.2,relheight=0.1)

entryFolder = JsonFinder.Entry(frameFinder, bg="white")
entryFolder.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.1)

labelFolder=JsonFinder.Button(frameFinder,text="Upload Folder", bg="#a6bab9",command=lambda:getFolder())
labelFolder.place(relx=0.79,rely=0.1,relwidth=0.2,relheight=0.1)

button = JsonFinder.Button(frameFinder, text="Find", bg="#a6bab9",command=lambda:run(entry.get(),entryFolder.get()))
button.place(relx=0.79,rely=0.3,relwidth=0.2,relheight=0.1)

button3 = JsonFinder.Button(framehead2, text="compare", bg="#a6bab9",command=lambda:compare())
button3.place(relx=0,rely=0.5,relwidth=1,relheight=0.1)

labelUploader1=JsonFinder.Label(framehead2,text="Upload file 1")
labelUploader1.place(relx=0,rely=0.1,relwidth=0.2,relheight=0.1)

entryFile1 = JsonFinder.Entry(framehead2, bg="white")
entryFile1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.1)

butFile1=JsonFinder.Button(framehead2,text="Upload", bg="#a6bab9",command=lambda:getFile1(1))
butFile1.place(relx=0.79,rely=0.1,relwidth=0.2,relheight=0.1)

entryFile2 = JsonFinder.Entry(framehead2, bg="white")
entryFile2.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.1)

labelUploader2=JsonFinder.Label(framehead2,text="Upload File 2")
labelUploader2.place(relx=0,rely=0.3,relwidth=0.2,relheight=0.1)

butFile2 = JsonFinder.Button(framehead2, text="Upload", bg="#a6bab9",command=lambda:getFile2(1))
butFile2.place(relx=0.79,rely=0.3,relwidth=0.2,relheight=0.1)

window.mainloop()


