import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "":
            continue
        parse = inputstr.split(" ")
        if parse[0] == 'add' and len(parse) == 4:
            try:
                record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
            except ValueError:
                print("Value Error")
            else:
                scdb += [record]
        elif parse[0] == 'del' and len(parse) == 2:
            for p in scdb:
                if p['Name'] == parse[1]:
                    scdb.remove(p)	
        elif parse[0] == 'find' and len(parse) == 2:
            for p in scdb:
                if p['Name'] == parse[1]:
                    print("Age="+str(p['Age'])+" Name="+p['Name']+" Score="+str(p['Score']))
        elif parse[0] == 'inc' and len(parse) == 3:
            for p in scdb:
                if p['Name'] == parse[1]:
                    try:
                        p['Score'] += int(parse[2])
                    except ValueError:
                        print("Value Error")
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])
            

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()
    

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

