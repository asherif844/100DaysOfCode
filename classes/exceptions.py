class GitHubApiError(Exception):

    def __init__(self, status_code):
        if status_code == 403:
            message = 'Rate Limit Reached.'
        else:
            message = f'Status code was: {status_code}'
        
        super().__init__(message)



raise GitHubApiError(403)

1/0

2+'3'

int('a')

my_dict = {"hello":"world"}

my_dict["hello"]


class MyError(Exception):
    def __init__(self,message):
        new_message = f"!!! Error system failure: {message}"

        super().__init__(new_message)

raise MyError('ahmed')


for num in range(5,-1,-1):
    try:
        print(5/num)
    except:
        0