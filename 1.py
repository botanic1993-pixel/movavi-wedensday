def save_result(old_func):
    def new_func(*args, **kwargs):
        result = old_func(*args, **kwargs)
        with open('results.txt', 'a') as f:
            print(f'{result}', file = f)
        return new_func
     #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



