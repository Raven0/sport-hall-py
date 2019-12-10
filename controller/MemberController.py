import helper.CrudHelper as CrudHelper
import model.model as model

model = model.Member
helper = CrudHelper.CrudHelper(model.name)


class MemberController:
    def __init__(self):
        self.data = helper.get_all()

    def get(self):
        return self.data

    @staticmethod
    def create(args):
        return helper.create(model.attr, args)

    @staticmethod
    def read(mid):
        return helper.read(mid)

    @staticmethod
    def update(mid, args):
        return helper.update(mid, model.attr, args)

    @staticmethod
    def remove(mid):
        return helper.delete(mid)
