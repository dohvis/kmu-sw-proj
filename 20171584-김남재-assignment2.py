errormsg = "Plese enter positive integer or zero"

while True :
    try :
        inp = int(input("Enter a number : ")) 
    except :
        print(errormsg)
    else :
        if inp==-1 :
            break
        if inp<-1 :
            print(errormsg)
            continue
        
        i = inp
        fac = 1
        while i>1 :
            fac *= i
            i -= 1
        print("%d! = %d"%(inp,fac))
