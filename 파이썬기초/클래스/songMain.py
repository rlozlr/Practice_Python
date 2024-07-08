import mp3Player as mp3

s1 = mp3.Song('신호등', '이무진', 3)
s2 = mp3.Song('문어의꿈', '안예은', 4)
s3 = mp3.Song('Butter', 'BTS', 2)
s4 = mp3.Song('홀씨', '아이유', 5)
s5 = mp3.Song('우리의꿈', '코요테', 3)

player = mp3.Player()
player.addSong(s1)
player.addSong(s2)
player.addSong(s3)
player.addSong(s4)
player.addSong(s5)
player.setIsLoop(False)
player.shuffle()
player.play()