def string_naar_ham(string):
   
    string_lijst = [] #maakt van de string een lijst_basisbits 
    for bit in string:
        string_lijst.append(bit)

    lijst_basisbits = [1] #voegt alle basisbits toe aan een lijst_basisbits 
    l=len(string)
    x=2
    while l>0:
        l-=x
        lijst_basisbits.append(x)
        x=x*2

    for waarde in lijst_basisbits: #voegt aan de stringlijst de 0 van de controlebits toe 
        string_lijst.insert(waarde-1,'0')

    if len(string_lijst)>=lijst_basisbits[-1]*2:#voegt nog een extra toe als de resulterende lijst_basisbits nog een extra basisbit nodig heeft 
        string_lijst.insert(lijst_basisbits[-1]*2-1,'0')
        lijst_basisbits.append(x)

    for p in lijst_basisbits: #bepaald de waardes van de basisbits en past ze aan 
        r=0
        i=0
        for bit in string_lijst: 
            i+=1 
            for t in range(p*2-p):
                if i%(p*2)==p+t: 
                    r+=int(bit)
        
        if r%2==1:
            string_lijst[p-1]=1

    string='' #maakt van lijst_basisbits weer een string        
    for p in string_lijst:
        string=string+str(p)
    return string

def ham_naar_string(ham):
    
    lijst_basisbits = [1] #voegt alle basisbits toe aan een lijst_basisbits 
    l=len(ham)
    x=2
    while l>0:
        l-=x
        lijst_basisbits.append(x)
        x=x*2

    if lijst_basisbits[-1]-1==len(ham): #correctie basisbitslijst
        lijst_basisbits.pop(-1)

    correctie=[] #maakt correctielijst gebasseerd op de het tellen wat in de ham string staat (zelfde als van string naar ham) 
    for p in lijst_basisbits:
        r=0
        i=0
        for bit in ham: 
            i+=1 
            for t in range(p*2-p):
                if i%(p*2)==p+t and i!=p: 
                    r+=int(bit)
        correctie.append(r%2)
   
    ham_lijst = [] #maakt van string een lijst 
    for bit in ham:
        ham_lijst.append(bit)

    correctie2=[] #maakt correctielijst gebasseerd op wat de controlebits daadwerkelijk zijn
    for p in lijst_basisbits:
        correctie2.append(ham_lijst[p-1])
    

    i=0 #als de correctielijsten niet overeenkomen dan wordt de index van de verkeerde bit bepaald 
    fout=0
    x=1
    for waarde in correctie:
        
        if str(waarde) != correctie2[i]:
            fout = fout+x
        i+=1
        x=x*2 

     
    if fout>0: #verkeerde bit wordt aangepast 
        if ham_lijst[fout-1]=='1':
            ham_lijst[fout-1]='0'
        else: ham_lijst[fout-1]='1'
    
    
    lijst_basisbits.reverse() #haalt controlebits weg 
    for waarde in lijst_basisbits:
        ham_lijst.pop(waarde-1) 

    string='' #maakt van lijst weer een string 
    for letter in ham_lijst:
        string= string+letter
        

    return(string)

def pariteitbits_gever(ham):
    lijst_basisbits = [1] #voegt alle basisbits toe aan een lijst_basisbits 
    l=len(ham)
    x=2
    while l>0:
        l-=x
        lijst_basisbits.append(x)
        x=x*2

    if lijst_basisbits[-1]-1==len(ham): #correctie basisbitslijst
        lijst_basisbits.pop(-1)

    correctie=[] #maakt correctielijst gebasseerd op de het tellen wat in de ham string staat (zelfde als van string naar ham) 
    for p in lijst_basisbits:
        r=0
        i=0
        for bit in ham: 
            i+=1 
            for t in range(p*2-p):
                if i%(p*2)==p+t and i!=p: 
                    r+=int(bit)
        correctie.append(r%2)
    string = ''
    for bit in correctie:
        string = string + str(bit)
    return string

    
