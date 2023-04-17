# PlentifyFirmware

## Description
Backhaul emulator for listening to incoming messages and and processing hexadecimal as well as key-value pair data. This library contains a user interface, as well as an API, that allows the user to view either packet or hexadecimal data in an easy-to-read format.

## Requirements
In order to use this library, Python's "struct" and "binascii" modules need to be imported. 

## Usage
To make use of the library from a terminal, navigate to the project directory and type "python interface.py"
This will provide you with two options:
    1. "H":
        - The user must input the hex version of the work product packet
        - The output will be key-value data structure
    2. "P":
        - The user will be promted to enter the value for each key in the product packet
        - The hex version of the work packet will be outputted
