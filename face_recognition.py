from tkinter import*
from tkinter import ttk
from tkinter import Button, Entry, Frame, Label, LabelFrame, Scrollbar, StringVar, Tk, ttk
from tkinter.constants import BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, VERTICAL, W, X, Y
from typing import Pattern, cast
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x800+0+0")
        self.root.title("Face recognition sys")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=(
            "times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=5, width=1550, height=75)

        ##################### images #################

        # img 1
        img = Image.open(r"images\face1.jpg")
        img = img.resize((790, 450), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=405, y=150, width=790, height=450)

        # button
        b1_1 = Button(self.root, text="Detect", command=self.face_recog, font=(
            "times new roman", 25, "bold"), bg="teal", fg="white", cursor="hand2")
        b1_1.place(x=700, y=650, width=190, height=70)

    ############### attendance ###############

    def mark_attendance(self, i, r, n, c):
        with open("Anshita.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])

            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (c not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{c},{dtString},{d1},Present")

    ############################ face recognition ####################

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for(x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 4)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Anshita@0120", database="attendance")
                my_cursor = conn.cursor()

                my_cursor.exceute(
                    "select name from student where student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.exceute(
                    "select rollno from student where student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.exceute(
                    "select course from student where student_id=" + str(id))
                c = my_cursor.fetchone()
                c = "+".join(c)

                my_cursor.exceute(
                    "select student_id from student where student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 79:
                    cv2.putText(
                        img, f"Id:{i}", (x, y-65), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 4)
                    cv2.putText(
                        img, f"Roll no:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 4)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 4)
                    cv2.putText(
                        img, f"Course:{c}", (x, y-7), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 4)

                    self.mark_attendance(i, r, n, c)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 4)
                    cv2.putText(
                        img, "Unknown", (x, y-7), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 4)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1,
                                  10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Recognixer", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
