from time import sleep
import random
class Song:
    def __init__(self, t, s, pt):
        self.title =t
        self.singer = s
        self.play_time = pt

    def printSongInfo(self):
        print(f'Title: {self.title}, Singer: {self.singer}, Play time: {self.play_time}')


class Player:

    def __init__(self):
        self.songList = []
        self.isLoop = False

    def addSong(self, s):
        self.songList.append(s)

    def play(self):
        if self.isLoop:
            while self.isLoop:
                for s in self.songList:
                    print(f'Title: {s.title}, Singer: {s.singer}, Play time: {s.play_time}sec')
                    sleep(s.play_time)
        else:
            for s in self.songList:
                print(f'Title: {s.title}, Singer: {s.singer}, Play time: {s.play_time}sec')
                sleep(s.play_time)

    def shuffle(self):
        random.shuffle(self.songList)

    def setIsLoop(self, flag):
        self.isLoop = flag
