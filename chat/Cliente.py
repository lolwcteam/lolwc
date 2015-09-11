import xmpp

class Cliente(object):
    friends = None
    state = None
    server = None
    user = None
    password = None
    connected = None
    connection = None
    roster = None

    def __init__(self, user, password, server):
        self.user = user
        self.password = password
        self.setServer(server)
        connect = self.connect()
        if connect != "connect stablished":
            self.connected = False
        else:
            self.connected = True

    def setServer(self, server):
        serverList = {"br":"br1",
                      "eune":"eun1",
                      "euw":"euw1",
                      "kr":"kr",
                      "lan":"la1",
                      "las":"la2",
                      "na":"na1",
                      "oce":"oc1",
                      "tr":"tr1",
                      "ru":"ru",
                      "pbe":"pbe1"}
        self.server = serverList[server]

    def connect(self):
        self.conn = xmpp.Client("pvp.net")
        if not self.conn.connect(server=("chat."+self.server+".lol.riotgames.com", 5223)):
            return "connect failed":
        if not self.conn.auth(self.user, "AIR_" + self.password, "xiff"):
            return "auth failed."
        return "connect stablished"
        conn.RegisterHandler("message", self.recvMessage)
        conn.sendInitPresence(requestRoster=1)
        self.roster = self.conn.getRoster()

    def recvMessage(self, conn, msg):
        user = roster.getName(str(msg.getFrom()))
        text = msg.getBody()
        print "[%s] %s" % (user, text)
        self.sendReply(conn, msg, text)

    def sendReply(self, conn, msg, text):
        reply = msg.buildReply("[ECHO] %s" % (text))
        reply.setType("chat")
        self.conn.send(reply)
