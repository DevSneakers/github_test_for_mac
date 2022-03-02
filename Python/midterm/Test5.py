m_name = input("Mother's name : ")
m_age = int(input("Mother's age : "))
f_name = input("Father's name : ")
f_age = int(input("Father's age : "))

if m_age == f_age:
    print('{} and {} are the same age.'.format(m_name, f_name))
elif m_age > f_age:
    print('Older :', m_name)
    print('Younger :', f_name)
    print('Age gap :', (m_age-f_age))
else:
    print('Older :', f_name)
    print('Younger :', m_name)
    print('Age gap :', (f_age-m_age))