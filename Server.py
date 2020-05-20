import socket
import sys
import _thread
import threading


#Setting up Server
_thread.__all__ = ("error", "LockType", "start_new_thread", "interrupt_main", "exit", "allocate_lock", "get_ident", "stack_size","acquire", "release", "locked")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

global a
a = []
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port))
server.listen(100)
players = []
val = list(9 for i in range(101))
print("done")

#Connecting Clients and giving them their Number
def clientthread(conn, addr, p):
    d = ">Player "+str(p)+" Welcome to this chatroom!"
    conn.send(d.encode())


#Receive message from 1 player and sending it to all other players connected to the server
def game(conn, addr, j, i):
    global a, c, val
    a = []
    message = conn.recv(2048).decode()
    if message:
        print("<" + addr[0] + "> " + message)
        if i <= 135:
            print (message)
            a = message.split(" ")
            print("<" + addr[0] + "> " + message)
            c = int(a[0])
            d = int(a[1])
            if val[d] == 9:
                val[d] = c
                print(val.count(0))
                print(val.count(1))
                print(val.count(2))
            print("val :")
            print(val)
            print('c =' + str(c))
            print('j=' + str(j))
        #Checking if chance was played by correct user or not .
        if c != j:
            print("<" + addr[0] + "> " + message)
            message = "Its not your chance"
            conn.send(message.encode())
            game(conn, addr, j, i)
        else:
            print("<" + addr[0] + "> " + message)
            message_to_send = "<" + addr[0] + "> " + message
            broadcast(message_to_send, conn)
    else:
        remove(conn)

#Sending message to all the players
def broadcast(message, connection):
    for clients in players:
        if clients != connection:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                remove(clients)

#Removing a player
def remove(connection):
    if connection in players:
        players.remove(connection)


h = "h"
p = 0
thread_count = 0
obj = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print("hello")
while p <= 2:
    t = "nt"
    conn, addr = server.accept()
    players.append(conn)
    print("player " + str(p) + " connected")
    thread_count += 1
    t = t + str(thread_count)
    t = threading.Thread(target=clientthread(conn, addr, thread_count))
    obj[p][0] = t
    obj[p][1] = conn
    obj[p][2] = addr
    obj[p][3] = thread_count
    t.start()
    p += 1
    print(p)


print(obj)
i = 0
j = 0
while i < 135:

    t = obj[j]
    print("h")
    t = threading.Thread(target=game(obj[j][1], obj[j][2], obj[j][3], i))
    t.start()
    if j == 2:
        j = 0
    else:
        j += 1
    print("j = " + str(j))
    i += 1
    print("i = " + str(i))

x = val.count(1)
y = val.count(2)
z = val.count(3)
#Finding the elements selected by each player
print("Player 1: " + str(val.count(1)))
print("Player 2: " + str(val.count(2)))
print("Player 3: " + str(val.count(3)))
#Displaying the Winner
if x>y and x>z:
    print("PLAYER 1 : WINNER")
    message = "PLAYER 1 : WINNER"
elif y>x and y>z:
    print("PLAYER 2 : WINNER")
    message = "PLAYER 2 : WINNER"
else:
    print("PLAYER 3 : WINNER")
    message = "PLAYER 3 : WINNER"
broadcast(message, conn)
#Closing Connection
print("Closing Connection")
conn.close()
