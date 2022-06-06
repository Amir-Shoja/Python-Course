from pytube import YouTube
from actor import Actor


class Media:
    def __init__(self, ID, NAME, DIRECTOR, YEAR, SCORE, CASTS, INFO, CATEGORY, URL):
        self.name = NAME
        self.director = DIRECTOR
        self.imdb_score = SCORE
        self.url = URL
        self.cast = CASTS
        self.year = YEAR
        self.info = INFO
        self.id = ID
        self.category = CATEGORY

    def showInfo(self):
        print(self.info)

    def download(self):
        try:
            YouTube(self.url).streams.first().download()
            print("Download Completed!")
        except:
            print("Connection Error")

    def listCasts(self):
        casts = self.cast.split(" , ")
        for actor in casts:
            Actor(actor).show()

    def showInfo(self):
        print(self.info)

    def show(self):
        print(
            f"ID: {self.id},  Name{self.name}, Category: {self.category},  Year: {self.year},  Director: {self.director},  IMDB Score: {self.imdb_score}",
            "\n----------------------" * 5,
        )
