import model.model

# initialization
field = model.model.FIELD
path = "X:/PROJECT/Console/py/sport-hall-py/file/" + field + ".txt"


# function


def get_all():
    return open(path, "r").read()


def get_line(index: int):
    line = get_all().split()
    return line[index]


def write_line(args):
    write_file = open(path, "a")
    write_file.write("\n" + args)
    write_file.close()


def delete_line(index: int):
    line = get_all().split()
    line.remove(line[index])
    write_file = open(path, "w")
    for i in line:
        length = len(line)
        if line[length-1] == i:
            write_file.write(i)
        else:
            write_file.write(i + "\n")
    write_file.close()
    return "deleted"
