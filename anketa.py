from datetime import datetime
current_datetime = datetime.now()

print('Вас приветствует анкета, заполните пожалуйста свои данные.')
user_info = []
user_info_2 = ['Имя: ', 'вашу дату рождения в формате yyyy/mm/dd: ',
               'Любимый фильм: ', 'Возраст: ', 'Дата рождения: ']
for i in range(3):
    user_int = input(f'Введите {user_info_2[i]}')
    user_info.append(user_int)
date = user_info[1].replace('/', '.')


def age(year, mounth, day):
    current_year = current_datetime.year
    current_mounth = current_datetime.month
    current_day = current_datetime.day
    result = current_year - year
    if mounth > current_mounth:
        result -= 1
    if mounth == current_mounth:
        if day > current_day:
            result -= 1
    elif day > current_day:
        result -= 1
    return result
age_user = age(int(date[:4]), int(date[5:7]),int(date[-1]))

def count_spase(user):

    if len(user[0]) > len(user[1]) and len(user[0]) > len(user[2]):
        len_pr = len(user[0]) + 17
    elif len(user[1]) > len(user[0]) and len(user[1]) > len(user[2]):
        len_pr = len(user[1]) + 17
    else:
        len_pr = len(user[2]) + 17
    return len_pr
len_pr = count_spase(user_info)


ank = 'Анкета'
n_sp = len_pr - len(user_info_2[0]) - len(user_info[0])
d_sp = len_pr - len(user_info_2[-1]) - len(date)
a_sp = len_pr - len(user_info_2[-2]) - len(str(age_user))
f_sp = len_pr - len(user_info_2[-3]) - len(user_info[2])
ank_sp = (len_pr - len(ank)) // 2

print('''
%(ank_l)sАнкета%(ank_l)s
Имя:%(n_l)s %(n)s
Дата Рождения:%(d_l)s %(d)s
Возраст:%(a_l)s %(y)s
Любимый фильм:%(f_l)s %(f)s''' % {
    'n': user_info[0],
    'd': date,
    'y': age_user,
    'f': user_info[2],
    'n_l': ' '* n_sp,
    'd_l': ' '* d_sp,
    'a_l': ' '* a_sp,
    'f_l': ' '* f_sp,
    'ank_l': ' '* ank_sp
})