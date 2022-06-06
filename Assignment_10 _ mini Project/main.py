from clip import Clip
from media import Media
from film import Film
from series import Series
from documentary import Documentary


class main:
    def __init__(self):

        f = open("Data.csv")
        all_data = f.read()
        parts = all_data.split("\n")

        self.medias = []

        for i in range(len(parts)):
            info = parts[i].split(",")
            if info[9] == "film":
                self.medias.append(Film())

            elif info[9] == "series":
                self.medias.append(Series())

            elif info[9] == "documentary":
                self.medias.append(Documentary())

            elif info[9] == "clip":
                self.medias.append(Clip())

            print("✔ data loaded!")

            self.menu()

    def menu(self):
        choose = input(
            "1- Add New Media\n",
            "2- Edit\n",
            "3- Delete\n",
            "4- Search by name \n",
            "5- Search by duration \n",
            "6- Show Media List\n",
            "7- Show actors\n",
            "8- Download\n",
            "9- save changes and Exit\n",
        )
        try:
            match choose:
                case "1":
                    self.AddMedia()
                case "2":
                    self.EditMedia()
                case "3":
                    self.DeleteMedia()
                case "4":
                    self.SearchByName()
                case "5":
                    self.SearchByDuration()
                case "6":
                    self.ShowMediaList()
                case "7":
                    self.ShowActors()
                case "8":
                    self.DownloadMedia()
                case "9":
                    self.SaveAndExit()
        except:
            print("Wrong input !")

    def AddMedia(self):
        category = input("enter the category: ( film - clip - documentary - series )\n")
        id = input("id: ")
        name = input("name: ")
        year = input("year: ")
        director = input("director: ")
        score = input("score: ")
        duration = input("duration: ")
        url = input("url: ")
        info = input("info: ")
        casts = input("casts: ")
        genre = input("genre: ")
        episode = input("episode: ")
        subject = input("subject: ")
        company = input("company: ")
        media_info = [
            id,
            category,
            name,
            year,
            director,
            score,
            duration,
            url,
            info,
            casts,
            genre,
            episode,
            subject,
            company,
        ]

        if category == "film":
            self.medias.append(Film(media_info))
        elif category == "clip":
            self.medias.append(Clip(media_info))
        elif category == "documentary":
            self.medias.append(Documentary(media_info))
        elif category == "series":
            self.medias.append(Series(media_info))
        else:
            print("wrong input !")

        self.menu()

    def EditMedia(self):

        print("Editing a media:")
        name = input("enter name of media that you whant to edit:")
        for media in self.medias:
            if name == media.name:
                if media.category == "film":
                    media = media.editInfoFilm()
                    break
                elif media.category == "documentary":
                    media = media.editInfoDoucumentary()
                    break
                elif media.category == "clip":
                    media = media.editInfoClip()
                    break
                elif media.category == "series":
                    media = media.editInfoSeries()
                    break
                else:
                    print("there is a problem in the data")
                    break
        else:
            print("not exists!")
        self.menu()

    def DeleteMedia(self):
        print("Deleting Media ...")
        user_input = input("please enter the name of media or id: ")

        for media in self.medias:
            if user_input == media.name or user_input == media.id:
                answer = input("are you sure you want delete this media? \n  y?  n? ")
                if answer == "y":
                    self.medias.remove(media)
                    break
        else:
            print("not exists")
        self.menu()

    def SearchByName(self):
        user_input = input("enter 'Name' of media: ")
        for media in self.medias:
            if media.name == user_input:
                media.show()
                break
        else:
            print("not found")
        self.menu()

    def SearchByDuration(self):
        print("Search media with a specific duration")
        first_duration = input("enter first duration with format {00:00}: ")
        first_duration = first_duration.split(":")
        first_duration = [int(i) for i in first_duration]
        sec_duration = input("enter second duration with format {00:00}: ")
        sec_duration = sec_duration.split(":")
        sec_duration = [int(i) for i in sec_duration]
        for media in self.medias:
            if media.category != "series":
                media_duration = media.duration.split(":")
                media_duration = [int(i) for i in media_duration]
                if media_duration >= first_duration and media_duration <= sec_duration:
                    media.show()
        self.menu()

    def ShowMediaList(self):
        for media in self.medias:
            media.show()
        self.menu()

    def ShowActors(self):
        user_input = input(
            "please enter the name of media or id for show information: "
        )
        for media in self.medias:
            if user_input == media.name or user_input == media.id:
                media.listCasts()
                break
        else:
            print("not exists")
        self.menu()

    def DownloadMedia(self):
        user_input = input("please enter the name of media or id for download: ")
        for media in self.medias:
            if user_input == media.name or user_input == media.id:
                media.download()
                break
        else:
            print("not exists")
        self.menu()

    def SaveAndExit(self):
        out = open("Data.csv", "w")
        for media in self.medias:
            out.write(
                media.id
                + ","
                + media.category
                + ","
                + media.name
                + ","
                + media.year
                + ","
                + media.director
                + ","
                + media.imdb_score
                + ","
                + media.duration
                + ","
                + media.url
                + ","
                + media.info
                + ","
                + media.cast
                + ","
                + media.genre
                + ","
                + media.episode
                + ","
                + media.subject
                + ","
                + media.company
            )
            if media != self.medias[-1]:
                out.write("\n")
        out.close()
        print("Done")
        exit()
