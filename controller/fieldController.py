import model.model

# initialization
field = model.model.FIELD
path = "X:/PROJECT/Console/py/sport-hall-py/file/" + field + ".txt"


# function


def get_all():
    return open(path, "r").read()


def get_with_id():
    wid = []
    iid = 1
    for i in get_all().split():
        wid.append(str(iid)+'. '+i)
        iid = iid + 1
    return wid


def get_line(index: int):
    line = get_all().split()
    return line[index-1]


def write_line(args):
    write_file = open(path, "a")
    write_file.write("\n" + args)
    write_file.close()


def update_line(args, index: int):
    line = get_all().split()
    line[index-1] = args
    write_file = open(path, "w")
    for i in line:
        length = len(line)
        if line[length - 1] == i:
            write_file.write(i)
        else:
            write_file.write(i + "\n")
    write_file.close()
    return "updated"


def delete_line(index: int):
    line = get_all().split()
    line.remove(line[index-1])
    write_file = open(path, "w")
    for i in line:
        length = len(line)
        if line[length-1] == i:
            write_file.write(i)
        else:
            write_file.write(i + "\n")
    write_file.close()
    return "deleted"
