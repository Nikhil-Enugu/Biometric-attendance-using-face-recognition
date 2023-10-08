from tkinter import *
from openpyxl import workbook,load_workbook
from datetime import datetime
import cv2
import face_recognition
from PIL import Image,ImageTk
import os
import numpy
import time
root=Tk()
root.geometry("1920x1080")
var=StringVar()
var.set("Please Show your QR")
title=Label(root,textvariable=var,font=("Arial",45)).place(x=520,y=45)
L1=Label()
L1.place(x=450,y=140)
def markattendance(name):
    wb=load_workbook('attendance.xlsx') #loading excel sheet
    ws=wb.active
    now=datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    ws.append([name,time])
    wb.save('attendance.xlsx') #marking attendance and saving excel sheet named 'attendance.xlsx
def find_encodings(id):
    path='faces'
    mylist=os.listdir(path) #path where the user faces are available
    data={}
    id=id+".jpg"
    curimg=cv2.imread(f'{path}/{id}') #loading the image
    if(curimg is None):
        return curimg #If image is not found return None so that qr is not valid
    curimg = cv2.cvtColor(curimg,cv2.COLOR_BGR2RGB)
    return face_recognition.face_encodings(curimg) #returns face encodings of person with id 'id'
cap=cv2.VideoCapture(0)
while(True):
    qrdecode=''
    while(qrdecode==''): #runs until qr is captured
        suc,qr=cap.read()
        det=cv2.QRCodeDetector()
        val,b,c=det.detectAndDecode(qr)
        img=cv2.cvtColor(qr,cv2.COLOR_BGR2RGB)
        img=ImageTk.PhotoImage(Image.fromarray(img))
        L1['image']=img
        root.update()
        qrdecode=val #updates value if qr is decoded
    time.sleep(1)
    unknown_face_encoding=[]
    while(len(unknown_face_encoding)==0): #capturing the face
        i=0
        flag=0
        while(i<100):
            i=i+1
            ran,img=cap.read()
            imgs = cv2.resize(img,(0,0),None,0.25,0.25)
            if(i==50):
                img1=imgs
            facloc=face_recognition.face_locations(imgs)
            if(len(facloc)!=0):
                y1,x2,y2,x1=facloc[0]
                y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            var.set("Show your face")
            aimg=img
            aimg = cv2.cvtColor(aimg,cv2.COLOR_BGR2RGB)
            aimg = ImageTk.PhotoImage(Image.fromarray(aimg))
            L1['image'] = aimg
            root.update()
        img = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        unknown_face_encoding=(face_recognition.face_encodings(img))
        if(len(unknown_face_encoding) == 0):
            var.set("Please Try again") #if face is not detected returns try again
            img=cv2.imread('tryagain.jpg')
            img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
            img=ImageTk.PhotoImage(Image.fromarray(img))
            L1['image']=img
            root.update()
            time.sleep(1)
            flag = 1
            break
    if(len(unknown_face_encoding) == 0):
        break
    unknown_face_encoding=numpy.array(unknown_face_encoding)
    known_encodings=find_encodings(qrdecode)
    if(known_encodings is None): #if detected qr is wrong 
        img=cv2.imread('wrongqr.jpg')
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img=ImageTk.PhotoImage(Image.fromarray(img))
        L1['image']=img
        var.set("INVALID QR")
        root.update()
        time.sleep(1)
        break
    matchrate=face_recognition.compare_faces(known_encodings,unknown_face_encoding)
    distance=face_recognition.face_distance(known_encodings,unknown_face_encoding[0])
    if(matchrate[0]==True and distance<0.5): #marks the attendance in excel sheet
        time.sleep(1)
        img=cv2.imread('attendancedone.jpeg')
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img=ImageTk.PhotoImage(Image.fromarray(img))
        L1['image']=img
        var.set("Attendance marked")
        root.update()
        time.sleep(1)
        markattendance(qrdecode)
        break
    else: #face didn't matched
        img=cv2.imread('tryagain.jpg')
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img=ImageTk.PhotoImage(Image.fromarray(img))
        L1['image']=img
        var.set("NO MATCH")
        root.update()
        time.sleep(1)
        break
    root.mainloop()
