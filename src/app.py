import customtkinter as ctk
import tkinter as tk
from src import db
import random

ctk.set_appearance_mode("dark")
            
class SignUpWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("500x300")
        self.title("Sign Up")
        
        self.TitleLabel = ctk.CTkLabel(self, justify=ctk.LEFT, text="Sign Up", font=("IBMPlexSerif", 20), text_color="white").grid(row=0, column=0, pady=10, padx=10)
        self.ageEntry = ctk.CTkEntry(self, placeholder_text="MM/DD/YYYY").grid(row=1, column=0, pady=10, padx=10)
        self.userEntry = ctk.CTkEntry(self, placeholder_text="Username").grid(row=2, column=0, pady=10, padx=10)
        self.newPasswordEntry = ctk.CTkEntry(self, placeholder_text="Password", show="*").grid(row=3, column=0, pady=10, padx=10)
        self.confirmPasswordEntry = ctk.CTkEntry(self, placeholder_text="Confirm Password", show="*").grid(row=4, column=0, pady=10, padx=10)
        self.confirmSignUp = ctk.CTkButton(self, text="Sign Up", command=self.destroy).grid(row=5, column=0, pady=10, padx=10)
        
        
class MainMenu(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    
        self.configure(segmented_button_selected_color="#5B9A8E", segmented_button_selected_hover_color="#37675E")        
        
        self.id = ctk.IntVar(value=4)
        self.checkingAmount = ctk.DoubleVar(value=db.getChecking(self.id.get()))
        self.savingsAmount = ctk.DoubleVar(value=db.getSavings(self.id.get()))
        
        # create tabs
        self.add("Balance")
        self.add("Deposit")
        self.add("Pay and Transfer")
        self.add("Account")

        # add widgets on tabs
        
        self.checkDeposit = ctk.StringVar()
        
        privacySwitch = ctk.CTkSwitch(self.tab("Balance"), text="privacy").pack(side=ctk.TOP, padx=20, pady=20)
        
        self.checkingBalanceFrame = ctk.CTkFrame(self.tab("Balance"))
        self.checkingBalanceFrame.pack(side=ctk.LEFT, padx=10, pady=10, ipadx=10, ipady=10, fill="both", expand=True)
        self.checkingBalanceLabel = ctk.CTkLabel(self.checkingBalanceFrame, text="Checking", font=("IBMPlexSerif", 20), justify=ctk.CENTER).pack(side=ctk.TOP, padx=20, pady=10)
        self.checkingAmountLabel = ctk.CTkLabel(self.checkingBalanceFrame, textvariable=self.checkingAmount, font=("IBMPlexSerif", 40), justify=ctk.CENTER).pack(padx=30, pady=30)
        #transactionsCheckingFrame = ctk.CTkScrollableFrame(checkingBalanceFrame, label_text="Transactions").pack(side=ctk.BOTTOM, padx=20, pady=20, ipadx=20, ipady=20, fill="both", expand=True)
        self.depositLabel = ctk.CTkLabel(self.checkingBalanceFrame, text="Deposit", font=("IBMPlexSerif", 15), justify=ctk.CENTER).pack(padx=30, pady=30)
        self.checkingDepositEntry = ctk.CTkEntry(self.checkingBalanceFrame, placeholder_text="Deposit", textvariable=self.checkDeposit).pack(padx=10, pady=10)
        
        self.savingsBalanceFrame = ctk.CTkFrame(self.tab("Balance"))
        self.savingsBalanceFrame.pack(side=ctk.RIGHT, padx=10, pady=10, ipadx=10, ipady=10, fill="both", expand=True)
        self.savingsBalanceLabel = ctk.CTkLabel(self.savingsBalanceFrame, text="Savings", font=("IBMPlexSerif", 20), justify=ctk.LEFT).pack(side=ctk.TOP, padx=20, pady=10)
        self.savingsAmountLabel = ctk.CTkLabel(self.savingsBalanceFrame, textvariable=self.savingsAmount, font=("IBMPlexSerif", 40)).pack(padx=30, pady=30)
        self.TransactionsSavingsFrame = ctk.CTkScrollableFrame(self.savingsBalanceFrame, label_text="Transactions").pack(side=ctk.BOTTOM, padx=20, pady=20, ipadx=20, ipady=20, fill="both", expand=True)
        
        self.depositFrame = ctk.CTkFrame(self.tab("Deposit"))
        self.depositFrame.pack(padx=20, pady=20, ipadx=20, ipady=20, fill="both", expand=True, anchor=ctk.CENTER)
        self.AccountChoice = ctk.CTkOptionMenu(self.depositFrame, values=["Checking", "Savings"], font=("IBMPlexSerif", 20), width=200, height=30).pack(padx=60, pady=20)
        self.amountEntry = ctk.CTkEntry(self.depositFrame, placeholder_text="0.00", width=200, height=40).pack(padx=60, pady=20)
        self.depositButton = ctk.CTkButton(self.depositFrame, text="Deposit", width=80, height=40).pack(padx=60, pady=20)
        
        self.transferFrame = ctk.CTkFrame(master=self.tab("Pay and Transfer"))
        self.transferFrame.pack(padx=20, pady=20, ipadx=20, ipady=20, fill="both", expand=True, anchor=ctk.CENTER)
        self.fromLabel = ctk.CTkLabel(self.transferFrame, text="From:").grid(column=0, row=0, padx=20, pady=20)
        self.fromAccountChoice = ctk.CTkOptionMenu(self.transferFrame, values=["Checking", "Savings"]).grid(column=1, row=0, padx=20, pady=20)
        self.toLabel = ctk.CTkLabel(self.transferFrame, text="To:").grid(column=0, row=1, padx=20, pady=20)
        self.toAccountChoice = ctk.CTkOptionMenu(self.transferFrame, values=["Checking", "Savings"]).grid(column=1, row=1, padx=20, pady=20)
        self.amountLabel = ctk.CTkLabel(self.transferFrame, text="Amount:").grid(column=0, row=2, padx=20, pady=20)
        self.amountEntry = ctk.CTkEntry(self.transferFrame, placeholder_text="0.00", width=200, height=40).grid(column=1, row=2, padx=60, pady=20)
        
        self.newButton = ctk.CTkButton(self.checkingBalanceFrame, command=self.assignrandomnumber).pack(padx=10, pady=10)
        
    def assignrandomnumber(self):
        self.checkingAmount.set(random.randint(0, 200000000))
        
    #def privacy(self):
        #self.configure(fg_color="transparent")
           
           
          
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.geometry("900x600")
        self.title("AlbaBank_2023")
        
        self.loginFrame = ctk.CTkFrame(self)
        self.loginFrame.pack(pady=20, padx=60, fill="both", expand=True)
        
        self.titleLabel = ctk.CTkLabel(self.loginFrame, justify=ctk.LEFT, text="Alba Bank", font=("IBMPlexSerif", 20), text_color="white")
        self.titleLabel.pack(pady=30, padx=50)

        self.usernameEntry = ctk.CTkEntry(self.loginFrame, placeholder_text="Username")
        self.usernameEntry.pack(pady=10, padx=10)

        self.passwordEntry = ctk.CTkEntry(self.loginFrame, placeholder_text="Password", show="*")
        self.passwordEntry.pack(pady=10, padx=10)

        self.login_button = ctk.CTkButton(self.loginFrame, text="Login", command=self.openMainMenu)
        self.login_button.pack(pady=10, padx=10)

        self.signup_button = ctk.CTkButton(self.loginFrame, command=self.open_signUp, text="Sign Up")
        self.signup_button.pack(pady=0, padx=10)
        
    def open_signUp(self):
        signUpwindow = SignUpWindow(self)
        signUpwindow.grab_set()
        
    def openMainMenu(self):
        self.loginFrame.destroy()
        self.tab_view = MainMenu(self)
        self.tab_view.pack(padx=20, pady=20, fill="both", expand=True)
        self.grid_columnconfigure(1, weight=1)


app = App()
app.mainloop()