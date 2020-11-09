from chessboard import *
from engine import *
from megothread import *
from oppogothread import *
import socket
def mainThread():
    '''多线程五子棋的主流程'''
    clientSocket =None
    try:
        clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientSocket.connect(('192.168.55.30', 30000))
        #绑定地址和端口号

        #创建棋盘并初始化
        chessboard = ChessBoard()
        chessboard.initBoard()
        chessboard.printBoard()
        #创建引擎对象
        engine = Engine(chessboard)
        #创建两个棋子对象
        chessmanMe= ChessMan()
        chessmanMe.setColor('x')
        chessmanOppo = ChessMan()
        chessmanOppo.setColor('o')
        #启动两个子线程
        usergo=  MeGoThread(clientSocket,engine,chessmanMe)
        oppogo = OppoGoThread(clientSocket,engine,chessmanOppo)
        oppogo.setDaemon(True)
        usergo.setDaemon(True)
        oppogo.start()
        usergo.start()
        while True:
            # 1 本方wait
            chessmanMe.doWait()
            # 3 在棋盘上摆放用户下棋的棋子
            chessboard.setChessMan(chessmanMe)
            chessboard.printBoard()
            pos = chessmanMe.getPos()
            color = chessmanMe.getColor()
            if engine.isWon(pos, color):
                print('恭喜赢了')
                break
            # 2 对方notify

            chessmanOppo.doNotify()
            # 4 对方wait
            chessmanOppo.doWait()
            # 5 在棋盘上摆放对方下的棋子
            chessboard.setChessMan(chessmanOppo)
            chessboard.printBoard()
            pos = chessmanOppo.getPos()
            color = chessmanOppo.getColor()
            if engine.isWon(pos, color):
                print('呵呵输了')
                break

            #5 本方 notify
            chessmanMe.doNotify()
    except:
        pass
    finally:
        if clientSocket!=None:
            clientSocket.close()
if __name__ =='__main__':
    mainThread()















