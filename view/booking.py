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

def create_book():
    print("Field yang tersedia")
    for n in fieldC.get()['field']:
        print(n['name'])
    f = input('Pilih Field :')
    print()
    print('Schedule Tersedia')
    for n in scheduleC.get()['schedule']:
        print(n['date'])
    sch = input('Pilih Schedule :')
    print()
    print('Session yang tersedia')
    for n in sessionC.get()['session']:
        print(n['time'])
    ses = input('Pilih Session :')
    print()
    print('Member yang ada')
    for i in memberC.get()['member']:
        print(i['name'])
    m = input('Pilih Member : ')
    print('input booking time)')
    t = bookTime.returnTimeNow()
    final = (f + ' ' + sch + ' ' + ses + " " + m + " " + t)
    print(final)

    return final

def read_book():
    f_id = ''
    s_id = ''
    ss_id = ''
    m_id = ''

    for i in controller.get()['booking']:
        f_id = i['field_id']
        s_id = i['schedule_id']
        ss_id = i['session_id']
        m_id = i['user_id']

    print(f_id,s_id,ss_id,m_id)

def cek_book():
    create_book()







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
        read_book()

    elif m == 3:
        # if cek_book() in read_book():
        #     print('Booking sudah ada')
        # else:
        #     controller.create(create_book())
        cek_book()

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
