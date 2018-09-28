from tkinter import *
from tkinter import messagebox
from DatabaseConnection import Database
import os
dataBase = Database()

ENTRY_FONT = ("Fira Mono", 16)


class SignUpPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.configure(padx=20, pady=20)

        self.headingImage = PhotoImage(file="logo.png")
        self.headingLabel = Label(self, image=self.headingImage, anchor=CENTER)
        self.headingLabel.grid(row=0, column=0, columnspan=3)

        self.userNameVar = StringVar()
        self.userEmailVar = StringVar()
        self.userPasswordVar = StringVar()
        self.userAgeVar = IntVar()
        self.userGenderVar = StringVar()
        self.userPhoneVar = IntVar()

        self.userNameEntry = Entry(
            self, textvariable=self.userNameVar, font=ENTRY_FONT)
        self.userNameEntry.insert(0, "Full Name")
        self.userNameEntry.grid(row=1, column=0, columnspan=3, sticky=EW, pady=5)

        self.userAgeEntry = Entry(
            self, textvariable=self.userAgeVar, font=ENTRY_FONT)
        self.userAgeEntry.insert(0,"Age: ")
        self.userAgeEntry.grid(row=2, column=0, columnspan=2, sticky=EW, pady=5)

        self.userEmailEntry = Entry(
            self, textvariable=self.userEmailVar, font=ENTRY_FONT)
        self.userEmailEntry.insert(0, "example@mail.com")
        self.userEmailEntry.grid(row=3, column=0, pady=5)

        self.userPasswordEntry = Entry(
            self, show="*", textvariable=self.userPasswordVar, font=ENTRY_FONT)
        self.userPasswordEntry.insert(0, "Password")
        self.userPasswordEntry.grid(row=3, column=1, pady=5)

        self.radioMale = Radiobutton(self, text="MALE", variable=self.userGenderVar, value="Male")
        self.radioMale.grid(row=4, column=0, pady=5)

        self.radioFemale = Radiobutton(
            self, text="FEMALE", variable=self.userGenderVar, value="Female")
        self.radioFemale.grid(row=4, column=1, pady=5)

        self.userPhoneEntry = Entry(
            self, textvariable=self.userPhoneVar, font=ENTRY_FONT)
        self.userPhoneEntry.insert(0, "Phone Number: ")
        self.userPhoneEntry.grid(row=5, column=0, columnspan=2, pady=5)

        self.signUpButton = Button(self, bg="#e53935", fg="white",
                                   text="Sign Up", font=ENTRY_FONT,command=lambda:[Database.Insert(Database,self.userNameVar.get(),self.userAgeVar.get(),self.userPhoneVar.get(),self.userEmailVar.get(),self.userPasswordVar.get(),self.userGenderVar.get())
                                   ,messagebox.showinfo("","SIGNUP Sucessful")])
        self.signUpButton.grid(row=6, column=0, pady=5)
        self.backloginButton = Button(self, bg="#e53935", fg="white",
                                      text="Back to Login", font=ENTRY_FONT, command=lambda: controller.showFrame(LoginPage))
        self.backloginButton.grid(row=6, column=1, pady=5)


class LoginPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.headingImage = PhotoImage(file="logo.png")
        self.headingLabel = Label(self, image=self.headingImage)
        self.headingLabel.pack()
        
        self.contro=controller
        self.userEmailVar = StringVar()
        self.userPasswordVar = StringVar()

        self.userEmailEntry = Entry(self, textvariable=self.userEmailVar, font=ENTRY_FONT)
        self.userEmailEntry.insert(0, "example@mail.com")
        self.userEmailEntry.pack(pady=15, ipady=5, ipadx=5)

        self.userPasswordEntry = Entry(self, show="*", textvariable=self.userPasswordVar, font=ENTRY_FONT)
        self.userPasswordEntry.insert(0, "Password")
        self.userPasswordEntry.pack(pady=15, ipady=5, ipadx=5)

        self.loginButton = Button(self, bg="#e53935", fg="white", 
                                    text="Login", font=ENTRY_FONT, command=self.verifyLogin)
        self.loginButton.pack(ipadx=10,pady=10)

        #self.signUpButton = Button(self, bg="#e53935", fg="white",
        #                           text="Sign Up", font=ENTRY_FONT, command=lambda: controller.showFrame(SignUpPage))
        #self.signUpButton.pack(ipadx=10, pady=10)

    def verifyLogin(self):
        self.userEmailVar = self.userEmailEntry.get()
        self.userPasswordVar = self.userPasswordEntry.get()

        if self.userEmailVar == "" or self.userPasswordVar == "":
            messagebox.showwarning(title="Fill out both the fields", message="Please fill out both the entry fields.")
        else:
            #messagebox.showinfo(title="Notification", message=dataBase.LoginUser(self.userEmailVar, self.userPasswordVar))
            self.contro.showFrame(MainPage)

    #def goToUserProfile(self, userEmailVar, userPasswordVar):
    #    controller.showFrame(MainPage)

class MainPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.headingImage = PhotoImage(file="logo.png")
        self.headingLabel = Label(self, image=self.headingImage)
        self.headingLabel.pack()

        self.openApp = Button(self, bg="#e53935", fg="white", 
                                    text="Open Billing App", font=ENTRY_FONT, command=self.Start)
        self.openApp.pack(ipadx=10,pady=10)
        self.signUpButton = Button(self, bg="#e53935", fg="white",text="Sign Up", font=ENTRY_FONT, command=lambda: controller.showFrame(SignUpPage))
        self.signUpButton.pack(ipadx=10, pady=10)
    def Start(self):
        os.system("Python I1python01.py")