while True:
        ar=int(input("Δώσε έναν αριθμό μεχρι το 1000000"))
        while ar<2 or ar>1000000:
                ar=int(input("Λάθος,δώσε ξανά"))
        arithmos=ar
        protoi=[2]
        table=[0]
        for i in range(3,2000):
                k=0 
                for j in range(1,i+1):
                        if i%j==0:
                                k+=1

                if k==2: #Αν ο μετρητης ειναι ίσος με 2, αυτό σημαινει οτι αριθμος διαιρείται με τον εαυτό του και την μονάδα. Άρα ειναι πρώτος.
                        protoi.append(i)
                                        
        p=[0]*(len(protoi)+1)       
        while ar!=1:
                i=0
                while ar!=1:
                        if ar%protoi[i]==0:
                                ar=ar//protoi[i]
                                p[i]+=1
                                i=0
                        else:
                                i+=1

        apot=" "
        for i in range(len(protoi)):
                if p[i]!=0:
                        protos=str(protoi[i])
                        dyn=str(p[i])                
                        apot+="("+(protos + "**" + dyn)+")"         
        print("Ο" ,arithmos, "γράφεται ως γινόμενο πρώτων παραγόντων:" ,apot,)
        enter=str(input("Πάτα 'ENTER' για να δώσεις νέο αριθμό."))
        if enter!="":
                break
