print("++++++Choose by number++++++")
print("++++++1.Open new client account+++++++")
print("++++++2.Modify the account+++++")
print("++++++3.Check Clients Balance+++++++")
print("++++++4.All Clients list++++++")
print("++++++5.Close the account++++++")

def new():
    file=open('Bank', 'a')
    readfile=open('Bank', 'r')
    name=str(input("Enter the client's name :").replace(" ",""))
    amount=str(input("Enter the amount :"))
    Content = readfile.read()
    Counter=1
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1
    counter=str(Counter)
    info=str(counter+'\t'+name+'\t'+amount+'\n')
    file.write(info)
    file.close()
    print('Account number :'+counter+'\n'+'Name :'+name+'\n'+'Amount :'+amount)
    print("Please remember your account number.")

def Modify():
    readfile=open('Bank', 'r')
    No=input("Enter the account number :")
    Name=input("Enter the name :")
    newamount=input('Enter the new amount :')
    newinfo=No+'\t'+Name+'\t'+newamount
    newdata=''
    bank=readfile.readline()
    while bank !='':
        vr=bank.split()
        if No==vr[0]:
            newdata+=newinfo
            newdata+='\n'
        else:
            newdata+=bank
        bank=readfile.readline()
    readfile.close()
    try:
        file=open('Bank', 'w')
    except:
        print('File dosen\'t exit')
    else:
        print(newdata)
        file.write(newdata)
        file.close()


def Check():
    file = open('Bank', 'a')
    readfile = open('Bank', 'r')
    No = (input("Enter the account number :"))
    bank=readfile.readline()
    while bank!='':
        vr=bank.split()
        if vr[0]==No:
            print("No\tName\tAmount")
            print('%s\t%s\t\%s\t' %(vr[0],vr[1],vr[2]))
        bank=readfile.readline()
    file.close()

def all():
    readfile = open('Bank', 'r')
    read=readfile.read()
    print(read)


def close():
    readfile = open('Bank', 'r')
    lines=readfile.readlines()
    No = int(input("Enter the account number :"))
    del lines[No-1]
    new=open('Bank', 'w')
    for line in lines:
        new.write('\n')
        new.write(line)
    new.close()

while 1:
    print('If you want break enter break')
    choice = input("Choose by number :")
    if choice == '1':
        new()
    if choice == '2':
        Modify()
    if choice == '3':
        Check()
    if choice == '4':
        all()
    if choice == '5':
        close()
    elif choice=='break':
        break

    else:
        continue







