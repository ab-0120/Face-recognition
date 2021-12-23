import tkinter
from tkinter import Button, Label, Tk, Toplevel, ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
import os
from face_recognition import Face_recognition


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x800+0+0")
        self.root.title("Face recognition sys")

        # first
        img = Image.open(r"C:\Users\ASUS\Documents\Attendance\images\th.jpeg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second
        img1 = Image.open(r"C:\Users\ASUS\Documents\Attendance\images\th.jpeg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=510, height=130)

        # third
        img2 = Image.open(r"C:\Users\ASUS\Documents\Attendance\images\th.jpeg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # bg image
        img3 = Image.open(
            r"C:\Users\ASUS\Documents\Attendance\images\train_bg.png")
        img3 = img3.resize((1590, 800), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=135, width=1590, height=800)

        title_lbl = Label(bg_img, text="WELCOME", font=(
            "times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # student button
        img4 = Image.open(
            r"C:\Users\ASUS\Documents\Attendance\images\student.jpg")
        img4 = img4.resize((200, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student, font=(
            "times new roman", 15, "bold"), cursor="hand2")
        b1_1.place(x=200, y=300, width=220, height=40)

        # face detection
        img5 = Image.open(
            r"C:\Users\ASUS\Documents\Attendance\images\face.jpg")
        img5 = img5.resize((200, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,
                    cursor="hand2", command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detection", font=(
            "times new roman", 15, "bold"), cursor="hand2", command=self.face_data)
        b1_1.place(x=500, y=300, width=220, height=40)

        # attendance
        img6 = Image.open(
            r"C:\Users\ASUS\Documents\Attendance\images\attendance.jpg")
        img6 = img6.resize((200, 200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", font=(
            "times new roman", 15, "bold"), cursor="hand2")
        b1_1.place(x=800, y=300, width=220, height=40)

        # train
        img8 = Image.open(
            r"C:\Users\ASUS\Documents\Attendance\images\train.jpg")
        img8 = img8.resize((200, 200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8,
                    cursor="hand2", command=self.train_data)
        b1.place(x=200, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Train", font=(
            "times new roman", 15, "bold"), cursor="hand2", command=self.train_data)
        b1_1.place(x=200, y=600, width=220, height=40)

        # photos face button
        img9 = Image.open(
            r"images\photos.jpg")
        img9 = img9.resize((200, 200), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,
                    cursor="hand2", command=self.open_img)
        b1.place(x=500, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", font=(
            "times new roman", 15, "bold"), cursor="hand2", command=self.open_img)
        b1_1.place(x=500, y=600, width=220, height=40)

        # exit
        img10 = Image.open(
            r"images\exit.jpg")
        img10 = img10.resize((200, 200), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b1.place(x=800, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", font=(
            "times new roman", 15, "bold"), cursor="hand2")
        b1_1.place(x=800, y=600, width=220, height=40)

    def open_img(self):
        os.startfile("sample_img")

    ########################  Function buttons ####################

    def student(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
