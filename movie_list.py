from movies import movie_lists

movies = {
    "action": [
        {"name": "🔥 John Wick (2014)", "image": "https://m.media-amazon.com/images/M/MV5BMTU2NjA1ODgzNF5BMl5BanBnXkFtZTgwMTM2MTI4MjE@._V1_.jpg"},
        {"name": "🔥 Mad Max: Fury Road (2015)", "image": "https://m.media-amazon.com/images/M/MV5BN2EwM2I5OWMtMGQyMi00Zjg1LWJkNTctZTdjYTA4OGUwZjMyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg"},
        {"name": "🔥 The Dark Knight (2008)", "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg"},
        {"name": "🔥 Inception (2010)", "image": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg"},
        {"name": "🔥 Gladiator (2000)", "image": "https://m.media-amazon.com/images/M/MV5BMzQxNzQzOTQwM15BMl5BanBnXkFtZTgwMDQ2NTcwMTE@._V1_.jpg"},
        {"name": "🔥 Avatar: The Way of Water (2022)", "image": "https://m.media-amazon.com/images/M/MV5BYjhiNjBlODUtY2ZiOC00YjVlLWFlNzAtNTVhNzU1MWRmOTU3XkEyXkFqcGdeQXVyMjkwOTAyMDU@._V1_.jpg"},
        {"name": "🔥 Top Gun: Maverick (2022)", "image": "https://m.media-amazon.com/images/M/MV5BZWYzOGEwNTgtNWU3NS00ZGQ0LThjODUtM2FiODU4M2Y3NTlhXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_.jpg"},
        {"name": "🔥 Die Hard (1988)", "image": "https://m.media-amazon.com/images/M/MV5BMzYyZjgxNjAtNWIxOC00YjEwLTkwZTUtN2ExMThjOWVmMGM0XkEyXkFqcGdeQXVyNjQ1MDcxNzM@._V1_.jpg"},
        {"name": "🔥 The Matrix (1999)", "image": "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"},
        {"name": "🔥 Avengers: Endgame (2019)", "image": "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzY2NzM@._V1_.jpg"},
        {"name": "🔥 Mission: Impossible - Fallout (2018)", "image": "https://m.media-amazon.com/images/M/MV5BMTk3NDY5MTU0NV5BMl5BanBnXkFtZTgwNDI3MDE1NTM@._V1_.jpg"},
        {"name": "🔥 Spider-Man: Into the Spider-Verse (2018)", "image": "https://m.media-amazon.com/images/M/MV5BMjMwNDkxMTgzOF5BMl5BanBnXkFtZTgwNTkwNTQ3NjM@._V1_.jpg"},
        {"name": "🔥 Extraction (2020)", "image": "https://m.media-amazon.com/images/M/MV5BMDJiNzUwYzEtNmQ2Yy00NWE4LWEwNzctM2M0MjE0OGUxZTA3XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg"},
        {"name": "🔥 Dune: Part Two (2024)", "image": "https://m.media-amazon.com/images/M/MV5BODUwNDNjYzctODUxNy00NTZlLTg4ODEtY2Y3NmNhNzcwNDRjXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_.jpg"},
        {"name": "🔥 Terminator 2: Judgment Day (1991)", "image": "https://m.media-amazon.com/images/M/MV5BMGU2NzRmZjUtOGUxYS00ZjdjLWEwZWItY2NlM2JhNjkxNTFmXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"}
    ],
    "comedy": [
        {"name": "😂 Superbad (2007)", "image": "https://m.media-amazon.com/images/M/MV5BMTc0NzgxMzQ2N15BMl5BanBnXkFtZTcwMzQ2NzcyMw@@._V1_.jpg"},
        {"name": "😂 The Hangover (2009)", "image": "https://m.media-amazon.com/images/M/MV5BMTU1MDA1MTYwMF5BMl5BanBnXkFtZTcwMDcxMzA1Mw@@._V1_.jpg"},
        {"name": "😂 Free Guy (2021)", "image": "https://m.media-amazon.com/images/M/MV5BOTY2NzFjODctOWUzMC00MGY1LWEwOWEtYjBkZmFlYmE3MDgyXkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_.jpg"},
        {"name": "😂 Home Alone (1990)", "image": "https://m.media-amazon.com/images/M/MV5BMzFkM2YwOTQtYzk2Mi00N2VlLWE3NTItN2YwNDg1YmY0ZDNmXkEyXkFqcGdeQXVyMTA0MTM5NjI2._V1_.jpg"},
        {"name": "😂 The Mask (1994)", "image": "https://m.media-amazon.com/images/M/MV5BOWExYjI5MzktNTRhNi00YzQ4LThjMTEtNzg4ODU4YjljYmFmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"},
        {"name": "😂 Rush Hour (1998)", "image": "https://m.media-amazon.com/images/M/MV5BMWM2MDNhZGYtYTRiNS00Nzg0LWIwNDAtYzFkNWUxN2VlZjNhXkEyXkFqcGdeQXVyMTA0MTM5NjI2._V1_.jpg"},
        {"name": "😂 We're the Millers (2013)", "image": "https://m.media-amazon.com/images/M/MV5BMjA5Njc0MzgxNF5BMl5BanBnXkFtZTcwMjUwNjYwOQ@@._V1_.jpg"},
        {"name": "😂 21 Jump Street (2012)", "image": "https://m.media-amazon.com/images/M/MV5BMTc3NzQ3OTg3NF5BMl5BanBnXkFtZTcwMjk5NTcxNw@@._V1_.jpg"},
        {"name": "😂 Grown Ups (2010)", "image": "https://m.media-amazon.com/images/M/MV5BMjA0Nzg0MDM0N15BMl5BanBnXkFtZTcwMjg4OTU1Mw@@._V1_.jpg"},
        {"name": "😂 Central Intelligence (2016)", "image": "https://m.media-amazon.com/images/M/MV5BMjA1MDc5MjI5NV5BMl5BanBnXkFtZTgwNjU5NTU0ODE@._V1_.jpg"},
        {"name": "😂 Dumb and Dumber (1994)", "image": "https://m.media-amazon.com/images/M/MV5BZDg1ZWEwMDYtYWJjMy00OTU0LWIwN2ItYzVmOWYyZDE3NWI5XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"},
        {"name": "😂 Ted (2012)", "image": "https://m.media-amazon.com/images/M/MV5BMTQ1MzM3MDM5N15BMl5BanBnXkFtZTcwMjg4MDAzNw@@._V1_.jpg"},
        {"name": "😂 Deadpool (2016)", "image": "https://m.media-amazon.com/images/M/MV5BYzE5MjY1ZDgtMTkyNC00MTMyLThhMjAtZGI5OTE1NzFlZGJjXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"},
        {"name": "😂 Knives Out (2019)", "image": "https://m.media-amazon.com/images/M/MV5BMGUwZjliMTAtNTg1YS00NzQ3LTg4Y2QtM2M4YzA3Yjk4NzhiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg"},
        {"name": "😂 Barbie (2023)", "image": "https://m.media-amazon.com/images/M/MV5BNjU3N2QxNzYtMjk1NC00MTc4LTk1NTQtMmUxNTljM2I0NDA5XkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_.jpg"}
    ],
    "drama": [
        {"name": "🎭 Forrest Gump (1994)", "image": "https://m.media-amazon.com/images/M/MV5BMTgxNTAyNTg1OV5BMl5BanBnXkFtZTcwNDc5MDQzNQ@@._V1_.jpg"},
        {"name": "🎭 The Shawshank Redemption (1994)", "image": "https://m.media-amazon.com/images/M/MV5BNDE3ODcxNzMtY2YzZC00NmNlLWJiNDMtZDFiYmUyNzM3NTc5XkEyXkFqcGdeQXVyNTc1NTQ4MA@@._V1_.jpg"},
        {"name": "🎭 Fight Club (1999)", "image": "https://m.media-amazon.com/images/M/MV5BODQ0OWJiMzktYjNlYi00MzcwLThlZWMtMzRkYTY4ZDgxNzgxXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
        {"name": "🎭 The Godfather (1972)", "image": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
        {"name": "🎭 Interstellar (2014)", "image": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2ExOS00NGExLTk3YmQtY2YzOGM2MWFhZTEwXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg"},
        {"name": "🎭 Titanic (1997)", "image": "https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg"},
        {"name": "🎭 The Wolf of Wall Street (2013)", "image": "https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_.jpg"},
        {"name": "🎭 Oppenheimer (2023)", "image": "https://m.media-amazon.com/images/M/MV5BMDBmYTZjNjUtN2M1MS00MTQ2LTk2ODgtNzc2M2QyZGE5NTVjXkEyXkFqcGdeQXVyNzAwMjU2MTY@._V1_.jpg"},
        {"name": "🎭 Whiplash (2014)", "image": "https://m.media-amazon.com/images/M/MV5BMTU4NjY3NzExM15BMl5BanBnXkFtZTgwOTkyMjQyMDE@._V1_.jpg"},
        {"name": "🎭 The Green Mile (1999)", "image": "https://m.media-amazon.com/images/M/MV5BMTUxMzQyNjA5MF5BMl5BanBnXkFtZTYwOTU2NTY3._V1_.jpg"},
        {"name": "🎭 Parasite (2019)", "image": "https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwN2Q5NTVkXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_.jpg"},
        {"name": "🎭 Schindler's List (1993)", "image": "https://m.media-amazon.com/images/M/MV5BNDE4OTMxMTctNWY0YS00N2YwLWE0M2YtODY2SmFiYjM2ZmQwXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_.jpg"},
        {"name": "🎭 Joker (2019)", "image": "https://m.media-amazon.com/images/M/MV5BNGVjNWI4ZGUtNzE0MS00YTJkLTkwY2ItNzk1YmLkYzA3YTkxXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_.jpg"},
        {"name": "🎭 La La Land (2016)", "image": "https://m.media-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_.jpg"},
        {"name": "🎭 The Pursuit of Happyness (2006)", "image": "https://m.media-amazon.com/images/M/MV5BMTQ5NjQ0NjI3M15BMl5BanBnXkFtZTcwMTc5MDIzMw@@._V1_.jpg"}
    ],
    "horror": [
        {"name": "😱 The Conjuring (2013)", "image": "https://m.media-amazon.com/images/M/MV5BMTM3NjA1NDMyMV5BMl5BanBnXkFtZTcwMDQzNDMzOQ@@._V1_.jpg"},
        {"name": "😱 It (2017)", "image": "https://m.media-amazon.com/images/M/MV5BZDVkZmI0YzAtNzdjMy00YWJiLWFkNDAtYTM1NTYwNTAwYjUxXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_.jpg"},
        {"name": "😱 Hereditary (2018)", "image": "https://m.media-amazon.com/images/M/MV5BMjE0NzIwMjExMV5BMl5BanBnXkFtZTgwNjIzMzg1NTM@._V1_.jpg"},
        {"name": "😱 A Quiet Place (2018)", "image": "https://m.media-amazon.com/images/M/MV5BMjI0MDMzNTQ0M15BMl5BanBnXkFtZTgwMTM5NzM3NDM@._V1_.jpg"},
        {"name": "😱 Get Out (2017)", "image": "https://m.media-amazon.com/images/M/MV5BMjUxMDQwNjcyNl5BMl5BanBnXkFtZTgwNzcwMzc0MDI@._V1_.jpg"},
        {"name": "😱 Insidious (2010)", "image": "https://m.media-amazon.com/images/M/MV5BMTYyMTcxNzc5M15BMl5BanBnXkFtZTcwOTg2ODE2NA@@._V1_.jpg"},
        {"name": "😱 Sinister (2012)", "image": "https://m.media-amazon.com/images/M/MV5BMjI5NDExNjI3NF5BMl5BanBnXkFtZTcwMzg1MTI2OA@@._V1_.jpg"},
        {"name": "😱 Midsommar (2019)", "image": "https://m.media-amazon.com/images/M/MV5BMzQxNzQzOTQwM15BMl5BanBnXkFtZTgwMDQ2NTcwMTE@._V1_.jpg"},
        {"name": "😱 The Exorcist (1973)", "image": "https://m.media-amazon.com/images/M/MV5BYzA2Nzk5M2EtNWY4Yi00ZDY4LWI0NTEtYTg0YmUwYWVkM2E1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"},
        {"name": "😱 Smile (2022)", "image": "https://m.media-amazon.com/images/M/MV5BZjE2ZWIwMWEtNWNjMy00MGE5LWIzYTUtZDBkZTM1MTUzMTE1XkEyXkFqcGdeQXVyMTA3MDk2NDg2._V1_.jpg"},
        {"name": "😱 Talk to Me (2022)", "image": "https://m.media-amazon.com/images/M/MV5BYmNhMjI1YzAtNDZlMC00OTNiLTg3MjctOTNhMGExYmU0MGNhXkEyXkFqcGdeQXVyMTM1NjM2ODg1._V1_.jpg"},
        {"name": "😱 The Ring (2002)", "image": "https://m.media-amazon.com/images/M/MV5BNDA1MTU1MzYxN15BMl5BanBnXkFtZTYwNTcxNTc5._V1_.jpg"},
        {"name": "😱 Don't Breathe (2016)", "image": "https://m.media-amazon.com/images/M/MV5BZGI5ZTU2M2YtZWY4MC00ZDFhLTliYTItZTk1NjdlN2NkMzg2XkEyXkFqcGdeQXVyMjY5ODI4NDk@._V1_.jpg"},
        {"name": "😱 Us (2019)", "image": "https://m.media-amazon.com/images/M/MV5BZTliNWJhM2YtNDc1MC00YTE1LWE2NTktMWM0MWZmZTYwNDU3XkEyXkFqcGdeQXVyNTMxMzgxMTE@._V1_.jpg"},
        {"name": "😱 Evil Dead Rise (2023)", "image": "https://m.media-amazon.com/images/M/MV5BMmY5ZDRhODQtNjM5ZC00YTI0LWI0YjAtYjI0ZTAzYmJiYTM2XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg"}
    ]
}

random_movies = movie_lists