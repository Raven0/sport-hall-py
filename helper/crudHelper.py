import json


# initialization
class crudHelper:
    def __init__(self, table):
        self.table = table
        self.path = "X:/PROJECT/Console/py/sport-hall-py/file/" + table + ".txt"

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

    def create(self, name, status, attr):
        data = self.get_all()
        lid = len(data[self.table])
        record = r"{'id':" + str(lid + 1) + ","
        for a in attr:
            r = "'{}': {},"
            r2 = "'{}': {}"
            if a == 'name':
                record += r.format(a, name)
            else:
                record += r2.format(a, status)
        record += "}"
        data[self.table].append(record.replace('"', '').strip())
        print(data[self.table])
        # data[self.table].append({
        #     'id': str(lid + 1),
        #     'name': name,
        #     'status': status,
        # })
        # self.write_all(data)

    def read(self, mid):
        data = self.get_all()
        for p in data[self.table]:
            if p['id'] == mid:
                return p

    def update(self, mid, name, status):
        data = self.get_all()
        record = self.read(mid)
        record['name'] = name
        record['status'] = status
        print(data)
        self.write_all(data)

    def delete(self, mid):
        data = self.get_all()
        record = self.read(mid)
        data[self.table].remove(record)
        print(data)
        self.write_all(data)
