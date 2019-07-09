from functools import wraps


def make_html(func):
    @wraps(func)
    def wrapper(*args, **kwargs):


@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text
