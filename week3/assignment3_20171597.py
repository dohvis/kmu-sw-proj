import pickle

dbfilename = 'test3_4.dat'

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
        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
            except IndexError:
                print("Invalid command: Please input like this 'add Name Age Score'")
            except ValueError:
                print("Invalid command: Age and Score are integer")
            except:
                print("Invalid command: I don't understand your command")
            else:
                scdb += [record]
        elif parse[0] == 'del':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except IndexError:
                print("Invalid command: Please input like this 'del Name'")
            except:
                print("Invalid command: I don't understand your command")
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for attr in sorted(p):
                            print(attr + "=" + str(p[attr]), end=' ')
                        print()
            except IndexError:
                print("Invalid command: Please input like this 'find Name'")
            except:
                print("Invalid command: I don't understand your command")
        elif parse[0] == 'inc':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] += int(parse[2])
            except IndexError:
                print("Invalid command: Please input like this 'inc Name Score'")
            except ValueError:
                print("Invalid command: Score is integer")
            except:
                print("Invalid command: I don't understand your command")
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])

def showScoreDB(scdb, keyname):
    try:
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                print(attr + "=" + str(p[attr]), end=' ')
            print()
    except KeyError:
        print("Invalid Keyname: " + keyname)
    except:
        print("Invalid command: I don't understand your command")

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)