import mysql.connector as mc
import random
from datetime import datetime
import tkinter as tk #for future upgrade

con = mc.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ENDE_SYS"
)

cur = con.cursor()

def first_translator(message):
    global code
    code = {"a": "p", "b": "q", "c": "o", "d": "b", "e": "ë", "f": "t", "g": "&", "h": "y", "i": "!", "j": "?", "k": "x", "l": "|", "m": "w", "n": "u", "o": "*", "p": ")", "q": "(", "r": "+", "s": "$", "t": "f", "u": "~", "v": ">", "w": "@", "x": "×", "y": "#", "z": '"', " ": "a"}
    result = ""
    for char in message.lower():
        result += code.get(char, char)
    return result

def encryption():
    username = input("Enter Your Username = ")
    frequency = datetime.now().strftime("%H:%M:%S")
    otp = random.randint(1, 100)
    message = input("Enter Your Message = ")

    first_ence = first_translator(message)
    mid = len(first_ence) // 2

    first_half = first_ence[:mid]
    second_half = first_ence[mid:]

    fh_asci = []
    sh_asci = []

    for char in first_half:
        fh_asci.append(ord(char))
    for alpha in second_half:
        sh_asci.append(ord(alpha))

    fh_asci1 = ""
    sh_asci2 = ""

    add_val = int(frequency[3])
    sub_val = int(frequency[6])

    for i in fh_asci:
        fh_asci1 += chr(i + add_val)

    for j in sh_asci:
        sh_asci2 += chr(j - sub_val)

    encre_message = fh_asci1 + sh_asci2
    print("Your OTP is = ", otp)
    print("Encrypted Message = ", encre_message)

    cur.execute("insert into data (otp, frequecny, username) values(%s,%s,%s)", (otp, frequency, username))
    con.commit()

def decryption():
    encrypted = input("Enter Encrypted Message To Read = ")
    otp_input = int(input("Enter Otp Generated While Encryption = "))

    cur.execute("select frequecny from data where otp=%s", (otp_input,))
    freq = cur.fetchone()

    if not freq:
        print("Invalid OTP")
        return

    freq_str = str(freq[0])

    add_val = int(freq_str[3])
    sub_val = int(freq_str[6])

    mid = len(encrypted) // 2
    first_half = encrypted[:mid]
    second_half = encrypted[mid:]

    fh_asci = []
    sh_asci = []

    for char in first_half:
        fh_asci.append(ord(char))
    for alpha in second_half:
        sh_asci.append(ord(alpha))

    fh_asci1 = ""
    sh_asci2 = ""

    for i in fh_asci:
        fh_asci1 += chr(i - add_val)

    for j in sh_asci:
        sh_asci2 += chr(j + sub_val)

    sec_decryp = fh_asci1 + sh_asci2

    rev_code = {v: k for k, v in code.items()}
    finall_decrypt = ""

    for ch in sec_decryp:
        finall_decrypt += rev_code.get(ch, ch)

    print("Your Decrypted Message = ", finall_decrypt)

    cur.execute("delete from data where otp=%s", (otp_input,))
    con.commit()

print("---------------Welcome To ENDE By EHM, Encryption & Decryption-------------")
print()
print("• Instructions")
print("1. Encryption")
print("2. Decryption")
print("3. Exit")

while True:
    choice = int(input("Enter Your Choice = "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    elif choice == 3:
        break
