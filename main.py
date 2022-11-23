# ==== Importing all the necessary libraries for Python Invoice Generator Project

import os
import tkinter as tk
from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import filedialog


# ==== creating main class
class InvoiceGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice")
        self.root.geometry("750x800")

        # creating frame in window

        self.frame = Frame(self.root, bg="white")
        self.frame.place(x=80, y=20, width=600, height=700)

        Label(self.frame, text="Enter your company details ", font=("times new roman", 30, "bold"), bg="white",
              fg="green", bd=0).place(x=50, y=10)

        Label(self.frame, text="Company Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=80)
        self.company_name = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.company_name.place(x=270, y=80, width=300, height=35)

        Label(self.frame, text="Address", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=140)
        self.address = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.address.place(x=270, y=140, width=300, height=35)

        Label(self.frame, text="Phone Number", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=200)
        self.phone = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.phone.place(x=270, y=200, width=300, height=35)

        Label(self.frame, text="Date", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=260)
        self.date = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.date.place(x=270, y=260, width=300, height=35)

        Label(self.frame, text="Customer Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=320)
        self.c_name = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.c_name.place(x=270, y=320, width=300, height=35)

        Label(self.frame, text="Car Type", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=380)
        self.carType = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.carType.place(x=270, y=380, width=300, height=35)

        Label(self.frame, text="Service Type", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=440)
        self.serviceType = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.serviceType.place(x=270, y=440, width=300, height=35)

        Label(self.frame, text="Payment Method", font=("times new roman", 15, "bold"), bg="white",
              fg="gray").place(
            x=50, y=500)
        self.pay = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.pay.place(x=270, y=500, width=300, height=35)

        Label(self.frame, text="Total Amount", font=("times new roman", 15, "bold"), bg="white",
              fg="gray").place(x=50, y=560)
        self.total = Entry(self.frame, font=("times new roman", 15), bg="light grey")
        self.total.place(x=270, y=560, width=300, height=35)

        Label(self.frame, text="Company Logo", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=620)

        # ==== Browse File
        Button(self.frame, text="Browse Files", font=("times new roman", 14), command=self.browse).place(x=270, y=620)

        # ====submit details
        Button(self.frame, text="Submit Details", command=self.generate_invoice, font=("times new roman", 14),
               fg="white", cursor="hand2", bg="#B00857").place(x=50, y=660, width=180, height=40)

    # ==== Browse Function
    def browse(self):
        self.file_name = filedialog.askopenfilename(title="Select a File")
        Label(self.frame, text=os.path.basename(self.file_name), font=("times new roman", 15)).place(x=270, y=660)

    # ==== Invoice Generation Function

    def generate_invoice(self):
        c = canvas.Canvas("Invoice.pdf", pagesize=(200, 250), bottomup=0)
        c.setFillColorRGB(0.0, 0.5, 0.5)

        c.line(70, 22, 180, 22)
        c.line(5, 45, 195, 45)

        c.translate(10, 40)
        c.scale(1, -1)
        c.drawImage(self.file_name, 0, 0, width=50, height=30)

        c.scale(1, -1)
        c.translate(-10, -40)

        c.setFont("Times-Bold", 10)
        c.drawCentredString(125, 20, self.company_name.get())

        c.setFont("Times-Bold", 5)
        c.drawCentredString(125, 30, self.address.get())

        c.setFont("Times-Bold", 8)
        c.drawCentredString(100, 55, "INVOICE")

        c.setFont("Times-Bold", 5)

        c.drawRightString(70, 70, "Customer Name: ")
        c.drawRightString(100, 70, self.c_name.get())

        c.drawRightString(70, 80, "Date :")
        c.drawRightString(100, 80, self.date.get())

        c.drawRightString(70, 90, "Phone No. :")
        c.drawRightString(100, 90, self.phone.get())

        c.drawRightString(70, 100, "Car Type :")
        c.drawRightString(100, 100, self.carType.get())

        c.drawRightString(70, 110, "Service Type :")
        c.drawRightString(100, 110, self.serviceType.get())

        c.drawRightString(70, 120, "Payment Method :")
        c.drawRightString(100, 120, self.pay.get())

        c.drawRightString(70, 130, "Total Amount :")
        c.drawRightString(100, 130, self.total.get())

        c.drawString(30, 230, "Thank you for believing in us!!")

        c.showPage()
        c.save()

    # ==== creating main function


def main():
    # ==== create tkinter window
    root = Tk()
    # === creating object for class InvoiceGenerator
    obj = InvoiceGenerator(root)
    # ==== start the gui
    root.mainloop()


if __name__ == "__main__":
    # ==== calling main function
    main()
