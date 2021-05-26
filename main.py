

def insertInDb(nameOfAnime, favAnime):
	f = open("db.txt", "w")
	f.write(nameOfAnime + ", " + favAnime)
	f.close()
	





def userInput():
	nameOfAnime = input("Name of Anime: ")
	favAnime = input("What is your favorite Anime? ")
	Gogeta = input("Who is better Goku or Vegeta? ")

	insertInDb(nameOfAnime,favAnime)




def main():
	userInput()













if __name__ == "__main__":
    main()























