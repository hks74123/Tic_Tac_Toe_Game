from tkinter import *

from tkinter import messagebox

screen=Tk()
screen.title('TIC TAC TOE ')
screen.geometry('600x900')
screen.resizable(height=True,width=True)
bcl=True
frame1=Frame(screen,height=100,width=300)
frame1.pack(side='top')
frame2=Frame(screen,height=100,width=300)
frame2.pack(side='top')
frame3=Frame(screen,height=100,width=300)
frame3.pack(side='top')

def game(bs):
    global bcl
    if bs['text']=="" and bcl==True:
        bs['text']='X'
        bcl=False
        if b1['text']=='X' and b2['text']=='X' and b3['text']=='X':
            b1['bg']='yellow'
            b2['bg']='yellow'
            b3['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b1['text']=='O' and b2['text']=='O' and b3['text']=='O':
            b1['bg']='yellow'
            b2['bg']='yellow'
            b3['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b1['text']=='X' and b4['text']=='X' and b7['text']=='X':
            b1['bg']='yellow'
            b4['bg']='yellow'
            b7['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b1['text']=='O' and b4['text']=='O' and b7['text']=='O':
            b1['bg']='yellow'
            b4['bg']='yellow'
            b7['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b1['text']=='X' and b5['text']=='X' and b9['text']=='X':
            b1['bg']='yellow'
            b5['bg']='yellow'
            b9['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b1['text']=='O' and b5['text']=='O' and b9['text']=='O':
            b1['bg']='yellow'
            b5['bg']='yellow'
            b9['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b4['text']=='X' and b5['text']=='X' and b6['text']=='X':
            b4['bg']='yellow'
            b5['bg']='yellow'
            b6['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b4['text']=='O' and b5['text']=='O' and b6['text']=='O':
            b4['bg']='yellow'
            b5['bg']='yellow'
            b6['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b7['text']=='X' and b8['text']=='X' and b9['text']=='X':
            b7['bg']='yellow'
            b8['bg']='yellow'
            b9['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b7['text']=='O' and b8['text']=='O' and b9['text']=='O':
            b7['bg']='yellow'
            b8['bg']='yellow'
            b9['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b2['text']=='X' and b5['text']=='X' and b8['text']=='X':
            b2['bg']='yellow'
            b5['bg']='yellow'
            b8['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b2['text']=='O' and b5['text']=='O' and b8['text']=='O':
            b2['bg']='yellow'
            b5['bg']='yellow'
            b8['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b3['text']=='X' and b6['text']=='X' and b9['text']=='X':
            b3['bg']='yellow'
            b6['bg']='yellow'
            b9['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b3['text']=='O' and b6['text']=='O' and b9['text']=='O':
            b3['bg']='yellow'
            b6['bg']='yellow'
            b9['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b7['text']=='X' and b5['text']=='X' and b3['text']=='X':
            b7['bg']='yellow'
            b5['bg']='yellow'
            b3['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b7['text']=='O' and b5['text']=='O' and b3['text']=='O':
            b7['bg']='yellow'
            b5['bg']='yellow'
            b3['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')

    elif bs['text']=="" and bcl==False:
        bs['text']='O'
        bcl=True
        if b1['text']=='X' and b2['text']=='X' and b3['text']=='X':
            b1['bg']='yellow'
            b2['bg']='yellow'
            b3['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b1['text']=='O' and b2['text']=='O' and b3['text']=='O':
            b1['bg']='yellow'
            b2['bg']='yellow'
            b3['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b1['text']=='X' and b4['text']=='X' and b7['text']=='X':
            b1['bg']='yellow'
            b4['bg']='yellow'
            b7['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b1['text']=='O' and b4['text']=='O' and b7['text']=='O':
            b1['bg']='yellow'
            b4['bg']='yellow'
            b7['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b1['text']=='X' and b5['text']=='X' and b9['text']=='X':
            b1['bg']='yellow'
            b5['bg']='yellow'
            b9['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b1['text']=='O' and b5['text']=='O' and b9['text']=='O':
            b1['bg']='yellow'
            b5['bg']='yellow'
            b9['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b4['text']=='X' and b5['text']=='X' and b6['text']=='X':
            b4['bg']='yellow'
            b5['bg']='yellow'
            b6['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b4['text']=='O' and b5['text']=='O' and b6['text']=='O':
            b4['bg']='yellow'
            b5['bg']='yellow'
            b6['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b7['text']=='X' and b8['text']=='X' and b9['text']=='X':
            b7['bg']='yellow'
            b8['bg']='yellow'
            b9['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b7['text']=='O' and b8['text']=='O' and b9['text']=='O':
            b7['bg']='yellow'
            b8['bg']='yellow'
            b9['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b2['text']=='X' and b5['text']=='X' and b8['text']=='X':
            b2['bg']='yellow'
            b5['bg']='yellow'
            b8['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b2['text']=='O' and b5['text']=='O' and b8['text']=='O':
            b2['bg']='yellow'
            b5['bg']='yellow'
            b8['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b3['text']=='X' and b6['text']=='X' and b9['text']=='X':
            b3['bg']='yellow'
            b6['bg']='yellow'
            b9['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b3['text']=='O' and b6['text']=='O' and b9['text']=='O':
            b3['bg']='yellow'
            b6['bg']='yellow'
            b9['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
        elif b7['text']=='X' and b5['text']=='X' and b3['text']=='X':
            b7['bg']='yellow'
            b5['bg']='yellow'
            b3['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 1 WINS')
        elif b7['text']=='O' and b5['text']=='O' and b3['text']=='O':
            b7['bg']='yellow'
            b5['bg']='yellow'
            b3['bg']='yellow'
            messagebox.showinfo('RESULTS','PLAYER 2 WINS')
    elif bs['text']=='END GAME':
        screen.destroy()
    elif bs['text']=='RESET GAME':
        b1['text']=""
        b2['text']=""
        b3['text']=""
        b4['text']=""
        b5['text']=""
        b6['text']=""
        b7['text']=""
        b8['text']=""
        b9['text']=""
        b1['bg']="white"
        b2['bg']="white"
        b3['bg']="white"
        b4['bg']="white"
        b5['bg']="white"
        b6['bg']="white"
        b7['bg']="white"
        b8['bg']="white"
        b9['bg']="white"

            
bs=StringVar('')
b1=Button(frame1,text='',font='Times 10 bold',bg='white',height=12,width=24,command=lambda:game(b1))
b1.pack(side='left')
b2=Button(frame1,text='',font='Times 10 bold',bg='white',height=12,width=24,command=lambda:game(b2))
b2.pack(side='left')
b3=Button(frame1,text='',font='Times 10 bold',bg='white',height=12,width=24,command=lambda:game(b3))
b3.pack(side='left')
b4=Button(frame2,text='',font='Times 10 bold',bg='white',height=12,width=24,command=lambda:game(b4))
b4.pack(side='left')
b5=Button(frame2,text='',font='Times 10 bold',bg='white',height=12,width=24,command=lambda:game(b5))
b5.pack(side='left')
b6=Button(frame2,text='',font='Times 10 bold',bg='white',height=12,width=24,command=lambda:game(b6))
b6.pack(side='left')
b7=Button(frame3,text='',font='Times 10 bold',bg='white',height=12,width=24,command=lambda:game(b7))
b7.pack(side='left')
b8=Button(frame3,text='',font='Times 10 bold',bg='white',height=12,width=24,command=lambda:game(b8))
b8.pack(side='left')
b9=Button(frame3,text='',font='Times 10 bold',bg='white',height=12,width=24,command=lambda:game(b9))
b9.pack(side='left')
b10=Button(screen,text='END GAME',bg='plum1',height=3,width=12,command=lambda:game(b10))
b10.pack(side='right')
b11=Button(screen,text='RESET GAME',bg='plum1',height=3,width=12,command=lambda:game(b11))
b11.pack(side='right')










