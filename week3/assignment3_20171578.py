import pickle
import copy

db_file_name = 'assignment3.dat'


def read_db():
    try:
        db_file = open(db_file_name, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", db_file_name)
        return []

    db = []
    try:
        db = pickle.load(db_file)
    except:
        print("Empty DB: ", db_file_name)
    else:
        print("Open DB: ", db_file_name)
    db_file.close()
    return db


# write the data into person db
def write_db(db):
    db_file = open(db_file_name, 'wb')
    pickle.dump(db, db_file)
    db_file.close()


def query_db(db):
    while True:
        input_str = (input("Score DB > "))
        if not input_str:
            continue
        parse = input_str.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                db += [record]
            except:
                print("Invalid command")
        elif parse[0] == 'del':
            try:
                # to deep copy db
                copy_db = copy.deepcopy(db)
                for p in copy_db:
                    if p['Name'] == parse[1]:
                        db.remove(p)
            except:
                print("Invalid command")
        elif parse[0] == 'show':
            try:
                sort_key = 'Name' if len(parse) == 1 else parse[1]
                show_db(db, sort_key)
            except:
                print("Invalid command")
        elif parse[0] == 'quit':
            break
        elif parse[0] == 'find':
            try:
                for person in db:
                    if person['Name'] == parse[1]:
                        print(person)
                    else:
                        print("There is no", parse[1])
            except:
                print("Invalid command")    
        elif parse[0] == 'inc':
            try:
                for person in db:
                    if person['Name'] == parse[1]:
                        person['Score'] += parse[2]
                        print("Increase %d to %d" % (parse[2], parse[1]))
            except:
                print("Invalid command")
        else:
            print("Invalid command: " + parse[0])


def show_db(db, key_name):
    for p in sorted(db, key=lambda person: person[key_name]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()


db = read_db()
query_db(db)
write_db(db)