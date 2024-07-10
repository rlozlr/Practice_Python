# 일정표에서 사용자가 입력한 일정을 삭제
'''마케팅 회의, 회의록 정리, 점심 약속, 월간 업무 보고, 치과 방문, 마트 장보기'''
scheduleList = ['마케팅 회의', '회의록 정리', '점심 약속', '월간 업무 보고', '치과 방문', '마트 장보기']
print('일정표 : {}'.format(scheduleList))

remoteItem = input('삭제할 일정: ')
scheduleList.remove(remoteItem)
print('\'{}\' 삭제 완료'.format(remoteItem))
print('일정표 : [{}]'.format(scheduleList))
