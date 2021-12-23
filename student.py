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


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x800+0+0")
        self.root.title("Face recognition sys")

        ################## variables ########################
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_semester = StringVar()
        self.var_rollno = StringVar()
        self.var_studentid = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_year = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()

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
            r"C:\Users\ASUS\Documents\Attendance\images\flower.jpg")
        img3 = img3.resize((1590, 800), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=135, width=1590, height=800)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1550, height=45)

        # MAKING MAIN FRAME
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1500, height=700)

        # left label frame -- can add text in label frame
        left_frame = LabelFrame(
            main_frame, bd=4, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=20, width=690, height=580)

        ##############################################################

        # current course -- can add text in label frame
        current_course_frame = LabelFrame(
            left_frame, bd=4, bg="white", relief=RIDGE, text="Current course details", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=10, width=670, height=120)

        # department label
        dept_label = Label(current_course_frame, text="Department",
                           font=("times new roman", 12, "bold"), bg="white")
        dept_label.grid(row=0, column=0, padx=10)

        # combo box
        dept_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 13, "bold"), width=17)
        dept_combo["values"] = (
            "Select", "CS", "IT", "CIVIL", "MECHANICAL", "ECE")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=5, pady=10)

        # course
        course_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(current_course_frame,  textvariable=self.var_course, font=(
            "times new roman", 13, "bold"), width=17)
        course_combo["values"] = (
            "Select", "Btech", "BJMC", "BBA", "BCA", "BSc")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        # year
        year_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,  font=(
            "times new roman", 13, "bold"), width=17)
        year_combo["values"] = ("Select", "2023", "2022",
                                "2021", "2020", "2019", "2019", "2018")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        # semester
        semester_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,  font=(
            "times new roman", 13, "bold"), width=17, state="readonly")
        semester_combo["values"] = ("Select", "1", "2",
                                    "3", "4", "5", "6", "7", "8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=5, pady=10, sticky=W)

        ###################################################################

        # student info frame -- can add text in label frame
        student_course_frame = LabelFrame(
            left_frame, bd=4, bg="white", relief=RIDGE, text="Student details", font=("times new roman", 12, "bold"))
        student_course_frame.place(x=5, y=150, width=670, height=380)

        # rollno label
        rollno_label = Label(student_course_frame, text="Roll no", font=(
            "times new roman", 12, "bold"), bg="white")
        rollno_label.grid(row=0, column=0, padx=10, sticky=W)

        rn_entry = ttk.Entry(student_course_frame, textvariable=self.var_rollno,  width=20, font=(
            "times new roman", 12, "bold"))
        rn_entry.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        # name label
        name_label = Label(student_course_frame, text="Name", font=(
            "times new roman", 12, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, sticky=W)

        name_entry = ttk.Entry(student_course_frame,  textvariable=self.var_name, width=20, font=(
            "times new roman", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        # student ID
        studentid_label = Label(student_course_frame, text="Student Id", font=(
            "times new roman", 12, "bold"), bg="white")
        studentid_label.grid(row=1, column=0, padx=10, sticky=W)

        studentid_entry = ttk.Entry(student_course_frame, textvariable=self.var_studentid,  width=20, font=(
            "times new roman", 12, "bold"))
        studentid_entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        # gender
        gender_label = Label(student_course_frame, text="Gender", font=(
            "times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=1, column=2, padx=10, sticky=W)

        gender_combo = ttk.Combobox(student_course_frame, textvariable=self.var_gender,  font=(
            "times new roman", 13, "bold"), width=17, state="readonly")
        gender_combo["values"] = ("Select", "Male", "Female",
                                  "Others")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=5, pady=10, sticky=W)

        # email
        email_label = Label(student_course_frame, text="Email", font=(
            "times new roman", 12, "bold"), bg="white")
        email_label.grid(row=2, column=0, padx=10, sticky=W)

        email_entry = ttk.Entry(student_course_frame, textvariable=self.var_email,  width=20, font=(
            "times new roman", 12, "bold"))
        email_entry.grid(row=2, column=1, padx=5, pady=10, sticky=W)

        # phoneno
        phoneno_label = Label(student_course_frame, text="Phone no", font=(
            "times new roman", 12, "bold"), bg="white")
        phoneno_label.grid(row=2, column=2, padx=10, sticky=W)

        phoneno_entry = ttk.Entry(student_course_frame, textvariable=self.var_phone,  width=20, font=(
            "times new roman", 12, "bold"))
        phoneno_entry.grid(row=2, column=3, padx=5, pady=10, sticky=W)

        # Address
        address_label = Label(student_course_frame, text="Address", font=(
            "times new roman", 12, "bold"), bg="white")
        address_label.grid(row=3, column=0, padx=10, sticky=W)

        address_entry = ttk.Entry(student_course_frame,  textvariable=self.var_address, width=20, font=(
            "times new roman", 12, "bold"))
        address_entry.grid(row=3, column=1, padx=5, pady=10, sticky=W)

        # radio btns
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            student_course_frame, variable=self.var_radio1, text="Take a sample", value="yes")
        radiobtn1.grid(row=4, column=0, padx=40, pady=10)

        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(
            student_course_frame, variable=self.var_radio1, text="No sample", value="no")
        radiobtn2.grid(row=4, column=1)

        ###################################################################

        # btn frame
        btn_frame = Frame(student_course_frame, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=220, width=650, height=42)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=14, font=(
            "times new roman", 12, "bold"), bg="seagreen", fg="white")
        save_btn.grid(row=0, column=0, padx=24, pady=10)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=14, font=(
            "times new roman", 12, "bold"), bg="seagreen", fg="white")
        update_btn.grid(row=0, column=1, padx=10, pady=10)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=14, font=(
            "times new roman", 12, "bold"), bg="seagreen", fg="white")
        delete_btn.grid(row=0, column=2, padx=10, pady=10)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=14, font=(
            "times new roman", 12, "bold"), bg="seagreen", fg="white")
        reset_btn.grid(row=0, column=3, padx=10, pady=10)

        ###################################################################

        # btn frame
        btn_frame1 = Frame(student_course_frame, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=270, width=650, height=42)

        takephoto_btn = Button(btn_frame1, command=self.generate_dataset, text="Take sample", width=18, font=(
            "times new roman", 12, "bold"), bg="seagreen", fg="white")
        takephoto_btn.grid(row=0, column=0, padx=80, pady=10)

        updatephoto_btn = Button(btn_frame1, text="Update sample", width=18, font=(
            "times new roman", 12, "bold"), bg="seagreen", fg="white")
        updatephoto_btn.grid(row=0, column=1, padx=20, pady=10)

        # right label frame -- can add text in label frame
        right_frame = LabelFrame(
            main_frame, bd=4, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=710, y=20, width=770, height=580)

        ############################## Search ##############################
        search_frame = LabelFrame(
            right_frame, bd=4, text="Search", relief=RIDGE, bg="white", font=(
                "times new roman", 12, "bold"))
        search_frame.place(x=7, y=15, width=750, height=90)

        search_label = Label(search_frame, text="Search By:", font=(
            "times new roman", 12, "bold"), bg="grey")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 13, "bold"), width=17, state="readonly")
        search_combo["values"] = ("Select", "Roll no", "Name",
                                  "Course")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=19, font=(
            "times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12, font=(
            "times new roman", 12, "bold"), bg="grey", fg="white")
        search_btn.grid(row=0, column=3, padx=10, pady=10)

        showall_btn = Button(search_frame, text="Show all", width=12, font=(
            "times new roman", 12, "bold"), bg="grey", fg="white")
        showall_btn.grid(row=0, column=4, padx=10, pady=10)

        ##################### TABLE #########################
        table_frame = LabelFrame(
            right_frame, bd=4,  relief=RIDGE, bg="white")
        table_frame.place(x=7, y=115, width=750, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            "dep", "course", "name", "semester", "rollno", "studentid", "year", "gender", "phone", "email", "address", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("rollno", text="Roll no")
        self.student_table.heading("studentid", text="Student ID")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("phone", text="Phone no")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="Sample status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("name", width=150)
        self.student_table.column("semester", width=80)
        self.student_table.column("rollno", width=120)
        self.student_table.column("studentid", width=120)
        self.student_table.column("year", width=70)
        self.student_table.column("gender", width=60)
        self.student_table.column("phone", width=90)
        self.student_table.column("email", width=180)
        self.student_table.column("address", width=250)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    ############################### function ##########################

    def add_data(self):
        if self.var_course.get() == "Select" or self.var_year.get == "Select" or self.var_name == "Select" or self.var_rollno == "Select":
            messagebox.showerror(
                "Error", "Some fields are empty", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Anshita@0120", database="attendance")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_name.get(),
                        self.var_semester.get(),
                        self.var_rollno.get(),
                        self.var_studentid.get(),
                        self.var_year.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_radio1.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    ###################### Fetch data ##########################

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Anshita@0120", database="attendance")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    ########################## get cursor #####################

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_name.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_rollno.set(data[4]),
        self.var_studentid.set(data[5]),
        self.var_year.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_email.set(data[9]),
        self.var_address.set(data[10]),
        self.var_radio1.set(data[11]),

    ###################################### Update #################

    def update_data(self):
        if self.var_course.get() == "Select" or self.var_year.get == "Select" or self.var_name == "Select" or self.var_rollno == "Select":
            messagebox.showerror(
                "Error", "Some fields are empty", parent=self.root)

        else:
            try:
                upadate = messagebox.askyesno(
                    "Update", "Do you want to update this information", parent=self.root)
                if upadate > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Anshita@0120", database="attendance")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set dept=%s, course=%s, name=%s, semester=%s, rollno=%s, year=%s, gender=%s, phone=%s, email=%s,address=%s, photo=%s where student_id=%s", (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_name.get(),
                            self.var_semester.get(),
                            self.var_rollno.get(),
                            self.var_year.get(),
                            self.var_gender.get(),
                            self.var_phone.get(),
                            self.var_email.get(),
                            self.var_address.get(),
                            self.var_radio1.get(),
                            self.var_studentid.get()
                        ))
                else:
                    if not upadate:
                        return
                messagebox.showinfo(
                    "Success", "Student details updated successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to: {str(es)}", parent=self.root)

    ################################# delete ##########################
    def delete_data(self):
        if self.var_studentid.get() == "":
            messagebox.showerror(
                "Error", "Student id is required", parent=self.root)

        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete", "Do you want to delete this data", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Anshita@0120", database="attendance")
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_studentid.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo(
                    "Delete", "Successfully deleted student", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to: {str(es)}", parent=self.root)

    ######################### reset ####################
    def reset_data(self):
        self.var_dep.set("Select")
        self.var_course.set("Select")
        self.var_name.set("")
        self.var_year.set("Select")
        self.var_semester.set("Select")
        self.var_gender.set("Select")
        self.var_rollno.set("")
        self.var_studentid.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")

    ############################## Generate photo samples ###########
    def generate_dataset(self):
        if self.var_course.get() == "Select" or self.var_year.get == "Select" or self.var_name == "Select" or self.var_rollno == "Select":
            messagebox.showerror(
                "Error", "Some fields are empty", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Anshita@0120", database="attendance")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "update student set dept=%s, course=%s, name=%s, semester=%s, rollno=%s, year=%s, gender=%s, phone=%s, email=%s,address=%s, photo=%s where student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_name.get(),
                        self.var_semester.get(),
                        self.var_rollno.get(),
                        self.var_year.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        self.var_studentid.get() == id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on frontal face from opencv ##
                face_classifier = cv2.CascadeClassifier(
                    "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

                #############
                def face_cropped(img):
                    # CONVERTING TO GRAY
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(
                        gray, 1.3, 5)  # scaling factor=1.3 minimum neighbor= 5

                    for(x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                ran = random.randint(0, 22) * random.randint(0, 100)
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "sample_img/user." + \
                            str(ran) + "." + str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped img", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 150:
                        # training
                        def train_classifier(self):
                            data_dir = ("sample_img")
                            path = [os.path.join(data_dir, file)
                                    for file in os.listdir(data_dir)]

                            faces = []
                            ids = []

                            for image in path:
                                img = Image.open(image).convert(
                                    'L')  # converting to gray scale
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

                                clf.train(faces, ids)
                                clf.write("classifier.xml")
                                cv2.destroyAllWindows()
                                messagebox.showinfo(
                                    "Result", "Training dataset completed")

                            except Exception as es:
                                messagebox.showerror(
                                    "Error", f"Due to: {str(es)}", parent=self.root)

                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating data set completed successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
