def save_result(old_func):
    def new_func(*args, **kwargs):
        result = old_func(*args, **kwargs)
        with open('results.txt', 'a') as f:
            print(f'{result}', file = f)
        return new_func
     


