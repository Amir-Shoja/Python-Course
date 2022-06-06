from media import Media


class Doucumentary(Media):
    def __init__(self, media):
        Media.__init__(
            self,
            media[0],
            media[1],
            media[2],
            media[3],
            media[4],
            media[5],
            media[7],
            media[8],
            media[9],
        )
        self.media = media
        self.speaker = media[12]
        self.genre = "genre"
        self.duration = "duration"

    def editInfoDoucumentary(self):
        print(
            " 1. edit name\n",
            "2. edit director\n",
            "3. edit imdb_score\n",
            "4. edit url\n",
            "5. edit cast\n",
            "6. edit year\n",
            "7. edit info\n",
            "8. edit id\n",
            "9. edit category\n",
            "10. Cancel",
        )
        c = input("\nwhich item do you want to edit? ")
        match c:
            case "1":
                self.name = input("please enter alternate name: ")
            case "2":
                self.director = input("please enter alternate director: ")
            case "3":
                self.imdb_score = input("please enter alternate imdb_score: ")
            case "4":
                self.url = input("please enter alternate url: ")
            case "5":
                self.cast = input("please enter alternate cast: ")
            case "6":
                self.year = input("please enter alternate year: ")
            case "7":
                self.info = input("please enter alternate info: ")
            case "8":
                self.id = input("please enter alternate id: ")
            case "9":
                self.category = input("please enter alternate category: ")
            case "10":
                exit()
        return self.media
