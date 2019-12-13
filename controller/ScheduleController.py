import helper.CrudHelper as CrudHelper
import model.model as model

model = model.Schedule
helper = CrudHelper.CrudHelper(model.name)


class ScheduleController:
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
