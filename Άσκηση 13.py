def function(thelist,ar,themax,start,end):
    for i in range(end,start,-1):
        if((thelist[i]+themax)<=ar):
            themax+=thelist[i]
            function(thelist,ar,themax,start,i-1)
    return(themax)
def maxDistance(thelist,ar):
    thelist.sort()
    max1=0
    themax=0
    if (sum(thelist)<ar):
        return sum(thelist)
    a=len(thelist)
    for start in range(a):
        themax=thelist[start]
        for end in range(a-1,start,-1):
            if((thelist[end]+themax)<=ar):
                themax=function(thelist,ar,themax,start,end)
                max1=max(themax,max1)
    return max1
thelist=[]
t=""
while (t!="στοπ"):
    ap=int(input("Δώσε απόσταση: "))
    if (ap<=0):
        print ("error")
    else:
        thelist.append(ap)
    t=(input("Άν δεν θες να δώσεις άλλες αποστάσεις πληκτρολόγησε 'στοπ' αλλιώς πάτα οτιδήποτε άλλο για να συνεχίσεις.: " ))
ar=int(input ("Δώσε έναν θετικό ακέραιο: "))
while (ar<0):
    ar=int (input("Λάθος.Δώσε θετικό ακέραιο"))
print("Το μέγιστο άθροισμα είναι: ",maxDistance(thelist,ar))
