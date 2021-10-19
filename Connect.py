import socket
def connect():
    connection = False
    print("attempting connection...")
    while connection == False:
        try:
            s = socket.socket() # Create a socket object 
            host = socket.gethostname() # Get local machine name 
            port = 8000 # Reserve a port for your service. 
            s.connect((host, port))
            connection = True
            print("connected successfully")
        except:
            connection = False