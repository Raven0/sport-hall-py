import helper.crudHelper as crudHelper
import model.model as model

# initialization
field = model.Tarif
controller = crudHelper.crudHelper(field.name)
b = False

while not b:
    print("1. Get All")
    print("2. Read")
    print("3. Create")
    print("4. Update")
    print("5. Delete")
    m = int(input("Choose menu : "))
    if m == 1:
        print(controller.print_all())
    elif m == 2:
        print(controller.read(input()))
    elif m == 3:
        controller.create(field.attr, input())
    elif m == 4:
        print(controller.update(input(), field.attr, input()))
    elif m == 5:
        print(controller.delete(input()))

    v = input("continue? y/n ")

    if v == "n":
        b = True
    elif v == "y":
        b = False
    else:
        print("invalid answer, rebooting...")
