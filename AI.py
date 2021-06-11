#########################################################
#  Last edited on June 21, 2016                         #
#  By Shu Cheng                                         #
#########################################################



from graphics import*
win=GraphWin('五子棋',875,700)
win.setBackground('white')      

p=[[0 for a in range(20)] for b in range(20)]
black=[[0 for a in range(20)] for b in range(20)]
white=[[0 for a in range(20)] for b in range(20)]
q=[[0 for a in range(20)] for b in range(20)]
len=[0 for a in range(4)]
tb=[0 for a in range(4)]
m=[1 for a in range(3)]
n=[1 for a in range(3)]
AI=[[[0 for a in range(16)] for b in range(16)] for c in range(16)]
player=[[[0 for a in range(16)] for b in range(16)] for c in range(16)]


def WinBoard():
 
    for i in range(15):
       for j in range(15):
            p[i+1][j+1]=Point(j*43+43,i*43+43)
    
    for r in range(15):
        Line(p[r+1][1],p[r+1][15]).draw(win)
    for s in range(15):
        Line(p[1][s+1],p[15][s+1]).draw(win)
    center=Circle(p[8][8],3)
    center.draw(win)
    center.setFill('black')

def Click():
  
    while 1:
      p1=win.getMouse()
      x1=p1.getX()
      y1=p1.getY()
      for i in range(15):
         for j in range(15):
             sqrdis=((x1-p[i+1][j+1].getX())*(x1-p[i+1][j+1].getX()))+(y1-p[i+1][j+1].getY())*(y1-p[i+1][j+1].getY())
             if sqrdis<=200 and q[i+1][j+1]==0:
                black[i+1][j+1]=1
                q[i+1][j+1]=Circle(p[i+1][j+1],19.5)
                q[i+1][j+1].draw(win)
                q[i+1][j+1].setFill('black')
               
                return 0


               
def Check():    #判定五子连线

    for i in range(15):     #竖
        for j in range(11):
            if black[i+1][j+1] and black[i+1][j+2] and black[i+1][j+3] and black[i+1][j+4] and black[i+1][j+5]:
               return 1
               break
            if white[i+1][j+1] and white[i+1][j+2]and white[i+1][j+3]and white[i+1][j+4]and white[i+1][j+5]:
               return 2
               break
    for i in range(11):     #横
        for j in range(15):
            if black[i+1][j+1] and black[i+2][j+1]and black[i+3][j+1]and black[i+4][j+1]and black[i+5][j+1]:
               return 1
               break
            if white[i+1][j+1] and white[i+2][j+1]and white[i+3][j+1]and white[i+4][j+1]and white[i+5][j+1]:
               return 2
               break
    for i in range(11):     #右上
        for j in range(11):
            if black[i+1][j+1] and black[i+2][j+2]and black[i+3][j+3]and black[i+4][j+4]and black[i+5][j+5]:
               return 1
               break
            if white[i+1][j+1] and white[i+2][j+2]and white[i+3][j+3]and white[i+4][j+4]and white[i+5][j+5]:
               return 2
               break
    for i in range(11):     #右下
        for j in range(15):
            if black[i+1][j+1] and black[i+2][j]and black[i+3][j-1]and black[i+4][j-2]and black[i+5][j-3]:
               return 1
               break
            if white[i+1][j+1] and white[i+2][j]and white[i+3][j-1]and white[i+4][j-2]and white[i+5][j-3]:
               return 2
               break
   
  

        
def AIcompute():

    for i in range(17):
        q[i][0]=1
        q[i][16]=1
    for j in range(17):
        q[0][j]=1
        q[16][j]=1
    for i in range(15):
        for j in range(15):
            if q[i+1][j+1]!=0:
                for k in range(4):
                    AI[i+1][j+1][k]=1
            if q[i+1][j+1]==0:
                b=j+1
                d=j+1
                while white[i+1][b-1]==1:
                    b=b-1
                while white[i+1][d+1]==1:
                    d=d+1
                len[0]=d-b+1
                if q[i+1][b-1]==0 and q[i+1][d+1]==0:
                    tb[0]=1
                if q[i+1][b-1]!=0 and q[i+1][d+1]==0 or q[i+1][b-1]==0 and q[i+1][d+1]!=0:
                    tb[0]=2
                if q[i+1][b-1]!=0 and q[i+1][d+1]!=0:
                    tb[0]=3
   
                a=i+1
                c=i+1
                while white[a-1][j+1]==1:
                    a=a-1
                while white[c+1][j+1]==1:
                    c=c+1
                len[1]=c-a+1
                if q[a-1][j+1]==0 and q[c+1][j+1]==0:
                    tb[1]=1
                if q[a-1][j+1]!=0 and q[c+1][j+1]==0 or q[a-1][j+1]==0 and q[c+1][j+1]!=0:
                    tb[1]=2
                if q[a-1][j+1]!=0 and q[c+1][j+1]!=0:
                    tb[1]=3
                

                a1=i+1
                a2=i+1
                b1=j+1
                b2=j+1
                while white[a1-1][b1-1]==1:
                    a1=a1-1
                    b1=b1-1
                while white[a2+1][b2+1]==1:
                    a2=a2+1
                    b2=b2+1
                len[2]=a2-a1+1
                if q[a1-1][b1-1]==0 and q[a2+1][b2+1]==0:
                    tb[2]=1
                if q[a1-1][b1-1]!=0 and q[a2+1][b2+1]==0 or q[a1-1][b1-1]==0 and q[a2+1][b2+1]!=0:
                    tb[2]=2
                if q[a1-1][b1-1]!=0 and q[a2+1][b2+1]!=0:
                    tb[2]=3
               

                a1=i+1
                a2=i+1
                b1=j+1
                b2=j+1
                while white[a1-1][b1+1]==1:
                    a1=a1-1
                    b1=b1+1
                while white[a2+1][b2-1]==1:
                    a2=a2+1
                    b2=b2-1
                len[3]=a2-a1+1
                if q[a1-1][b1+1]==0 and q[a2+1][b2-1]==0:
                    tb[3]=1
                if q[a1-1][b1+1]!=0 and q[a2+1][b2-1]==0 or q[a1-1][b1+1]==0 and q[a2+1][b2-1]!=0:
                    tb[3]=2
                if q[a1-1][b1-1]!=0 and q[a2+1][b2+1]!=0:
                    tb[3]=3
                for k in range(4):
                    AI[i+1][j+1][k]=tb[k]*10+len[k]

        
                
def playercompute():

    for i in range(17):
        q[i][0]=1
        q[i][16]=1
    for j in range(17):
        q[0][j]=1
        q[16][j]=1
    for i in range(15):
        for j in range(15):
            if q[i+1][j+1]!=0:
                for k in range(4):
                    player[i+1][j+1][k]=1

            if q[i+1][j+1]==0:
                b=j+1
                d=j+1
                while black[i+1][b-1]==1:
                    b=b-1
                while black[i+1][d+1]==1:
                    d=d+1
                len[0]=d-b+1
                if q[i+1][b-1]==0 and q[i+1][d+1]==0:
                    tb[0]=1
                if q[i+1][b-1]!=0 and q[i+1][d+1]==0 or q[i+1][b-1]==0 and q[i+1][d+1]!=0:
                    tb[0]=2
                if q[i+1][b-1]!=0 and q[i+1][d+1]!=0:
                    tb[0]=3
               
               
                a=i+1
                c=i+1
                while black[a-1][j+1]==1:
                    a=a-1
                while black[c+1][j+1]==1:
                    c=c+1
                len[1]=c-a+1
                if q[a-1][j+1]==0 and q[c+1][j+1]==0:
                    tb[1]=1
                if q[a-1][j+1]!=0 and q[c+1][j+1]==0 or q[a-1][j+1]==0 and q[c+1][j+1]!=0:
                    tb[1]=2
                if q[a-1][j+1]!=0 and q[c+1][j+1]!=0:
                    tb[1]=3
          
                a1=i+1
                a2=i+1
                b1=j+1
                b2=j+1
                while black[a1-1][b1-1]==1:
                    a1=a1-1
                    b1=b1-1
                while black[a2+1][b2+1]==1:
                    a2=a2+1
                    b2=b2+1
                len[2]=a2-a1+1
                if q[a1-1][b1-1]==0 and q[a2+1][b2+1]==0:
                   tb[2]=1
                if q[a1-1][b1-1]!=0 and q[a2+1][b2+1]==0 or q[a1-1][b1-1]==0 and q[a2+1][b2+1]!=0:
                   tb[2]=2
                if q[a1-1][b1-1]!=0 and q[a2+1][b2+1]!=0:
                   tb[2]=3
          

                a1=i+1
                a2=i+1
                b1=j+1
                b2=j+1
                while black[a1-1][b1+1]==1:
                    a1=a1-1
                    b1=b1+1
                while black[a2+1][b2-1]==1:
                    a2=a2+1
                    b2=b2-1
                len[3]=a2-a1+1
                if q[a1-1][b1+1]==0 and q[a2+1][b2-1]==0:
                    tb[3]=1
                if q[a1-1][b1+1]!=0 and q[a2+1][b2-1]==0 or q[a1-1][b1+1]==0 and q[a2+1][b2-1]!=0:
                    tb[3]=2
                if q[a1-1][b1-1]!=0 and q[a2+1][b2+1]!=0:
                    tb[3]=3
                for k in range(4):
                    player[i+1][j+1][k]=tb[k]*10+len[k]
           
def score():

    for i in range(15):
        for j in range(15):
            AI[i+1][j+1][4]=0
            player[i+1][j+1][4]=0
            for k in range(4):
                if AI[i+1][j+1][k]==22:
                    AI[i+1][j+1][4]=10
                if player[i+1][j+1][k]==22:
                    player[i+1][j+1][4]=10
            for k in range(4):
                for l in range(k+1,4):
                    if AI[i+1][j+1][k]==22 and AI[i+1][j+1][l]==22:
                       AI[i+1][j+1][4]=15
                    if player[i+1][j+1][k]==22 and player[i+1][j+1][l]==22:
                       player[i+1][j+1][4]=15
            for k in range(4):
                if AI[i+1][j+1][k]==12:
                   AI[i+1][j+1][4]=20
                if player[i+1][j+1][k]==12:
                   player[i+1][j+1][4]=20
            for k in range(4):
                if AI[i+1][j+1][k]==23:
                   AI[i+1][j+1][4]=30
                if player[i+1][j+1][k]==23:
                   player[i+1][j+1][4]=30
            for k in range(4):
                 for l in range(k+1,4):
                    if AI[i+1][j+1][k]==12 and AI[i+1][j+1][l]==12:
                       AI[i+1][j+1][4]=40
                    if player[i+1][j+1][k]==12 and player[i+1][j+1][l]==12:
                       player[i+1][j+1][4]=40
            for k in range(4):
                 for l in range(k+1,4):
                    if AI[i+1][j+1][k]==12 and AI[i+1][j+1][l]==23 or AI[i+1][j+1][k]==12 and AI[i+1][j+1][l]==23:
                       AI[i+1][j+1][4]=45
                    if player[i+1][j+1][k]==23 and player[i+1][j+1][l]==12 or player[i+1][j+1][k]==12 and player[i+1][j+1][l]==23:
                       player[i+1][j+1][4]=45
            for k in range(4):
                 for l in range(k+1,4):
                    if AI[i+1][j+1][k]==13:
                       AI[i+1][j+1][4]=50
                    if player[i+1][j+1][k]==13:
                       player[i+1][j+1][4]=50
            for k in range(4):
                 for l in range(k+1,4):
                    if AI[i+1][j+1][k]==24:
                       AI[i+1][j+1][4]=60
                    if player[i+1][j+1][k]==24:
                       player[i+1][j+1][4]=50
            for k in range(4):
                 for l in range(k+1,4):
                    if AI[i+1][j+1][k]==13 and AI[i+1][j+1][l]==12 or AI[i+1][j+1][k]==12 and AI[i+1][j+1][l]==13:
                       AI[i+1][j+1][4]=65
                    if player[i+1][j+1][k]==13 and player[i+1][j+1][l]==12 or player[i+1][j+1][k]==12 and player[i+1][j+1][l]==13:
                       player[i+1][j+1][4]=55
            for k in range(4):
                 for l in range(k+1,4):
                    if AI[i+1][j+1][k]==23 and AI[i+1][j+1][l]==13 or AI[i+1][j+1][k]==13 and AI[i+1][j+1][l]==23:
                       AI[i+1][j+1][4]=70
                    if player[i+1][j+1][k]==23 and player[i+1][j+1][l]==13 or player[i+1][j+1][k]==13 and player[i+1][j+1][l]==23:
                       player[i+1][j+1][4]=70
            for k in range(4):
                 for l in range(k+1,4):
                    if AI[i+1][j+1][k]==13 and AI[i+1][j+1][l]==13:
                       AI[i+1][j+1][4]=80
                    if player[i+1][j+1][k]==13 and player[i+1][j+1][l]==13:
                       player[i+1][j+1][4]=80
            for k in range(4):
                if AI[i+1][j+1][k]==14:
                       AI[i+1][j+1][4]=90
                if player[i+1][j+1][k]==14:
                       player[i+1][j+1][4]=90
            for k in range(4):
                for l in range(4):
                    if AI[i+1][j+1][k]==24 and AI[i+1][j+1][l]==13 or AI[i+1][j+1][k]==13 and AI[i+1][j+1][l]==24:
                            AI[i+1][j+1][4]=90
                    if player[i+1][j+1][k]==24 and player[i+1][j+1][l]==13 or player[i+1][j+1][k]==13 and player[i+1][j+1][l]==24:
                            player[i+1][j+1][4]=90
            for k in range(4):
                for l in range(4):
                    if AI[i+1][j+1][k]==24 and AI[i+1][j+1][l]==24:
                       AI[i+1][j+1][4]=90
                    if player[i+1][j+1][k]==24 and player[i+1][j+1][l]==24:
                       player[i+1][j+1][4]=90
            for k in range(4):
                if AI[i+1][j+1][k]%5==0:
                   AI[i+1][j+1][4]=100
                if player[i+1][j+1][k]%5==0:
                   player[i+1][j+1][4]=100

    
    for i in range(15):
        for j in range(15):
             if AI[m[1]][n[1]][4]<AI[i+1][j+1][4]:
                if q[i+1][j+1]==0:
                   m[1]=i+1
                   n[1]=j+1
             if player[m[2]][n[2]][4]<player[i+1][j+1][4]:
                if q[i+1][j+1]==0:
                   m[2]=i+1
                   n[2]=j+1
    m[0]=m[2]
    n[0]=n[2]
    if AI[m[1]][n[1]][4]>=player[m[2]][n[2]][4]:
       m[0]=m[1]
       n[0]=n[1]
   

def AIput():
   
    white[m[0]][n[0]]=1
    q[m[0]][n[0]]=Circle(p[m[0]][n[0]],19.5)
    q[m[0]][n[0]].draw(win)
    q[m[0]][n[0]].setFill('white')
    
    for i in range(15):
        for j in range(15):
            for k in range(5):
                AI[i+1][j+1][k]=0
                player[i+1][j+1][k]=0
    for i in range(4):
        tb[i]=0
        len[i]=0
     
               
   
def computeree():
   
    WinBoard()
    while 1:
        Click()
        Check()
        if Check()==1:
            rec=Rectangle(Point(240,240),Point(450,450))
            rec.setFill('green')
            rec.draw(win)
            Text(Point(350,350),'the black is the winner').draw(win)
            break
        if Check()==2:
            rec=Rectangle(Point(240,240),Point(450,450))
            rec.setFill('green')
            rec.draw(win)
            Text(Point(350,350),'the white is the winner').draw(win)
            break
        AIcompute()
        playercompute()
        score()
        AIput()
        Check()
        if Check()==1:
            rec=Rectangle(Point(240,240),Point(450,450))
            rec.setFill('green')
            rec.draw(win)
            Text(Point(350,350),'the black is the winner').draw(win)
            break
        if Check()==2:
            rec=Rectangle(Point(240,240),Point(450,450))
            rec.setFill('green')
            rec.draw(win)
            Text(Point(350,350),'the white is the winner').draw(win)
            break
    win.getMouse()
    win.close()
    return 0

computeree()
