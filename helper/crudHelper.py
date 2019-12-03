import json


# initialization
class crudHelper:
    def __init__(self, table):
        self.table = table
        self.path = "../file/" + table + ".txt"

    # function
    def get_all(self):
        with open(self.path) as file:
            return json.load(file)

    def write_all(self, args):
        with open(self.path, 'w') as file:
            json.dump(args, file, indent=4)
        file.close()

    def print_all(self):
        data = self.get_all()
        return data[self.table]

    def create(self, attr, args):
        data = self.get_all()
        lid = len(data[self.table])
        record = "{'id': '" + str(lid + 1) + "',"
        r = "'{}': '{}',"
        r2 = "'{}': '{}'"
        ar = args.split()
        index = 0
        for i in range(len(ar)):
            for j in range(len(attr)):
                if i == j:
                    if index == len(attr)-1:
                        record += r2.format(attr[j], ar[i])
                    else:
                        record += r.format(attr[j], ar[i])
            index += 1
        record += "}"
        data[self.table].append(eval(record))
        self.write_all(data)

    def read(self, mid):
        data = self.get_all()
        for p in data[self.table]:
            if p['id'] == mid:
                return p

    def update(self, mid, attr, args):
        data = self.get_all()
        record = self.read(mid)
        ar = args.split()
        for i in range(len(ar)):
            for j in range(len(attr)):
                if i == j:
                    record[attr[j]] = ar[i]
        index = 0
        for ref in data[self.table]:
            index += 1
            if mid in ref['id']:
                break
        data[self.table][index-1] = record
        self.write_all(data)

    def delete(self, mid):
        data = self.get_all()
        record = self.read(mid)
        data[self.table].remove(record)
        print(data)
        self.write_all(data)
