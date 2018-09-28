from tkinter import *
from tkinter import messagebox
from DatabaseConnection import Database

dataBase = Database()

ENTRY_FONT = ("Fira Mono", 16)


class SignUpPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.headingImage = PhotoImage(file="logo.png")
        self.headingLabel = Label(self, image=self.headingImage)
        self.headingLabel.grid(row=0, column=0)

        self.userNameVar = StringVar()
        self.userEmailVar = StringVar()
        self.userPasswordVar = StringVar()
        self.userAgeVar = IntVar()
        self.userGenderVar = StringVar()

        self.userNameEntry = Entry(
            self, textvariable=self.userNameVar, font=ENTRY_FONT)
        self.userNameEntry.insert(0, "Full Name")
        self.userNameEntry.grid(row=1, column=1)  # (pady=15, ipady=5, ipadx=5)

        self.userAgeEntry = Entry(
            self, textvariable=self.userAgeVar, font=ENTRY_FONT)
        self.userAgeEntry.pack(pady=15, ipady=5, ipadx=5)

        self.userEmailEntry = Entry(
            self, textvariable=self.userEmailVar, font=ENTRY_FONT)
        self.userEmailEntry.insert(0, "example@mail.com")
        self.userEmailEntry.pack(pady=15, ipady=5, ipadx=5)

        self.userPasswordEntry = Entry(
            self, show="*", textvariable=self.userPasswordVar, font=ENTRY_FONT)
        self.userPasswordEntry.insert(0, "Password")
        self.userPasswordEntry.pack(pady=15, ipady=5, ipadx=5)

        self.radioMale = Radiobutton(
            self, text="MALE", variable=self.userGenderVar, value="Male")
        self.radioMale.pack(ipadx=10, pady=10)

        self.radioFemale = Radiobutton(
            self, text="FEMALE", variable=self.userGenderVar, value="Female")
        self.radioFemale.pack(ipadx=10, pady=10)

        self.signUpButton = Button(self, bg="#e53935", fg="white",
                                   text="Sign Up", font=ENTRY_FONT)
        self.signUpButton.pack(ipadx=10, pady=10)

        self.backloginButton = Button(self, bg="#e53935", fg="white",
                                      text="Back to Login", font=ENTRY_FONT, command=lambda: controller.showFrame(LoginPage))
        self.backloginButton.pack(ipadx=10, pady=10)


class LoginPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.headingImage = PhotoImage(file="logo.png")
        self.headingLabel = Label(self, image=self.headingImage)
        self.headingLabel.pack()

        self.userEmailVar = StringVar()
        self.userPasswordVar = StringVar()

        self.userEmailEntry = Entry(
            self, textvariable=self.userEmailVar, font=ENTRY_FONT)
        self.userEmailEntry.insert(0, "example@mail.com")
        self.userEmailEntry.pack(pady=15, ipady=5, ipadx=5)

        self.userPasswordEntry = Entry(
            self, show="*", textvariable=self.userPasswordVar, font=ENTRY_FONT)
        self.userPasswordEntry.insert(0, "Password")
        self.userPasswordEntry.pack(pady=15, ipady=5, ipadx=5)

        self.loginButton = Button(self, bg="#e53935", fg="white",
                                  text="Login", font=ENTRY_FONT, command=self.verifyLogin)
        self.loginButton.pack(ipadx=10, pady=10)

        self.signUpButton = Button(self, bg="#e53935", fg="white",
                                   text="Sign Up", font=ENTRY_FONT, command=lambda: controller.showFrame(SignUpPage))
        self.signUpButton.pack(ipadx=10, pady=10)

    def verifyLogin(self):
        self.userEmailVar = self.userEmailEntry.get()
        self.userPasswordVar = self.userPasswordEntry.get()

        if self.userEmailVar == "" or self.userPasswordVar == "":
            messagebox.showwarning(
                title="Fill out both the fields", message="Please fill out both the entry fields.")
        else:
            messagebox.showinfo(title="Notification", message=dataBase.LoginUser(
                self.userEmailVar, self.userPasswordVar))
            self.goToUserProfile(self.userEmailVar, self.userPasswordVar)

    def goToUserProfile(self, userEmailVar, userPasswordVar):
        pass
