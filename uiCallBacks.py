import sys
#Adds path, so we can add modules that are present in the folder
sys.path.insert(0, 'C:\\Users\\Ahmad\\OneDrive\\School\\Mech46x\\wirlessDataTransfer')

from dataTransferServer import *

class UICallBacks:
    def __init__(self):
    	pass
		# self._msgServerThread = msgServer(dataTransferMode.BLUETOOTH, commonBTAdress.RASPBERRYBTADDR)
		# self._msgServerThread.start()    	
        
    def onConnectButton(self): 
        self._msgServerThread.connectToClientBT()


#def onDataRecieve()