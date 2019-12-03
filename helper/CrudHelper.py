import json


# initialization
class CrudHelper:
    def __init__(self, table):
        self.table = table
        self.path = "../file/" + table + ".txt"
        self.data = self.get_all()

    # function
    def get_all(self):
        with open(self.path) as file:
            return json.load(file)

    def write_all(self, args):
        with open(self.path, 'w') as file:
            json.dump(args, file, indent=4)
        file.close()

    def print_all(self):
        return self.data[self.table]

    def create(self, attr, args):
        lid = len(self.data[self.table])
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
        self.data[self.table].append(eval(record))
        self.write_all(self.data)

    def read(self, mid):
        for p in self.data[self.table]:
            if p['id'] == mid:
                return p

    def update(self, mid, attr, args):
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
        self.data[self.table][index-1] = record
        self.write_all(self.data)

    def delete(self, mid):
        record = self.read(mid)
        self.data[self.table].remove(record)
        self.write_all(self.data)
