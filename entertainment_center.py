import fresh_tomatoes   #importing the prebuild module provided by Udacity
import media   #importing media for using Class Movie

#creating cast_away movie instance from Movie Class 
cast_away = media.Movie("Cast away",
                        "The film depicts a FedEx employee stranded on an uninhabited island",
                        "https://upload.wikimedia.org/wikipedia/en/a/a7/Cast_away_film_poster.jpg",
                        "https://www.youtube.com/watch?v=PJvosb4UCLs")
print(cast_away.storyline)

#creating avatar movie instance from Movie Class 
avatar = media.Movie("Avatar",
                     "Story of a Marine on alien Planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#creating interstellar movie instance from Movie Class 
interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_QL50_SY1000_CR0,0,640,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

#creating walle movie instance from Movie Class
walle = media.Movie("Wall.E",
                    "In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=alIq_wG9FNk")

#creating udaan movie instance from Movie Class
udaan = media.Movie("Udaan",
                    "Expelled from his school, a 16-year old boy returns home to his abusive and oppressive father",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzgxMzExMzUwNV5BMl5BanBnXkFtZTcwMDc2MjUwNA@@._V1_QL50_.jpg",
                    "https://www.youtube.com/watch?v=wEJxe2bE-cE")
#creating udaan movie instance from Movie Class
doctor_strange = media.Movie("Doctor Strange",
                             "A former neurosurgeon embarks on a journey of healing only to be drawn into the world of the mystic arts.",
                             "http://cdn1-www.comingsoon.net/assets/uploads/gallery/doctor-strange-1403135280/cf5nqhcxiae59i9-jpg-large.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")

#creating udaan movie instance from Movie Class
star_trek_beyond = media.Movie("Star Trek Beyond",
                               "The USS Enterprise crew explores the furthest reaches of uncharted space, where they encounter a new ruthless enemy who puts them and everything the Federation stands for to the test.",
                               "http://static.rogerebert.com/uploads/movie/movie_poster/star-trek-beyond-2016/large_ghL4ub6vwbYShlqCFHpoIRwx2sm.jpg",
                               "https://www.youtube.com/watch?v=XRVD32rnzOw")

#creating udaan movie instance from Movie Class
deadpool = media.Movie("Deadpool",
                       "A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.",
                       "https://3.bp.blogspot.com/-vn2bVLNwh9s/Vra6QSY_V1I/AAAAAAAAES4/e4N6No_5oJo/s1600/Deadpool_VerD-IMAX_Revised_RatedPoster_sRGB.JPG",
                       "https://www.youtube.com/watch?v=FyKWUTwSYAs" )

#creating udaan movie instance from Movie Class
arrival = media.Movie("Arrival",
                      "A linguist is recruited by the military to assist in translating alien communications.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_QL50_SY1000_CR0,0,640,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

#adding all movies into List movies                      
movies = [cast_away,avatar,interstellar,walle,udaan,doctor_strange,star_trek_beyond,deadpool,arrival]

#calling the function from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)


