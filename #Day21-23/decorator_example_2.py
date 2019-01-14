def make_html(func, var):
    def wrapped(func):
        return var + func() + var
    return wrapped


# def make_italic(func):
#     def wrapped():
#         return "<i>" + func() + "</i>"
#     return wrapped


@make_html('p')
@make_html('strong')
def getText(text='I code with PyBites'):
    return text


print(getText())
