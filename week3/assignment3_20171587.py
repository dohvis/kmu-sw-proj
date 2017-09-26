import pickle


class App:
    def __init__(self, filename):
        self.memory = []
        self.filename = filename

        try:
            self.fp = open(self.filename, "rb")
            self.memory = pickle.load(self.fp)
        except FileNotFoundError:
            print("[+] Create file based DB: {}".format(self.filename))
            open(self.filename, "wb").close()
            self.fp = open(self.filename, "rb")
        print("Open db: {}".format(self.filename))
        self.fp.close()

    def _get_index(self, name):
        index = -1
        for idx, row in enumerate(self.memory):
            if row['name'] == name:
                index = idx
        return index

    def show(self, *args):
        for row in sorted(self.memory, key=lambda row: row['name']):
            for key in sorted(row):
                print('{key} = {value}'.format(key=key, value=row[key]), end=' ')
            print()
        return ''

    def add(self, age, name, score, *args, **kwargs):
        row = {"age": age, "name": name, "score": score}

        self.memory.append(row)
        return 'Success to add {}'.format(row)

    def delete(self, name, *args, **kwargs):
        index = self._get_index(name)
        if index < 0:
            msg = '[-] There is no {}'
        else:
            self.memory.remove(index)
            msg = '[+] Success to delete {}'.format(name)
        return msg

    def increase(self, name, value, *args):
        index = self._get_index(name)
        if index < 0:
            return 'No {}'.format(name)
        self.memory[index] += int(value)
        return '[*] Done'

    def find(self, name):
        index = self._get_index(name)
        if index < 0:
            msg = ('[-] No {}'.format(name))
        else:
            msg = (self.memory[index])
        return msg

    def save(self, *args):
        with open(self.filename, "wb") as fp:
            pickle.dump(self.memory, fp)
        return '[*] Save complete.'

    def run(self):
        commands = {
            "add": self.add,
            "show": self.show,
            "delete": self.delete,
            "quit": None,  # keywords for break infinite loop
            "increase": self.increase,
            "find": self.find,
            "save": self.save
        }
        print('Function list: \n - {}'.format('\n - '.join(commands.keys())))
        while True:
            user_input = input('>>> ')

            input_list = user_input.split()
            cmd = input_list[0]
            if cmd == 'quit':
                print('[-] Bye')
                break

            args = input_list[1:]

            try:
                msg = commands[cmd](*args)
                # msg = self.add([age, name, score])
            except KeyError:
                msg = "[-] Invalid command {}".format(cmd)
            except TypeError:
                msg = "[-] Invalid arguments {} for {}".format(args, cmd)

            if len(msg) > 0:
                print(msg)


def main():
    filename = 'db'
    app = App(filename)
    app.run()


if __name__ == "__main__":
    main()

