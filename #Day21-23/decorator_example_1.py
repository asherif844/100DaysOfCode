def make_bold(func):
    def wrapped():
        return "<b>" + func() + "</b>"
    return wrapped


def make_italic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped


@make_bold
@make_italic
def hello():
    return 'hello world'


print(hello())
