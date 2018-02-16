class Number:
    def __init__(self,sl):
        self.sl=sl

class Empty:
    def __init__(self,x,y,sl):
        self.name = 'Empty'
        self.x = x
        self.y = y
        self.sl = sl

class Rook:
    def __init__(self,x,y,sl):
        self.name = 'Rook'
        self.x = x
        self.y = y
        self.sl = sl
        

class Pawn:
    def __init__(self,x,y,sl):
        self.name = 'Pawn'
        self.x = x
        self.y = y
        self.sl = sl

     

class Chess_Board:
    def __init__(self):
        self.board = [[Empty(x='',y='',sl='.')]*9 for _ in range(9)]

        self.board[1][1] = Rook(x=1,y=1,sl='R')
        self.board[2][2] = Pawn(x=2,y=2,sl='P')
       
        for i in range(9):
            self.board[i][8 ]= Number(sl=i)
        for j in range(9):
            self.board[8][j] = Number(sl=j)

    def display(self):
        for i in range(9):
            for j in range(9):
                print (self.board[i][j].sl, end=' ')
            print()

        
    def path1_mov1(self):
        self.mov1 = 'mov1'
        self.board[1][1] = Empty(x='',y='',sl='.')
      
        self.board[2][1] = Rook(x=2,y=1,sl='R')
        self.board[2][2] = Pawn(x=2,y=2,sl='P')
        print('First move of Rook and Pawn cant move')
        
    def path1_mov2(self):
        self.mov2 = 'mov2'
        self.board[2][1] = Empty(x='',y='',sl='.')
        self.board[2][2] = Rook(x=2,y=2,sl='R')
    def path2_mov1(self):
        self.mov1 = 'mov1'
        self.board[1][2] = Rook(x=1,y=2,sl='R')
        self.board[2][2] = Pawn(x=2,y=2,sl='P')
        print('Rook first move')
    def path2_mov11(self):
        
        self.board[1][1] = Empty(x='',y='',sl='.')
        self.board[1][2] = Rook(x=1,y=2,sl='R')
        self.board[2][1] = Pawn(x=2,y=1,sl='P')
        print('Pawn first move')
    def path2_mov2(self):
        self.mov2 = 'mov2'
        self.board[1][2] = Empty(x='',y='',sl='.')
        self.board[2][2] = Rook(x=2,y=2,sl='R')
        self.board[2][1] = Pawn(x=2,y=1,sl='P')
        print('Rook second move')
    def path2_mov21(self):
        self.mov21 = 'mov21'
        self.board[2][1] = Empty(x='',y='',sl='.')
        self.board[2][2] = Rook(x=2,y=2,sl='R')
        self.board[2][1] = Pawn(x=2,y=0,sl='P')
        print('Pawn second move')
    def path2_mov3(self):
        self.mov3 = 'mov3'
        self.board[2][2] = Empty(x='',y='',sl='.')
        self.board[2][1] = Empty(x='',y='',sl='.')
        self.board[2][0] = Rook(x=2,y=0,sl='R')
        print('Rook kill pawn at third move')
        

                 
        
a=Chess_Board()
a.display()
print('give path1 = 1 and path2 = 2')
try:
    path1 = int(input())
except:
    print('Coordinates can only be integers and must lie between(1,2)')

##        path2 = int(input())
if path1 == 1:
    a.path1_mov1()
    a.display()
    print('second move . "Rook killed Pawn"')
    a.path1_mov2()
    a.display()
    print('Numbers of moves for Rook in case of path1 = 2')
elif path1 == 2:
    a.path2_mov2()
    a.display()
    a.path2_mov21()
    a.display()
    a.path2_mov3()
    a.display()
    print('Numbers of moves for Rook in case of path2 = 3')
##else:
##    break 
    
       

print('''\n\n\npath1 ::- minimum numbers of moves for Rook to kill Pawn = 2 .''')




