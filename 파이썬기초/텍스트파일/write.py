# 시스템 시간과 일정을 텍스트 파일에 작성
import time

lt = time.localtime()
# dateStr = '[' + str(lt.tm_year) + '년 ' +\
#           str(lt.tm_mon) + '월 ' +\
#           str(lt.tm_mday) + '일] '
dateStr = '[' + time.strftime('%Y-%m-%d %I:%M:%S %p') + '] '    #시간: H는 24시간 표현 / I는 12시간 표현

todaySchedule = input('오늘 일정: ')

file = open('C:/pythonEx/test.txt', 'w')
file.write(dateStr + todaySchedule)
file.close()