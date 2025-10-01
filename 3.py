second = int(input())
hours = second // 3600
second = second % 3600
minutes = second // 60
second = second % 60
print(f'{hours:02}:{minutes:02}:{second:02}')

