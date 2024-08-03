# 문장에서 비속어가 있는지 알아내기
wrongWord = ["짭새", '담탱이', "꼰대", '찐따']
sentence = '꼰대 같은 담탱이가 짭새처럼 등장해 찐따를 구했다.'
for word in wrongWord:
    if word in sentence:
        print('비속어: {}'.format(word))