class port:
    def __init__(self):
        self.port = ''

    def setPort(self, port):
        self.port = port
        print(self.port, 'set')

    def getPort(self):
        return self.port
        print(self.port, 'get')