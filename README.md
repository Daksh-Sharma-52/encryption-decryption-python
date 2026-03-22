# Encryption & Decryption System (Python)

## Description
A Python-based system that encrypts and decrypts messages using custom character mapping, ASCII transformations, and OTP-based verification.

## Features
- Custom character substitution encryption
- Message splitting and ASCII transformation
- OTP-based security for decryption
- Time-based encryption logic
- MySQL database integration for OTP storage

## How It Works
1. User enters a message
2. Message is transformed using a custom character mapping
3. Message is split into two halves
4. ASCII values are modified using time-based logic
5. OTP is generated and stored in database
6. Decryption requires correct OTP to retrieve original message

## Tech Stack
- Python
- MySQL
- datetime module
- random module

## Database Setup
Database: ENDE_SYS

Table:
- data(otp, frequecny, username)

## How to Run
1. Install required module:
   pip install mysql-connector-python

2. Setup MySQL:
   - Create database ENDE_SYS
   - Create required table

3. Run the program:
   python ende.py

## Future Improvements
- Add GUI using Tkinter
- Improve encryption strength
- Add password protection
- Store encrypted messages

## Developer
Daksh Sharma (Eagle Head)
