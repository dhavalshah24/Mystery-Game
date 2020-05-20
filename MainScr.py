from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import socket
import select
import sys
import threading
import time
import pyttsx3
engine = pyttsx3.init()

window = Tk()
window.title("Mystery Game")
window.geometry("600x590")
chances = 4
answer_arr = []

# Class for Connection to send and receive messages
class Con:
    global b
    global a
    global c
    global i
    i = 0
    c = 0
    b = 0
    a = []

    #Function to receive messages from other users connected to same server
    def recvs(self, str):
        global b
        global a
        global c
        self.str = str
        sockets_list = [socket.socket(), server]
        read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])
        for socks in read_sockets:
            message = socks.recv(2048).decode()
            print(message)
            try:
                x, message = message.split('>')
            except:
                y = message
            if b < 1:
                a = message.split(" ")
                c = a[1]
                b += 1
            else:
                message = message.split(" ")
                engine.say(message[2])
                engine.runAndWait()

    #Function to send messages to other users connected to same server
    def sends(self, value):
        global c
        print(c)
        message = str(a[1]) + " " + str(value)
        server.send(message.encode())
        sys.stdout.write("<You>")
        sys.stdout.write(message + "\n")
        sys.stdout.flush()

    #Function to create chance for users in the game
    #Player 1 then Player 2 and so on ...
    def clicked(self, alphabet):
        global c, i
        i += 1
        p_no = int(c)
        p = 0
        while p < p_no - 1:
            self.recvs('Received: ')
            p += 1
        print("psst")
        self.sends(alphabet)
        p += 1
        while p < 3:
            self.recvs('Received: ')
            p += 1


if __name__ == "__main__":
    global c, i
    #Creating Connection
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if len(sys.argv) != 3:
        print("Correct usage: script, IP address, port number")
        exit()
    IP_address = str(sys.argv[1])
    Port = int(sys.argv[2])
    server.connect((IP_address, Port))
    obj1 = Con()
    obj1.recvs('Received: ')
    #User Interface using Tkinter
    btn1 = Button(window, text="1", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=lambda: obj1.clicked("1"))
    btn1.grid(column=1, row=1)
    btn2 = Button(window, text="2", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=lambda: obj1.clicked("2"))
    btn2.grid(column=2, row=1)
    btn3 = Button(window, text="3", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=lambda: obj1.clicked("3"))
    btn3.grid(column=3, row=1)
    btn4 = Button(window, text="4", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=lambda: obj1.clicked("4"))
    btn4.grid(column=4, row=1)
    btn5 = Button(window, text="5", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=lambda: obj1.clicked("5"))
    btn5.grid(column=5, row=1)
    btn6 = Button(window, text="6", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=lambda: obj1.clicked("6"))
    btn6.grid(column=6, row=1)
    btn7 = Button(window, text="7", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=lambda: obj1.clicked("7"))
    btn7.grid(column=7, row=1)
    btn8 = Button(window, text="8", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=lambda: obj1.clicked("8"))
    btn8.grid(column=8, row=1)
    btn9 = Button(window, text="9", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                  command=lambda: obj1.clicked("9"))
    btn9.grid(column=9, row=1)
    btn10 = Button(window, text="10", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("10"))
    btn10.grid(column=10, row=1)

    btn11 = Button(window, text="11", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("11"))
    btn11.grid(column=1, row=2)
    btn12 = Button(window, text="12", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("12"))
    btn12.grid(column=2, row=2)
    btn13 = Button(window, text="13", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("13"))
    btn13.grid(column=3, row=2)
    btn14 = Button(window, text="14", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("14"))
    btn14.grid(column=4, row=2)
    btn15 = Button(window, text="15", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("15"))
    btn15.grid(column=5, row=2)
    btn16 = Button(window, text="16", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("16"))
    btn16.grid(column=6, row=2)
    btn17 = Button(window, text="17", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("17"))
    btn17.grid(column=7, row=2)
    btn18 = Button(window, text="18", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("18"))
    btn18.grid(column=8, row=2)
    btn19 = Button(window, text="19", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("19"))
    btn19.grid(column=9, row=2)
    btn20 = Button(window, text="20", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("20"))
    btn20.grid(column=10, row=2)

    btn21 = Button(window, text="21", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("21"))
    btn21.grid(column=1, row=3)
    btn22 = Button(window, text="22", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("22"))
    btn22.grid(column=2, row=3)
    btn23 = Button(window, text="23", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("23"))
    btn23.grid(column=3, row=3)
    btn24 = Button(window, text="24", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("24"))
    btn24.grid(column=4, row=3)
    btn25 = Button(window, text="25", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("25"))
    btn25.grid(column=5, row=3)
    btn26 = Button(window, text="26", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("26"))
    btn26.grid(column=6, row=3)
    btn27 = Button(window, text="27", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("27"))
    btn27.grid(column=7, row=3)
    btn28 = Button(window, text="28", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("28"))
    btn28.grid(column=8, row=3)
    btn29 = Button(window, text="29", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("29"))
    btn29.grid(column=9, row=3)
    btn30 = Button(window, text="30", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("30"))
    btn30.grid(column=10, row=3)

    btn31 = Button(window, text="31", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("31"))
    btn31.grid(column=1, row=4)
    btn32 = Button(window, text="32", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("32"))
    btn32.grid(column=2, row=4)
    btn33 = Button(window, text="33", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("33"))
    btn33.grid(column=3, row=4)
    btn34 = Button(window, text="34", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("34"))
    btn34.grid(column=4, row=4)
    btn35 = Button(window, text="35", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("35"))
    btn35.grid(column=5, row=4)
    btn36 = Button(window, text="36", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("36"))
    btn36.grid(column=6, row=4)
    btn37 = Button(window, text="37", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("37"))
    btn37.grid(column=7, row=4)
    btn38 = Button(window, text="38", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("38"))
    btn38.grid(column=8, row=4)
    btn39 = Button(window, text="39", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("39"))
    btn39.grid(column=9, row=4)
    btn40 = Button(window, text="40", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("40"))
    btn40.grid(column=10, row=4)

    btn41 = Button(window, text="41", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("41"))
    btn41.grid(column=1, row=5)
    btn42 = Button(window, text="42", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("42"))
    btn42.grid(column=2, row=5)
    btn43 = Button(window, text="43", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("43"))
    btn43.grid(column=3, row=5)
    btn44 = Button(window, text="44", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("44"))
    btn44.grid(column=4, row=5)
    btn45 = Button(window, text="45", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("45"))
    btn45.grid(column=5, row=5)
    btn46 = Button(window, text="46", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("46"))
    btn46.grid(column=6, row=5)
    btn47 = Button(window, text="47", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("47"))
    btn47.grid(column=7, row=5)
    btn48 = Button(window, text="48", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("48"))
    btn48.grid(column=8, row=5)
    btn49 = Button(window, text="49", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("49"))
    btn49.grid(column=9, row=5)
    btn50 = Button(window, text="50", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("50"))
    btn50.grid(column=10, row=5)

    btn51 = Button(window, text="51", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("51"))
    btn51.grid(column=1, row=6)
    btn52 = Button(window, text="52", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("52"))
    btn52.grid(column=2, row=6)
    btn53 = Button(window, text="53", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("53"))
    btn53.grid(column=3, row=6)
    btn54 = Button(window, text="54", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("54"))
    btn54.grid(column=4, row=6)
    btn55 = Button(window, text="55", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("55"))
    btn55.grid(column=5, row=6)
    btn56 = Button(window, text="56", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("56"))
    btn56.grid(column=6, row=6)
    btn57 = Button(window, text="57", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("57"))
    btn57.grid(column=7, row=6)
    btn58 = Button(window, text="58", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("58"))
    btn58.grid(column=8, row=6)
    btn59 = Button(window, text="59", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("59"))
    btn59.grid(column=9, row=6)
    btn60 = Button(window, text="60", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("60"))
    btn60.grid(column=10, row=6)

    btn61 = Button(window, text="61", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("61"))
    btn61.grid(column=1, row=7)
    btn62 = Button(window, text="62", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("62"))
    btn62.grid(column=2, row=7)
    btn63 = Button(window, text="63", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("63"))
    btn63.grid(column=3, row=7)
    btn64 = Button(window, text="64", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("64"))
    btn64.grid(column=4, row=7)
    btn65 = Button(window, text="65", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("65"))
    btn65.grid(column=5, row=7)
    btn66 = Button(window, text="66", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("66"))
    btn66.grid(column=6, row=7)
    btn67 = Button(window, text="67", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("67"))
    btn67.grid(column=7, row=7)
    btn68 = Button(window, text="68", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("68"))
    btn68.grid(column=8, row=7)
    btn69 = Button(window, text="69", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("69"))
    btn69.grid(column=9, row=7)
    btn70 = Button(window, text="70", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("70"))
    btn70.grid(column=10, row=7)

    btn71 = Button(window, text="71", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("71"))
    btn71.grid(column=1, row=8)
    btn72 = Button(window, text="72", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("72"))
    btn72.grid(column=2, row=8)
    btn73 = Button(window, text="73", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("73"))
    btn73.grid(column=3, row=8)
    btn74 = Button(window, text="74", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("74"))
    btn74.grid(column=4, row=8)
    btn75 = Button(window, text="75", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("75"))
    btn75.grid(column=5, row=8)
    btn76 = Button(window, text="76", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("76"))
    btn76.grid(column=6, row=8)
    btn77 = Button(window, text="77", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("77"))
    btn77.grid(column=7, row=8)
    btn78 = Button(window, text="78", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("78"))
    btn78.grid(column=8, row=8)
    btn79 = Button(window, text="79", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("79"))
    btn79.grid(column=9, row=8)
    btn80 = Button(window, text="80", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("80"))
    btn80.grid(column=10, row=8)

    btn81 = Button(window, text="81", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("81"))
    btn81.grid(column=1, row=9)
    btn82 = Button(window, text="82", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("82"))
    btn82.grid(column=2, row=9)
    btn83 = Button(window, text="83", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("83"))
    btn83.grid(column=3, row=9)
    btn84 = Button(window, text="84", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("84"))
    btn84.grid(column=4, row=9)
    btn85 = Button(window, text="85", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("85"))
    btn85.grid(column=5, row=9)
    btn86 = Button(window, text="86", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("86"))
    btn86.grid(column=6, row=9)
    btn87 = Button(window, text="87", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("87"))
    btn87.grid(column=7, row=9)
    btn88 = Button(window, text="88", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("88"))
    btn88.grid(column=8, row=9)
    btn89 = Button(window, text="89", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("89"))
    btn89.grid(column=9, row=9)
    btn90 = Button(window, text="90", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("90"))
    btn90.grid(column=10, row=9)

    btn91 = Button(window, text="91", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("91"))
    btn91.grid(column=1, row=10)
    btn92 = Button(window, text="92", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("92"))
    btn92.grid(column=2, row=10)
    btn93 = Button(window, text="93", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("93"))
    btn93.grid(column=3, row=10)
    btn94 = Button(window, text="94", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("94"))
    btn94.grid(column=4, row=10)
    btn95 = Button(window, text="95", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("95"))
    btn95.grid(column=5, row=10)
    btn96 = Button(window, text="96", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("96"))
    btn96.grid(column=6, row=10)
    btn97 = Button(window, text="97", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("97"))
    btn97.grid(column=7, row=10)
    btn98 = Button(window, text="98", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("98"))
    btn98.grid(column=8, row=10)
    btn99 = Button(window, text="99", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                   command=lambda: obj1.clicked("99"))
    btn99.grid(column=9, row=10)
    btn100 = Button(window, text="100", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                    command=lambda: obj1.clicked("100"))
    btn100.grid(column=10, row=10)

    label1 = Label(window, text="Total Chances are : 45")
    label1.grid(row=0, column=11)
    #Total chances are 45 per player
    for i in range(45):
        window.mainloop()
    time.sleep(2)

    #Closing Connection
    print("Closing Connection")
    server.close()
    window.destroy()
