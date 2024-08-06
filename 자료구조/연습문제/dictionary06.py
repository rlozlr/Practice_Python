# 다음 문장에서 비속어를 찾고 비속어를 표준어로 변경하는 프로그램 만들기
# 강도는 서로 쪼개다, 짭새를 보고 빠르게 따돌리며 먹튀했다.
sentence = '강도는 서로 쪼개다, 짭새를 보고 빠르게 따돌리며 먹튀했다.'

words = {
    '쪼개다':'웃다',
    '짭새':'경찰',
    '먹튀':'먹고 도망'
}
keys = list(words.keys())

for key in keys:
    if key in sentence:
        print('key : {}'.format(key))
        print('word[{}] : {}'.format(key, words[key]))
        sentence = sentence.replace(key, words[key])
print(sentence)