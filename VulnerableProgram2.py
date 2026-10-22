import pickle
import os

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

# Save a default account if there is no file 
def create_account():
    account = BankAccount("Harby", 500)  # Default account
    with open("account.dat", "wb") as f:
        pickle.dump(account, f)
    print("No file found. Created a new account.dat.")

# Load the account if the file exists
def load_account():
    if not os.path.exists("account.dat"):
        create_account()  # Create file if no file is found 
    
    with open("account.dat", "rb") as f:
        account = pickle.loads(f.read())  # Vulnerable Deserialization
        print(account) 


load_account()  # Run the script

