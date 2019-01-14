def make_html(tag_name):
    def tags_decorator(func):
        def func_wrapper():
            return "<{0}>{1}</{0}>".format(tag_name, func())
        return func_wrapper
    return tags_decorator


@make_html("p")
@make_html("strong")
def get_text(text='I code with PyBites'):
    return text


print(get_text())
