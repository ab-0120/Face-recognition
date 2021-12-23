from tkinter import*
from tkinter import ttk
from tkinter import Button, Entry, Frame, Label, LabelFrame, Scrollbar, StringVar, Tk, ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x800+0+0")
        self.root.title("Face recognition sys")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=(
            "times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=5, width=1550, height=75)

        ##################### images #################

        # img 1
        img = Image.open(r"images\train_img.jpg")
        img = img.resize((290, 350), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=485, y=150, width=290, height=350)

        # img 2

        img1 = Image.open(r"images\tain_img1.jpg")
        img1 = img1.resize((500, 350), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f1_lbl = Label(self.root, image=self.photoimg1)
        f1_lbl.place(x=805, y=150, width=290, height=350)

        # button
        b1_1 = Button(self.root, text="Train", command=self.train_classifier, font=(
            "times new roman", 25, "bold"), bg="teal", fg="white", cursor="hand2")
        b1_1.place(x=700, y=600, width=190, height=70)

    # LBPH local binary pattern histogram
    ################################## function #####################

    def train_classifier(self):
        data_dir = ("sample_img")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # converting to gray scale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Train", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        ################### train classifier and save #############
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            # clf = cv2.ml_TrainData(faces, ids)
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training dataset completed")

        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
