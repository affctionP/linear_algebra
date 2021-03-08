from tkinter import *
from numpy import *
import numpy as np
import sympy as sy

root=Tk()
root.title("JABRE KHATI")
root.resizable(1,1)
title_f=Frame(root)
title_f.pack(side=TOP)

head_l=Label(title_f,text="تعداد سطرها و ستون ها را وارد کنيد و کليد ماتريس را فشار دهيد",font=('arial',20),bg="#aadd54")
head_l.pack(fill=X)
t=Label(title_f,text="توجه کنيد فيلد هارا خالي نگذاريد ومقادير حقيقي وارد کنيد",font=('arial',16),bg='red')
t.pack(fill=X)
ROW=StringVar()
COLUMN=StringVar()
r_l=Label(title_f,text="سطر:",font=('arial',16))
r_l.pack(side=LEFT)
r_e=Entry(title_f,textvariable=ROW)
r_e.pack(side=LEFT)
C_l=Label(title_f,text=":ستون",font=('arial',16))
C_l.pack(side=RIGHT)
c_e=Entry(title_f,textvariable=COLUMN)
c_e.pack(side=RIGHT)


def maketable():

    vors =[]
    for i in range (int(ROW.get())):
      for j in range(int(COLUMN.get())):
        vors.append(StringVar())
        en=Entry(m_frame,textvariable=vors[-1])
        en.grid(column=j,row=i)



        
    def mohasebeh():
        r=int(ROW.get())
        c=int(COLUMN.get())
        b=zeros((r,c))
        i=0
        j=0
        k=0
        g=0
        p=1
        while (i<=(r*c)-1):
            for k in range (c):
                b[j][k]=float(vors[i].get())
                i=i+1
            j=j+1

        def cheek(m,n,o):
          while (m+o<r):
           if(b[m][n]==0):
               t=b[m]
               b[m]=b[m+o]
               b[m+o]=t
               cheek(m,n,o+1)
           else:
                return 1;
        
        for k in range (r):
           if(cheek(k,g,p)):
              b[k]=b[k]/b[k][g]#float shoud be
              for v in range (k+1,r):
                 b[v]=b[v]-(b[v][g]*b[k])
           else:
               g+1
               if(cheek(k,g,p)):
                 b[k]=b[k]/b[k][g]#float shoud be
                 for v in range (k+1,r):
                     b[v]=b[v]-(b[v][g]*b[k])
           g=g+1
        
        result=Tk()
        result.title("نتيجه")
        re_f=Label(result,text=str(b),font=('arial', 18))


        re_f.pack(fill=X)
            
  

    def vijeh():
        r=int(ROW.get())
        c=int(COLUMN.get())
        b=zeros((r,c))
        i=0
        j=0
        k=0
        q=np.zeros((r,r))
        while (i<=(r*c)-1):
            for k in range (c):
                b[j][k]=float(vors[i].get())
                i=i+1
            j=j+1
        y=sy.Symbol("y")
        hamani=np.identity(r)
        v=(b-(hamani*y))
        def hazf(array,sa,so):
            tm=array
            tm=list (tm[:sa])+list (tm[sa+1:])
            for z in range (0,len(tm)):
                tm[z]=list(tm[z][:so])+list(tm[z][so+1:])
            return tm

        def determinan(ar,lens):
           if lens==1:return ar[0][0]
           if lens==2:return (ar[0][0]*ar[1][1]-ar[0][1]*ar[1][0])
           sumi=0
           for tedad in range (0,lens):
               ha=hazf(ar,0,tedad)
               sumi=sumi+((-1)**tedad)*ar[0][tedad]*determinan(ha,lens-1)
           return sumi
        moadeleh=determinan(v,r)
        result=sy.solve(moadeleh)
        u=Tk()
        u.title("نتيجه")
        f=Label(u,text=str(result),font=('arial', 18),bg='orange')
        f.pack()


    h_b=Button(m_frame,text="محاسبه ماتريس پلکاني",bg='pink',command=mohasebeh)
    h_b.grid(column=0,row=int(COLUMN.get())+3)
    vi_b=Button(m_frame,text="محاسبه مقادير ويژه",bg='yellow',command=vijeh)
    vi_b.grid(column=0,row=int(COLUMN.get())+6)
  
m_b=Button(title_f,text="ماتريس",bg='blue',command=maketable)
m_b.pack()
m_frame=Frame(root)
m_frame.pack(side=TOP)
if __name__ == '__main__':
    root.mainloop()
