import helper.CrudHelper as CrudHelper
import model.model as model

model = model.Booking
helper = CrudHelper.CrudHelper(model.name)


class BookingController:
    @staticmethod
    def get():
        return helper.get_all()

    @staticmethod
    def create(args):
        helper.create(model.attr, args)

    @staticmethod
    def read(mid):
        return helper.read(mid)

    @staticmethod
    def update(mid, args):
        helper.update(mid, model.attr, args)

    @staticmethod
    def remove(mid):
        helper.delete(mid)
