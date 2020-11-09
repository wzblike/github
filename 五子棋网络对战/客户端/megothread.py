import threading
import engine
import socket
class MeGoThread(threading.Thread):
    '''用户下棋的线程'''


    def __init__(self,socket,engine,chessmanMe):
        '''初始化'''
        super(MeGoThread,self).__init__()
        self.socket = socket
        self.engine = engine
        self.chessmanMe = chessmanMe


    def run(self):
        '''子线程执行的代码'''
        try:
            while True:
                #1 用户下棋
                userInput = input('请输入下棋坐标：')
                self.engine.userGo(self.chessmanMe,userInput)
                #通过网络通知对方下棋坐标
                self.socket.send(userInput.encode('gbk'))

                #2 用户notify
                self.chessmanMe.doNotify()

                #3 用户wait
                self.chessmanMe.doWait()
        except:
            pass



















