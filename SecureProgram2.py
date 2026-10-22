import json
import os
import hashlib

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

    def to_dict(self):
        """Convert the object to a dictionary for JSON serialization."""
        return {"owner": self.owner, "balance": self.balance}

    @staticmethod
    def from_dict(data):
        """Reconstruct a BankAccount instance from a dictionary."""
        return BankAccount(data["owner"], data["balance"])

# Function to create a new BankAccount and save it to a file with a checksum
def create_account():
    account = BankAccount("Hamza", 1000000)
    json_data = json.dumps(account.to_dict()).encode()  # Convert to JSON bytes

    # Calculate the checksum (SHA256 hash) of the JSON data
    checksum = hashlib.sha256(json_data).hexdigest().encode()  # Store as hex string

    # Save both the JSON data and the checksum
    with open("account.json", "wb") as f:
        f.write(json_data + b"\n")  # JSON data followed by a newline
        f.write(checksum)  # Store the checksum as a string

    print(f"New account created: {account}")

# Function to load the account with integrity verification
def load_account():
    # Check if the file exists
    if not os.path.exists("account.json"):
        create_account()  # If the file doesn't exist, create a new one

    with open("account.json", "rb") as f:
        file_content = f.read().split(b"\n")  # Split JSON data and checksum

        if len(file_content) < 2:
            raise ValueError("Invalid file: Corrupted or incomplete data")

        json_data = file_content[0]  # Extract JSON data
        stored_checksum = file_content[1]  # Extract stored checksum

    # Calculate checksum for integrity check
    calculated_checksum = hashlib.sha256(json_data).hexdigest().encode()

    if stored_checksum != calculated_checksum:
        raise ValueError("Data integrity compromised: Checksum mismatch!")

    try:
        # Deserialize JSON data
        data = json.loads(json_data.decode())
        account = BankAccount.from_dict(data)
    except Exception as e:
        print(f"Error during deserialization: {e}")
        return None

    return account

if __name__ == "__main__":
    try:
        account = load_account()
        if account:
            print(account)
    except ValueError as e:
        print(f"Error: {e}")

