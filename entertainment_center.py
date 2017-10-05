import media
import fresh_tomatoes

up = media.Movie(movie_title= "Up" ,
           movie_storyline = "Seventy-eight year old Carl Fredricksen travels to Paradise Falls in his home equipped with balloons, inadvertently taking a young stowaway." ,
           poster_image= "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1_SY1000_CR0,0,664,1000_AL_.jpg",
           trailer_youtube= 'https://www.youtube.com/watch?v=pkqzFUhGPJg')

zoo = media.Movie(movie_title= "Zootopia",
                 trailer_youtube = "https://www.youtube.com/watch?v=jWM0ct-OLsM",
                 movie_storyline="In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy.",
                 poster_image= "https://images-na.ssl-images-amazon.com/images/M/MV5BOTMyMjEyNzIzMV5BMl5BanBnXkFtZTgwNzIyNjU0NzE@._V1_SY1000_SX675_AL_.jpg")

incredibles = media.Movie(movie_title= "The Incredibles",
                 trailer_youtube = "https://www.youtube.com/watch?v=eZbzbC9285I",
                 movie_storyline ="A family of undercover superheroes, while trying to live the quiet suburban life, are forced into action to save the world.",
                 poster_image= "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY5OTU0OTc2NV5BMl5BanBnXkFtZTcwMzU4MDcyMQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg")

justiceL = media.Movie(movie_title= "Justice League",
                 trailer_youtube = "https://www.youtube.com/watch?v=DblEwHkde8U",
                 movie_storyline="SuperHeroes Team-up to save Earth",
                 poster_image= "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI2NjI2MDQ0NV5BMl5BanBnXkFtZTgwMTc1MjAwMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg")

tdk = media.Movie(movie_title= "The Dark Knight",
                 trailer_youtube = "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                 movie_storyline="When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                 poster_image= "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg")

walter = media.Movie(movie_title= "The Secret Life of Walter Mitty",
                 trailer_youtube = "https://www.youtube.com/watch?v=QD6cy4PBQPI",
                 movie_storyline="When his job along with that of his co-worker are threatened, Walter takes action in the real world embarking on a global journey that turns into an adventure more extraordinary than anything he could have ever imagined.",
                 poster_image= "https://images-na.ssl-images-amazon.com/images/M/MV5BODYwNDYxNDk1Nl5BMl5BanBnXkFtZTgwOTAwMTk2MDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg")

drishyam = media.Movie(movie_title= "Drishyam",
                 trailer_youtube = "https://www.youtube.com/watch?v=AuuX2j14NBg",
                 movie_storyline="Desperate measures are taken by a man who tries to save his family from the dark side of the law, after they commit an unexpected crime.",
                 poster_image= "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYyMjgyNDY3N15BMl5BanBnXkFtZTgwOTMzNTE5NTE@._V1_SY1000_CR0,0,692,1000_AL_.jpg")

tid = media.Movie(movie_title= "3 Idiots",
                 trailer_youtube = "https://www.youtube.com/watch?v=K0eDlFX9GMc",
                 movie_storyline="Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them 'idiots'.",
                 poster_image= "https://images-na.ssl-images-amazon.com/images/M/MV5BZWRlNDdkNzItMzhlZC00YTdmLWIwNjktYjY5NjQ1ZmQ3N2FkXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,747,1000_AL_.jpg")

dangal = media.Movie(movie_title= "Dangal",
                 trailer_youtube = "https://www.youtube.com/watch?v=x_7YlGv9u1g",
                 movie_storyline="Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle towards glory at the Commonwealth Games in the face of societal oppression.",
                 poster_image= "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ4MzQzMzM2Nl5BMl5BanBnXkFtZTgwMTQ1NzU3MDI@._V1_SY1000_CR0,0,713,1000_AL_.jpg")


movies = [up,zoo,incredibles,justiceL,tdk,walter,drishyam,tid,dangal]

fresh_tomatoes.open_movies_page(movies)




