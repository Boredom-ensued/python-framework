import socket # create a socket object 
def host():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # get local machine name 
    host = socket.gethostname() #IP goes here
    port = 8000 # port goes here
    serversocket.bind((host, port)) 
    print ("searching for client devices...")
    serversocket.listen(25)
    while True: # establish a connection
        clientsocket,addr = serversocket.accept()
        print("Got a connection from %s" % str(addr))

