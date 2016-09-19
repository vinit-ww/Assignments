class Song(object):

    def __init__(self , lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

            
Happy_birthday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
bulls_song = Song(["Rose is Red",
                   "Sky is blue"])
Happy_birthday.sing_me_a_song()
bulls_song.sing_me_a_song()
