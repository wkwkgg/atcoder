yyyy, mm, dd = map(int, input().split("/"))
print('Heisei' if yyyy <= 2019 and mm <= 4 and dd <= 30 else 'TBD')