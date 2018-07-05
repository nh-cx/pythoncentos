department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 45678.123456
COURSE_FEES_Python = 1234.3456

Oldline1 = 'Department1 name:%-11sManager:%-11sCOURSE FEES:%-11.2fThe End!' % (depart1_m, depart1_m, COURSE_FEES_SEC)
Oldline2 = 'Department1 name:%-11sManager:%-11sCOURSE FEES:%-11.2fThe End!' % (depart2_m, depart2_m, COURSE_FEES_Python)

# 批量注释使用Ctrl+/
# newline1 = 'Department1 name:{0:<11}Manager:{1:<11}COURSE FEES:{2:<11.2f}The End!'.format(department1, depart1_m, COURSE_FEES_SEC)
# newline2 = 'Department1 name:{0:<11}Manager:{1:<11}COURSE FEES:{2:<11.2f}The End!'.format(department2, depart2_m, COURSE_FEES_Python)

length = len(Oldline1)
print('='*length)
print(Oldline1)
print(Oldline2)
print('='*length)


# length = len(newline1)
# print('='*length)
# print(newline1)
# print(newline2)
# print('='*length)
