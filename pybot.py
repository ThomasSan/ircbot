import socket

class IRC:
    irc = socket.socket()

    def __init__(self):
        irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " " + msg + "\n")

    def connect(self, server, channel, botnick):
        print "connection to : " + server
        self.irc.connect((server, 6667))
        self.irc.send("USER " + botnick + " " + botnick + " " + botnick + " " + botnick + "\r\n")
        self.irc.send("NICK " + botnick + "\r\n")
        self.irc.send("JOIN " + channel + "\r\n")

    def get_text(self):
        text = self.irc.recv(2048)

        if text.find('PING') != -1:
            self.irc.send('PONG ' + text.split()[1] + "\r\n")

        return text

