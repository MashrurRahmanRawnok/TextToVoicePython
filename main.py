#!/bin/python3
import pyttsx3 # Import The Pyttsx3 To Play The Audio Voice
default = "SomeText.txt"
path = input("""Please Inter The Path For The TxT File You Want to Hear \n Default (SomeText.txt) \n>>""")
if "/" in path:
   pass
elif not "/" and ".txt" in path :
    print("invalid Path Continuing With The Default One")
    path = default
elif path == "" :
    path = default
else:
    path = default

book=open(path) 
book_text=book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()