"""

klasse arduino vanuit  oogpunt van layout

    mockup voorbeeld                                     wat moet het doen      done/moeilijkheden
    poort weergeven                                      return                 gedaan
    naam weergeven                                       return                 gedaan
    oprol                                                static variable        weet niet hoe static werkt
    uitrol de maximale uitrol afstand                    aanpasbare variable    gedaan
    status waar is de arduino mee bezig                  return                 gedaan
    licht kan 3 waarden hebben "bright, light or dim"    return                 gedaan
    temperatuur weergaven                                return                 gedaan
    automatisch                                          ????                   ik weet niet hoe dit eruit moet zien
    handmatig                                            ????                   ik weet niet hoe dit eruit moet zien
    vergrendelen                                         ????                   ik weet niet hoe dit eruit moet zien

"""

listLight = ["bright", "light", "dim"]


class Arduino:

    rollUp = 0.05
    rollDown = 1
    tempeture = 20
    status = "bezig"

    def __init__(self, name, port, listLight):
        self.name = name
        self.port = port
        self.listLight = listLight

    def returnName(self):
        return self.name

    def returnPort(self):
        return self.port

    def returnRollUp(self):
        return self.rollUp

    def returnRollDown(self):
        return self.rollDown

    def returnLight(self):
        return self.listLight

    def returnTempeture(self):
        return self.tempeture

    def returnStatus(self):
        return self.status


test = Arduino('test', '2', listLight[1])

print(test.returnStatus())
