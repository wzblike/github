
import threading
class ChessMan(object):
    '''棋子类'''


    def __init__(self):
        self.pos = [0,0]
        self.__color ='+'
        # 初始化Condition
        self.con = threading.Condition()
    def setPos(self,pos):
        '''指定棋子的位置'''
        self.__pos = pos

    def getPos(self):
        '''返回棋子的位置'''
        return self.__pos

    def setColor(self,color):
        '''指定棋子的颜色'''
        self.__color = color

    def getColor(self):
        '''返回棋子的颜色'''
        return self.__color

    def doNotify(self):
        self.con.acquire()#获取锁
        self.con.notify()#唤醒download中的wait
        self.con.release()#释放锁
    def doWait(self):
        self.con.acquire()#获取锁
        self.con.wait()#等待upload中的notify唤醒
        self.con.release()#释放锁


