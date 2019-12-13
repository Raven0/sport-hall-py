import json

# initialization
# noinspection PyTypeChecker
success_msg = "{} successfully executed"
exception_msg = "{} exception occured"


# noinspection PyTypeChecker
class CrudHelper:
    def __init__(self, table):
        self.table = table
        self.path = "../file/" + table + ".txt"
        self.data = self.get_all()

    # function
    def get_all(self):
        try:
            with open(self.path) as file:
                return json.load(file)
        except ValueError:
            return exception_msg.format("Value")
        except IOError:
            return exception_msg.format("IO")

    def write_all(self, args):
        try:
            with open(self.path, 'w') as file:
                json.dump(args, file, indent=4)
            file.close()
        except ValueError:
            print(exception_msg.format("Value"))
        except IOError:
            print(exception_msg.format("IO"))

    def print_all(self):
        try:
            return self.data[self.table]
        except ValueError:
            return exception_msg.format("Value")
        except IOError:
            return exception_msg.format("IO")

    def create(self, attr, args):
        try:
            lid = len(self.data[self.table])
            record = "{'id': '" + str(lid + 1) + "',"
            r = "'{}': '{}',"
            r2 = "'{}': '{}'"
            ar = args.split()
            index = 0
            for i in range(len(ar)):
                for j in range(len(attr)):
                    if i == j:
                        if index == len(attr) - 1:
                            record += r2.format(attr[j], ar[i])
                        else:
                            record += r.format(attr[j], ar[i])
                index += 1
            record += "}"
            self.data[self.table].append(eval(record))
            self.write_all(self.data)
            print(success_msg.format("Create " + self.table))
        except ValueError:
            print(exception_msg.format("Value"))
        except IOError:
            print(exception_msg.format("IO"))

    def read(self, mid):
        try:
            for p in self.data[self.table]:
                if p['id'] == mid:
                    return p
        except ValueError:
            print(exception_msg.format("Value"))
        except IOError:
            print(exception_msg.format("IO"))

    def update(self, mid, attr, args):
        try:
            record = self.read(mid)
            ar = args.split()
            for i in range(len(ar)):
                for j in range(len(attr)):
                    if i == j:
                        record[attr[j]] = ar[i]
            index = 0
            for ref in self.data[self.table]:
                index += 1
                if mid in ref['id']:
                    break
            self.data[self.table][index - 1] = record
            self.write_all(self.data)
            print(success_msg.format("Update", self.table))
        except ValueError:
            print(exception_msg.format("Value"))
        except IOError:
            print(exception_msg.format("IO"))

    def delete(self, mid):
        try:
            record = self.read(mid)
            self.data[self.table].remove(record)
            self.write_all(self.data)
            print(success_msg.format("Delete", self.table))
        except ValueError:
            print(exception_msg.format("Value"))
        except IOError:
            print(exception_msg.format("IO"))
