from tkinter import *
from controller.BookingController import BookingController
from controller.FeesController import FeesController
from controller.FieldController import FieldController
from controller.MemberController import MemberController
from controller.ScheduleController import ScheduleController
from controller.SessionController import SessionController
import helper.AuthHelper as Auth
import helper.TimeHelper as Time

isLogin = True
selectedItem = 0
selectedScheduleItem = 0
selectedFieldItem = 0
selectedSessionItem = 0
selectedMemberItem = 0


class Main(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("SPORT-HALL")

        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        main_menu = Menu(menu_bar)
        menu_bar.add_cascade(label="Main", menu=main_menu)
        main_menu.add_command(label="Login", command=lambda: authView())
        main_menu.add_command(label="Exit", command=self.onExit)

        master_menu = Menu(menu_bar)
        menu_bar.add_cascade(label="Master", menu=master_menu)
        master_menu.add_command(label="Field", command=lambda: masterView("Field"))
        master_menu.add_command(label="Fees", command=lambda: masterView("Fees"))
        master_menu.add_command(label="Member", command=lambda: masterView("Member"))
        master_menu.add_command(label="Schedule", command=lambda: masterView("Schedule"))
        master_menu.add_command(label="Session", command=lambda: masterView("Session"))
        master_menu.add_command(label="Booking", command=lambda: masterView("Booking"))

        action_menu = Menu(menu_bar)
        menu_bar.add_cascade(label="Action", menu=action_menu)
        action_menu.add_command(label="Register", command=lambda: masterView("Member"))
        action_menu.add_command(label="Booking", command=lambda: bookingView())
        action_menu.add_command(label="Payment", command=lambda: paymentView())
        action_menu.add_command(label="Report", command=lambda: reportView())

    def onExit(self):
        self.quit()


def onSelectItem(event):
    global selectedItem
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    selectedItem = value[0]


def onSelectScheduleItem(event):
    global selectedScheduleItem
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    selectedScheduleItem = value[0]


def onSelectFieldItem(event):
    global selectedFieldItem
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    selectedFieldItem = value[0]


def onSelectSessionItem(event):
    global selectedSessionItem
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    selectedSessionItem = value[0]


def onSelectMemberItem(event):
    global selectedMemberItem
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    selectedMemberItem = value[0]


def bookingView():
    global selectedScheduleItem
    global selectedFieldItem
    global selectedSessionItem
    global selectedMemberItem
    if isLogin:
        view = Toplevel()
        view.title('System')
        schedule_list_box = Listbox(view)
        schedule_list_box.grid(row=1, column=1)
        for data in ScheduleController.get()['schedule']:
            schedule_list_box.insert(int(data['id']), data['id'] + '.date: ' + data['date'])
        schedule_list_box.bind('<<ListboxSelect>>', onSelectScheduleItem)
        field_list_box = Listbox(view)
        field_list_box.grid(row=1, column=2)
        for data in FieldController.get()['field']:
            field_list_box.insert(int(data['id']), data['id'] + '.name: ' + data['name'])
        field_list_box.bind('<<ListboxSelect>>', onSelectFieldItem)
        session_list_box = Listbox(view)
        session_list_box.grid(row=2, column=1)
        session_list_box.bind('<<ListboxSelect>>', onSelectSessionItem)
        Button(view, text='Check Session', command=lambda: checkAvailableSession()) \
            .grid(row=3, column=1)
        Button(view, text='Book Session', command=lambda: bookSession()) \
            .grid(row=3, column=2)
        member_list_box = Listbox(view)
        member_list_box.grid(row=2, column=2)
        for data in MemberController.get()['member']:
            member_list_box.insert(int(data['id']), data['id'] + '.name: ' + data['name'])
        member_list_box.bind('<<ListboxSelect>>', onSelectMemberItem)
    else:
        toast("Please Login first")

    def checkAvailableSession():
        if selectedScheduleItem == 0 and selectedFieldItem == 0:
            toast('Please select item first')
        else:
            taken_session = []
            session_list_box.delete(0, END)
            for b in BookingController.get()['booking']:
                if b['schedule_id'] == selectedScheduleItem and b['field_id'] == selectedFieldItem:
                    taken_session.append(b['session_id'])
            for session in SessionController.get()['session']:
                if session['id'] not in taken_session:
                    session_list_box.insert(int(session['id']), session['id'] + '.time: ' + session['time'])

    def bookSession():
        if selectedSessionItem == 0:
            toast('Please make sure you have selected session item')
        elif selectedMemberItem == 0:
            toast('Please make sure you have selected member item')
        else:
            booking = str(selectedFieldItem) \
                      + ' ' + str(selectedScheduleItem) \
                      + ' ' + str(selectedSessionItem) \
                      + ' ' + str(selectedMemberItem) \
                      + ' ' + str(Time.TimeHelper.returnTimeNow()) \
                      + ' ' + 'book'
            BookingController.create(booking)
            toast('Session booked')
            checkAvailableSession()
            clearSelection()

    def clearSelection():
        global selectedSessionItem
        selectedSessionItem = 0
        global selectedMemberItem
        selectedMemberItem = 0


def paymentView():
    global selectedMemberItem
    global selectedItem
    loadedBooking = []
    if isLogin:
        view = Toplevel()
        view.title('System')
        member_list_box = Listbox(view, width=80)
        member_list_box.grid(row=1, columnspan=2)
        for data in MemberController.get()['member']:
            member_list_box.insert(int(data['id']), data['id'] + '.name: ' + data['name'])
        member_list_box.bind('<<ListboxSelect>>', onSelectMemberItem)
        Button(view, text='Checkout', width=25, command=lambda: loadData()) \
            .grid(row=2)
        list_box = Listbox(view, width=80)
        list_box.grid(row=3, columnspan=2)
        list_box.bind('<<ListboxSelect>>', onSelectItem)
        Button(view, text='Payment', width=25, command=lambda: payment_confirmation()) \
            .grid(row=4)
    else:
        toast("Please Login first")

    def loadData():
        if selectedMemberItem == 0:
            toast('Please select member first')
        else:
            list_box.delete(0, END)
            loadedBooking.clear()
            for booking in BookingController.get()['booking']:
                if booking['status'] != 'done' and booking['user_id'] == selectedMemberItem:
                    loadedBooking.append(booking)
                    list_box.insert(int(booking['id']), booking['id']
                                    + '.field: ' + str(FieldController.read(booking['field_id'])['name'])
                                    + '.schedule: ' + str(ScheduleController.read(booking['schedule_id'])['date'])
                                    + '.session: ' + str(SessionController.read(booking['session_id'])['time'])
                                    + '.user_id: ' + booking['user_id']
                                    + '.booking_time: ' + booking['booking_time'])

    def payment_confirmation():
        rate = FeesController.read('1')['rate']
        payment_view = Toplevel()
        payment_view.title('Payment')
        detail = 'Payment for:\n'
        for item in loadedBooking:
            detail += 'Booking id: ' + str(item['id']) +\
                      ' Field: ' + str(FieldController.read(item['field_id'])['name']) +\
                      ' Schedule: ' + str(ScheduleController.read(item['schedule_id'])['date']) +\
                      ' Session: ' + str(SessionController.read(item['session_id'])['time']) + '\n'
        Label(payment_view, text=detail).pack()
        Label(payment_view, text='Total price : ' + str(int(rate) * len(loadedBooking))).pack()
        Button(payment_view, text='Pay', command=lambda: payment(payment_view)).pack()

    def payment(context):
        for pay in loadedBooking:
            BookingController\
                .update(pay['id'],
                        pay['field_id'] + ' ' +
                        pay['schedule_id'] + ' ' +
                        pay['session_id'] + ' ' +
                        pay['user_id'] + ' ' +
                        pay['booking_time'] + ' ' +
                        'done')
        context.destroy()
        loadData()


def reportView():
    if isLogin:
        view = Toplevel()
        view.title('System')
        list_box = Listbox(view, width=100)
        list_box.grid(row=1, columnspan=1)
        list_box.bind('<<ListboxSelect>>', onSelectMemberItem)
        Button(view, text='Load', width=25, command=lambda: loadData()) \
            .grid(row=2)
    else:
        toast("Please Login first")

    def loadData():
        list_box.delete(0, END)
        for booking in BookingController.get()['booking']:
            list_box.insert(int(booking['id']), booking['id']
                            + '.field: ' + str(FieldController.read(booking['field_id'])['name'])
                            + '.schedule: ' + str(ScheduleController.read(booking['schedule_id'])['date'])
                            + '.session: ' + str(SessionController.read(booking['session_id'])['time'])
                            + '.user_id: ' + booking['user_id']
                            + '.booking_time: ' + booking['booking_time']
                            + '.status: ' + booking['status'])


def masterView(args):
    global selectedItem
    if isLogin:
        view = Toplevel()
        view.title('System')
        list_box = Listbox(view, width=65)
        list_box.grid(row=1, columnspan=2)
        if args == "Booking":
            for data in BookingController.get()['booking']:
                list_box.insert(int(data['id']), data['id'] + '.field_id: ' + data['field_id']
                                + '.schedule_id: ' + data['schedule_id']
                                + '.session_id: ' + data['session_id']
                                + '.user_id: ' + data['user_id']
                                + '.booking_time: ' + data['booking_time'])
        elif args == "Fees":
            for data in FeesController.get()['fees']:
                list_box.insert(int(data['id']), data['id'] + '.rate: ' + data['rate'])
        elif args == "Field":
            for data in FieldController.get()['field']:
                list_box.insert(int(data['id']), data['id'] + '.name: ' + data['name'])
        elif args == "Member":
            for data in MemberController.get()['member']:
                list_box.insert(int(data['id']), data['id'] + '.name: ' + data['name'])
        elif args == "Schedule":
            for data in ScheduleController.get()['schedule']:
                list_box.insert(int(data['id']), data['id'] + '.date: ' + data['date'])
        elif args == "Session":
            for data in SessionController.get()['session']:
                list_box.insert(int(data['id']), data['id'] + '.time: ' + data['time'])
        list_box.bind('<<ListboxSelect>>', onSelectItem)
        Button(view, text='Create', width=25, command=lambda: createView(view, args)) \
            .grid(row=2, columnspan=2)
        Button(view, text='Update', width=25, command=lambda: updateView(view, args, selectedItem)) \
            .grid(row=4, columnspan=2)
        Button(view, text='Delete', width=25, command=lambda: deleteView(view, args, selectedItem)) \
            .grid(row=5, columnspan=2)
    else:
        toast("Please Login first")


def createView(context, args):
    view = Toplevel()
    view.title('Create')
    Label(view, text='Create New Data').grid(row=0, columnspan=2)
    if args == "Booking":
        Label(view, text='field_id').grid(row=1)
        p1 = Entry(view)
        p1.grid(row=1, column=1)
        Label(view, text='schedule_id').grid(row=2)
        p2 = Entry(view)
        p2.grid(row=2, column=1)
        Label(view, text='session_id').grid(row=3)
        p3 = Entry(view)
        p3.grid(row=3, column=1)
        Label(view, text='user_id').grid(row=4)
        p4 = Entry(view)
        p4.grid(row=4, column=1)
        Button(view, text='Create', width=25, command=lambda: createValidation(
            p1.get()
            + ' ' + p2.get()
            + ' ' + p3.get()
            + ' ' + p4.get()
            + ' ' + Time.TimeHelper.returnTimeNow()
            + ' ' + 'book')) \
            .grid(row=5, columnspan=2)
        Button(view, text='Done', width=25, command=lambda: done()).grid(row=6, columnspan=2)
    elif args == "Fees":
        Label(view, text='Rate').grid(row=1)
        p = Entry(view)
        p.grid(row=1, column=1)
        Button(view, text='Create', width=25, command=lambda: createValidation(p.get())) \
            .grid(row=2, columnspan=2)
        Button(view, text='Done', width=25, command=lambda: done()).grid(row=3, columnspan=2)
    elif args == "Field":
        Label(view, text='Field').grid(row=1)
        p = Entry(view)
        p.grid(row=1, column=1)
        Button(view, text='Create', width=25, command=lambda: createValidation(p.get())) \
            .grid(row=2, columnspan=2)
        Button(view, text='Done', width=25, command=lambda: done()).grid(row=3, columnspan=2)
    elif args == "Member":
        Label(view, text='Name').grid(row=1)
        p = Entry(view)
        p.grid(row=1, column=1)
        Button(view, text='Create', width=25, command=lambda: createValidation(p.get())) \
            .grid(row=2, columnspan=2)
        Button(view, text='Done', width=25, command=lambda: done()).grid(row=3, columnspan=2)
    elif args == "Schedule":
        Label(view, text='Date').grid(row=1)
        p = Entry(view)
        p.grid(row=1, column=1)
        Button(view, text='Create', width=25, command=lambda: createValidation(p.get())) \
            .grid(row=2, columnspan=2)
        Button(view, text='Done', width=25, command=lambda: done()).grid(row=3, columnspan=2)
    elif args == "Session":
        Label(view, text='Time').grid(row=1)
        p = Entry(view)
        p.grid(row=1, column=1)
        Button(view, text='Create', width=25, command=lambda: createValidation(p.get())) \
            .grid(row=2, columnspan=2)
        Button(view, text='Done', width=25, command=lambda: done()).grid(row=3, columnspan=2)

    def createValidation(value):
        if value is None:
            toast("Field empty")
        else:
            if args == "Booking":
                BookingController.create(value)
            elif args == "Fees":
                FeesController.create(value)
            elif args == "Field":
                FieldController.create(value)
            elif args == "Member":
                MemberController.create(value)
            elif args == "Schedule":
                ScheduleController.create(value)
            elif args == "Session":
                SessionController.create(value)

    def done():
        view.destroy()
        context.destroy()
        masterView(args)


def updateView(context, args, mid):
    view = Toplevel()
    view.title('Edit')
    Label(view, text='Edit Existing Data').grid(row=0, columnspan=2)
    if args == "Booking":
        Label(view, text='field_id').grid(row=1)
        p1 = Entry(view)
        p1.insert(0, BookingController.read(mid)['field_id'])
        p1.grid(row=1, column=1)
        Label(view, text='schedule_id').grid(row=2)
        p2 = Entry(view)
        p2.insert(0, BookingController.read(mid)['schedule_id'])
        p2.grid(row=2, column=1)
        Label(view, text='session_id').grid(row=3)
        p3 = Entry(view)
        p3.insert(0, BookingController.read(mid)['session_id'])
        p3.grid(row=3, column=1)
        Label(view, text='user_id').grid(row=4)
        p4 = Entry(view)
        p4.insert(0, BookingController.read(mid)['user_id'])
        p4.grid(row=4, column=1)
        Button(view, text='Update', width=25, command=lambda: updateValidation(
            p1.get()
            + ' ' + p2.get()
            + ' ' + p3.get()
            + ' ' + p4.get()
            + ' ' + Time.TimeHelper.returnTimeNow())) \
            .grid(row=5, columnspan=2)
        Button(view, text='Done', width=25, command=lambda: done()).grid(row=6, columnspan=2)
    elif args == "Fees":
        Label(view, text='Rate').grid(row=1)
        p = Entry(view)
        p.insert(0, FeesController.read(mid)['rate'])
        p.grid(row=1, column=1)
        Button(view, text='Update', width=25, command=lambda: updateValidation(p.get())) \
            .grid(row=2, columnspan=2)
        Button(view, text='Done', width=25, command=lambda: done()).grid(row=3, columnspan=2)
    elif args == "Field":
        Label(view, text='Field').grid(row=1)
        p = Entry(view)
        p.insert(0, FieldController.read(mid)['name'])
        p.grid(row=1, column=1)
        Button(view, text='Update', width=25, command=lambda: updateValidation(p.get())) \
            .grid(row=2, columnspan=2)
        Button(view, text='Done', width=25, command=lambda: done()).grid(row=3, columnspan=2)
    elif args == "Member":
        Label(view, text='Name').grid(row=1)
        p = Entry(view)
        p.insert(0, MemberController.read(mid)['name'])
        p.grid(row=1, column=1)
        Button(view, text='Update', width=25, command=lambda: updateValidation(p.get())) \
            .grid(row=2, columnspan=2)
        Button(view, text='Done', width=25, command=lambda: done()).grid(row=3, columnspan=2)
    elif args == "Schedule":
        Label(view, text='Date').grid(row=1)
        p = Entry(view)
        p.insert(0, ScheduleController.read(mid)['date'])
        p.grid(row=1, column=1)
        Button(view, text='Update', width=25, command=lambda: updateValidation(p.get())) \
            .grid(row=2, columnspan=2)
        Button(view, text='Done', width=25, command=lambda: done()).grid(row=3, columnspan=2)
    elif args == "Session":
        Label(view, text='Time').grid(row=1)
        p = Entry(view)
        p.insert(0, SessionController.read(mid)['time'])
        p.grid(row=1, column=1)
        Button(view, text='Update', width=25, command=lambda: updateValidation(p.get())) \
            .grid(row=2, columnspan=2)
        Button(view, text='Done', width=25, command=lambda: done()).grid(row=3, columnspan=2)

    def updateValidation(value):
        if value is None:
            toast("Field empty")
        else:
            if args == "Booking":
                BookingController.update(mid, value)
            elif args == "Fees":
                FeesController.update(mid, value)
            elif args == "Field":
                FieldController.update(mid, value)
            elif args == "Member":
                MemberController.update(mid, value)
            elif args == "Schedule":
                ScheduleController.update(mid, value)
            elif args == "Session":
                SessionController.update(mid, value)

    def done():
        view.destroy()
        context.destroy()
        masterView(args)


def deleteView(context, args, mid):
    if args == "Booking":
        BookingController.remove(mid)
    elif args == "Fees":
        FeesController.remove(mid)
    elif args == "Field":
        FieldController.remove(mid)
    elif args == "Member":
        MemberController.remove(mid)
    elif args == "Schedule":
        ScheduleController.remove(mid)
    elif args == "Session":
        SessionController.remove(mid)
    context.destroy()
    masterView(args)


def authView():
    if isLogin:
        toast('Already logged-in')
    else:
        view = Toplevel()
        view.title('System Login')
        Label(view, text='System Login').grid(row=0, columnspan=2)
        Label(view, text='password').grid(row=1)
        p = Entry(view, show='*')
        p.grid(row=1, column=1)
        Button(view, text='Login', width=25, command=lambda: login(view, p.get())).grid(row=3, columnspan=2)


def login(view, args):
    global isLogin
    if Auth.AuthHelper.authVerification(args):
        isLogin = True
        view.destroy()
    else:
        isLogin = False
        toast('Wrong password')


def main():
    view = Tk()
    view.geometry('200x200')
    Main()
    Label(view, text='Sport Hall System').grid(row=0, columnspan=2)
    view.mainloop()


def toast(args):
    view = Toplevel()
    view.title('Toast Message')
    Label(view, text=args).pack()
    Button(view, text='Exit', command=lambda: view.destroy()).pack()


if __name__ == '__main__':
    main()
