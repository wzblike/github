import random
from chessman import *
import re
from chessboard import *
class Engine(object):
    def __init__(self,chessboard):
        self.__chessboard = chessboard

    def computerGo(self,chessman):
        if not isinstance(chessman,ChessMan):
            raise Exception('第一个参数必须为chessman对象')
        '''
        电脑下棋 把下棋的位置写入chessman对象中
        :param chessman: 棋子对象 里面已经设置好棋子的颜色
        :return: 
        '''
        while True:

            posX = random.randint(1,15)#[1,15]1到15
            posY = random.randint(1,15)#[1,15]1到15
            #判断该位置是否为空
            if self.__chessboard.isEmpty((posX,posY)):
                print('电脑下棋的位置：',(posX,posY))
                #如果该位置为空 则把posx和posY写入棋子的位置中
                chessman.setPos((posX,posY))
                #退出while循环
                break

    def userGo(self,chessman,userInput):
        '''
        用户下棋 读取用户输入的字符串 并把下棋的位置写入chessman对象中
        :param chessman: 棋子对象 里面已经设置了棋子的颜色
        :param userInput: 用户输入下棋的坐标1-15，a-o
        :return:False不能正常下棋 True能够下棋
        '''
        if not isinstance(chessman,ChessMan):
            raise Exception('第一个参数必须为chessman对象')

        pattern = '^([1-9]|1[0-5]),([a-o])$'
        ret = re.findall(pattern,userInput)
        if len(ret):
            posX,posY = ret[0]
            posX = int(posX)
            posY = ord(posY) - ord('a') + 1
            print('用户下棋的位置：', (posX, posY))
            #判断该位置是否为空
            if self.__chessboard.isEmpty((posX,posY)):
                # 如果该位置为空 则把posx和posY写入棋子的位置中
                chessman.setPos((posX, posY))
                return True

        #输入格式不正确或位置非空
        return False

    def isWon(self,pos,color):
        '''
        判断当下某一颗棋子是否赢钱
        :param pos:下棋的位置
        :param color:棋子的颜色
        :return:TRUE胜负已分 false胜负未分
        '''
        if not isinstance(pos,tuple) and not isinstance(pos,list):
            raise Exception('第一个参数必须为元组或者列表')
        if pos[0] <= 0 or pos[0] > ChessBoard.BOARD_SIZE:
            raise Exception('下标越界')
        if pos[1] <= 0 or pos[1] > ChessBoard.BOARD_SIZE:
            raise Exception('下标越界')

        #上下方向(posX-4,posY)-(posX+4,posY)
        startX = 1 # 开始遍历的位置
        if pos[0] - 4 > 1:
            startX = pos[0] - 4
        endX = ChessBoard.BOARD_SIZE#结束遍历的x位置
        if pos[0] + 4 < ChessBoard.BOARD_SIZE:
            endX = pos[0] + 4
        count = 0 # 统计有多少颗棋子连在一起

        for posX in range(startX,endX + 1):
            if self.__chessboard.getChess((posX,pos[1])) == color:
                count += 1
                if count >= 5:
                    return True

            else:#一旦断开 则统计计数清0
                count = 0


        #左右方向
        startY = 1  # 开始遍历的位置
        if pos[1] - 4 > 1:
            startY = pos[1] - 4
        endY = ChessBoard.BOARD_SIZE  # 结束遍历的y位置
        if pos[1] + 4 < ChessBoard.BOARD_SIZE:
            endY = pos[1] + 4
        count = 0  # 统计有多少颗棋子连在一起

        for posY in range(startY,endY + 1):
            if self.__chessboard.getChess((pos[0], posY)) == color:
                count += 1
                if count >= 5:
                    return True

            else:  # 一旦断开 则统计计数清0
                count = 0

        # 左上右下方向
        count = 0
        s = pos[0] - pos[1]
        start = startX
        end = endY + s
        if pos[0] > pos[1]:
            start = startY + s
            end = endX
        for index in range(start, end + 1):
            if self.__chessboard.getChess((index, index - s)) == color:
                count += 1
                if count >= 5:
                    return True
            else:
                # 一旦断开 统计数清0
                count = 0

        # 左下右上方向
        count = 0
        s = pos[0] + pos[1]
        if pos[0] + pos[1] <= 16:
            start = startX
            end = s - startY

        if pos[0] + pos[1] > 16:
            start = s - startY
            end = startX

        if s >= 6 and s <= 12:
            for index in range(start, end + 1):
                if self.__chessboard.getChess((index, s - index)) == color:
                    count += 1
                    if count >= 5:
                        return True
                else:
                    # 一旦断开 统计数清0
                    count = 0
        #四个方向都找不到连续5颗相同颜色的棋子 则游戏继续

        return False

    def isWonMan(self,chessman):
        '''
        判断在棋盘上放置chessman是否赢棋
        :param chessman:放置的棋子位置和颜色
        :return:TRUE胜负已分 false胜负未分
        '''
        if not isinstance(chessman,ChessMan):
            raise Exception('第一个参数必须为chessman对象')
        pos = chessman.getPos()
        color = chessman.getColor()
        return self.isWon(pos,color)



