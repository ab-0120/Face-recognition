from tkinter import*
import tkinter
from tkinter import Button, Entry, Frame, Label, LabelFrame, Scrollbar, StringVar, Tk, ttk
from tkinter.constants import BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, VERTICAL, W, X, Y
from typing import Pattern, cast
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import random
import os
import numpy as np


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x800+0+0")
        self.root.title("Attendance")

        title_lbl = Label(self.root, text="ATTENDANCE", font=(
            "times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=5, width=1550, height=75)

        ##################### images #################

        # MAKING MAIN FRAME
        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=10, y=85, width=1500, height=700)

        # ================================================
        # left label frame -- can add text in label frame
        left_frame = LabelFrame(
            main_frame, bd=4, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=20, width=690, height=660)

        # current course -- can add text in label frame
        current_course_frame = LabelFrame(
            left_frame, bd=4, bg="white", relief=RIDGE)
        current_course_frame.place(x=5, y=10, width=670, height=420)

        # ====================================================
        # right label frame -- can add text in label frame
        right_frame = LabelFrame(
            main_frame, bd=4, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=710, y=20, width=770, height=660)


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
