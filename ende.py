import os
def encrypt():
    str=input("Enter the file name you want to encrypt\n")
    f1=open(str,'r')
    r=f1.read()
    f1.close()
    f1=open('key.txt','r')
    k=f1.read(108)
    K=f1.read()
    # print(k)
    # print(K)
    f1.close()
    if(os.path.exists('key.txt')):  
        f2=open('enp.txt','w+')
    for i in r:
        if i == ' ':
            f2.write(i)
            continue
        if i.isupper():
             n=K.index(i)
             # print(n)
             str2=K[n+1]+K[n+2]
             # print(str2)
             f2.write(str2)
        else:     
             n=k.index(i)
             # print(n)
             str2=k[n+1]+k[n+2]
             # print(str2)
             f2.write(str2)
    f2.close()
def decrypt():
    str=input("Enter the file name you want to decrypt\n")
    f1=open(str,'r')
    r=f1.read()
    f1.close()
    f1=open('key.txt','r')
    k=f1.read(108)
    K=f1.read()
    # print(k)
    # print(K)
    f1.close()
    if(os.path.exists('key.txt')):  
        f2=open('output.txt','w+')
    for i in range(0,len(r)):
        if r[i]==' ':
            f2.write(r[i])
            continue
        if r[i].islower():
           try:
               c=r[i]+r[i+1]
               n=K.index(c)
           except ValueError:
              continue
           except IndexError:
               continue
           # print(k[n-1],end='')
           f2.write(K[n-1])
        else:
            try:
               c=r[i]+r[i+1]
               n=k.index(c)
            except ValueError:
               continue
            except IndexError:
               continue
           # print(k[n-1],end='')
            f2.write(k[n-1])
    f2.close()
print("-----FILE ENCRYPTION=====\n")
print("Select your choice\n")
print("1.Encrypt")
print("2.Decrypt")
n=int(input())
if n==1:
    encrypt()
elif n==2:
    decrypt()
else:
    print("INVALID")
