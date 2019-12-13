import controller.BookingController as bookingController
import controller.FieldController as fieldController
import controller.ScheduleController as scheduleController
import controller.SessionController as sessionController
import controller.MemberController as memberController
import helper.TimeHelper as timeHelper

# initialization
controller = bookingController.BookingController()
fieldC = fieldController.FieldController()
scheduleC = scheduleController.ScheduleController()
sessionC = sessionController.SessionController()
memberC = memberController.MemberController()
bookTime = timeHelper.TimeHelper()



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
        print("Field yang tersedia")
        for n in fieldC.get()['field']:
            print(n['name'])
        f = input('Pilih Field')
        print()
        print('Schedule Tersedia')
        for n in scheduleC.get()['schedule']:
            print(n['date'])
        sch = input('Pilih Schedule')
        print()
        print('ession')
        for n in sessionC.get()['session']:
            print(n['time'])
        print('pilih session')
        # ses = input()
        print()
        print('silahkan pilih member')
        for i in memberC.get()['member']:
            print(i['name'])
        print()
        print('input booking time)')
        print(bookTime.returnTimeNow(input()))







        # 1 = field 1 = fasd 3 13 13:30
        # controller.create(input())
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
