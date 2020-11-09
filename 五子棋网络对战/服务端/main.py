from chessboard import *
from engine import *
from megothread import *
from oppogothread import *
import socket
def mainThread():
    '''多线程五子棋的主流程'''
    serverSocket =None
    print('正在等待对方连接')
    try:
        serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        serverSocket.bind(('', 30000))
        serverSocket.listen(5)
        clientSocket, clientInfo = serverSocket.accept()
        #绑定地址和端口号

        #创建棋盘并初始化
        chessboard = ChessBoard()
        chessboard.initBoard()
        chessboard.printBoard()
        #创建引擎对象
        engine = Engine(chessboard)
        #创建两个棋子对象
        chessmanMe= ChessMan()
        chessmanMe.setColor('o')
        chessmanOppo = ChessMan()
        chessmanOppo.setColor('x')
        #启动两个子线程
        usergo=  MeGoThread(clientSocket,engine,chessmanMe)
        oppogo = OppoGoThread(clientSocket,engine,chessmanOppo)
        oppogo.setDaemon(True)
        usergo.setDaemon(True)
        oppogo.start()
        usergo.start()
        while True:
            # 1 对方wait
            chessmanOppo.doWait()
            # 3 在棋盘上摆放用户下棋的棋子
            chessboard.setChessMan(chessmanOppo)
            chessboard.printBoard()
            pos = chessmanOppo.getPos()
            color = chessmanOppo.getColor()
            if engine.isWon(pos, color):
                print('你输了')
                break
            # 2 本方notify

            chessmanMe.doNotify()
            # 4 本方wait
            chessmanMe.doWait()
            # 5 在棋盘上摆放下的棋子
            chessboard.setChessMan(chessmanMe)
            chessboard.printBoard()
            pos = chessmanMe.getPos()
            color = chessmanMe.getColor()
            if engine.isWon(pos, color):
                print('恭喜赢了')
                break

            #5 对方 notify
            chessmanOppo.doNotify()
    except:
        pass
    finally:
        if serverSocket!=None:
            serverSocket.close()
if __name__ =='__main__':
    mainThread()















