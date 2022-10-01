from tkinter import *
import tkinter.messagebox
import random
main_window=Tk()
main_window.title('Encrypt & Decrypt')
p=PhotoImage(file="en and de.png")
main_window.iconphoto(False,p)
main_window.configure(bg='#8ED6EA')
main_window.geometry("445x430")
my_font=('Georgia',13,'bold')
main_window.resizable(False, False)
my_font1=('Segoe UI Historic',12)
primes=[]
for s in range(17,150):
    if s>1:
        for t in range(2,s):
            if(s%t==0):
                break
        else:
            primes.append(s)
x=random.randint(0,len(primes))
p=primes[x]
primes.remove(p)
y=random.randint(0,len(primes))
q=primes[y]
e=2
n=p*q
phi=(p-1)*(q-1)
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
while(e<phi):
    if(gcd(phi,e)==1):
        break
    else:
        e=e+1
def modinv(a,m):
	g,x,y = egcd(a,m)
	if g!= 1:
		return None
	else:
		return x%m
def egcd(a,b):
	if a==0:
		return (b,0,1)
	else:
		g,y,x=egcd(b%a,a)
		return (g,x-(b//a)*y,y)
d=modinv(e,phi)
Label(main_window,text="",bg='#8ED6EA').grid(row=1,column=0)
Label(main_window,text="Enter the text to be encrypted or decrypted",bg='#8ED6EA',font=my_font).grid(row=2,column=0,columnspan=10)
text=Text(main_window,borderwidth=2,width=30,height=8,font=my_font1)
text.grid(row=3,column=0,padx=70,pady=10,columnspan=10)
Label(main_window,text=f"Public Key={n} {e}",font=my_font1,bg='#8ED6EA').grid(row=4,column=0)
Label(main_window,text=f"Private Key={n} {d}",font=my_font1,bg='#8ED6EA').grid(row=4,column=1)
Label(main_window,text="Enter the password",font=my_font,bg='#8ED6EA').grid(row=5,column=0,columnspan=10)
pasw=Entry(main_window,width=15,borderwidth=1,show='*',font=my_font)
pasw.grid(row=6,column=0,columnspan=10,pady=10)
def encrypt():
    pas=pasw.get()
    if(pas=='surajk'):
        plain_text=text.get(1.0,END)
        ascii=[]
        en=[]
        for i in plain_text:
            ascii.append(ord(i))
        for j in ascii:
            c=pow(j,e)
            c=c%n
            en.append(c)
        a = Tk()
        a.title("Encrypted Message")
        a.geometry("300x240")
        a.resizable(False, False)
        a.configure(bg="#FE8CF7")
        Label(a,text="Encrypted Message",bg="#FE8CF7",font=my_font).grid(row=0,column=0)
        texten = Text(a,width=25,height=7,font=my_font1)
        texten.grid(row=1, column=0,padx=30,pady=10)
        for i in en:
            texten.insert(END,str(i)+" ")
    else:
        tkinter.messagebox.showerror("Encrypt","Incorrect Password")
    pasw.delete(0,'end')
def decrypt():
    pas=pasw.get()
    if(pas=='surajk'):
        de=[]
        plain_text=text.get(1.0,END)
        plain_text=plain_text.split()
        plain_text=[int(x) for x in plain_text]
        for i in plain_text:
            l=pow(i,d)
            l=int(l%n)
            de.append(l)
        res = ''.join(chr(val) for val in de)
        b=Tk()
        b.title("Decrypted Message")
        b.geometry("300x240")
        b.configure(bg="#FC994C")
        b.resizable(False, False)
        Label(b, text="Decrypted Message",bg="#FC994C", font=my_font).grid(row=0, column=0)
        textde = Text(b, width=25, height=7, font=my_font1)
        textde.grid(row=1, column=0, padx=30, pady=10)
        textde.insert(END,res)
    else:
        tkinter.messagebox.showerror("Decrypt", "Incorrect Password")
    pasw.delete(0,'end')
encry=Button(main_window,text="ENCRYPT",bg="#FE8CF7",command=encrypt)
encry.grid(row=7,column=0,pady=10,padx=80)
decry=Button(main_window,text="DECRYPT",bg="#FC994C",command=decrypt)
decry.grid(row=7,column=1,pady=10,padx=80)
main_window.mainloop()