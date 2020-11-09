import engine
import threading
import socket
class  OppoGoThread(threading.Thread):
    '''电脑下棋的线程'''

    def __init__(self,socket,engine,chessmanOppo):
        '''初始化'''
        super(OppoGoThread,self).__init__()
        self.socket = socket
        self.engine = engine
        self.chessmanOppo = chessmanOppo

    def run(self):
        '''子线程执行的代码'''
        try:
            while True:
                # 1 对方wait
                self.chessmanOppo.doWait()
                # 2 接受对方下棋位置
                recvData = self.socket.recv(1024).decode('gbk')
                #对方下棋坐标输出到终端

                self.engine.userGo(self.chessmanOppo,recvData)
                x,y = self.chessmanOppo.getPos()
                print('对方下：%d,%d' % (x, y))
                # 3 对方notify
                self.chessmanOppo.doNotify()
        except:
            pass











