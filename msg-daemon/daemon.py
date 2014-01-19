"""
The daemon which listens to messages from 
the underlying network.
Note: Currently a UDP server. TODO: Use APRS
"""

import constants
import socket 

class MessageDaemon:
    BUF_SZ = constants.MAX_MSG_SZ

    def __init__(self, ip, port):
        self.host_ip = ip
        self.host_port = port

    """
    Process received message
    """
    def _dispatch(self, msg):
        print "Received %s" % msg
    
    """
    Create a UDP socket and bind to
    specified host:port
    """
    def _connect(self):
        #Create socket
        self.sock = socket.socket(  socket.AF_INET,
                                    socket.SOCK_DGRAM)
        # Set socket options
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if self.sock is not None:
            self.sock.bind((self.host_ip, self.host_port))
        else:
            return -1
    
    """
    Receive a message
    """
    def _recv(self):
        data, addr = self.sock.recvfrom(self.BUF_SZ)
        if data != "":
            return data
        else: 
            return None

    """
    Start the message daemon
    """
    def start(self):
        self._connect()
        while 1:
            msg = self._recv()
            if msg is not None:
                self._dispatch(msg)
            
    def stop():
        # Clean up
        self.sock.shutdown()
        self.sock.close()
        pass
    
    # Getters and Setters
    def set_buf_size(new_sz):
        self.BUF_SZ = new_sz

if __name__ == "__main__":
    daemon = MessageDaemon("127.0.0.1",12345)
    daemon.start()
