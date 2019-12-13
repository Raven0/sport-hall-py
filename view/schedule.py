import controller.ScheduleController as scheduleController

# initialization
controller = scheduleController.ScheduleController()
b = False

while not b:
    print("1. Get All")
    print("2. Read")
    print("3. Create")
    print("4. Update")
    print("5. Delete")
    m = int(input("Choose menu : "))
    if m == 1:
        print(controller.get())
    elif m == 2:
        print(controller.read(input()))
    elif m == 3:
        controller.create(input())
    elif m == 4:
        print(controller.update(input(), input()))
    elif m == 5:
        print(controller.remove(input()))

    v = input("continue? y/n ")

    if v == "n":
        b = True
    elif v == "y":
        b = False
    else:
        print("invalid answer, rebooting...")
