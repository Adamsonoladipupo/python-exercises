from fastapi import FastAPI, Body
app = FastAPI()

MOVIES = [
{"ID":1,"Moviename":"Inception","Genre":"Sci-Fi","YearOfRelease":2010,"Budget":160000000,"Revenue":829895144,"DirectorName":"Christopher Nolan"},
{"ID":2,"Moviename":"The Godfather","Genre":"Crime","YearOfRelease":1972,"Budget":6000000,"Revenue":246120974,"DirectorName":"Francis Ford Coppola"},
{"ID":3,"Moviename":"Pulp Fiction","Genre":"Crime","YearOfRelease":1994,"Budget":8000000,"Revenue":213928762,"DirectorName":"Quentin Tarantino"},
{"ID":4,"Moviename":"The Dark Knight","Genre":"Action","YearOfRelease":2008,"Budget":185000000,"Revenue":1004558444,"DirectorName":"Christopher Nolan"},
{"ID":5,"Moviename":"Forrest Gump","Genre":"Drama","YearOfRelease":1994,"Budget":55000000,"Revenue":678222284,"DirectorName":"Robert Zemeckis"},
{"ID":6,"Moviename":"Titanic","Genre":"Romance","YearOfRelease":1997,"Budget":200000000,"Revenue":2187463944,"DirectorName":"James Cameron"},
{"ID":7,"Moviename":"The Matrix","Genre":"Sci-Fi","YearOfRelease":1999,"Budget":63000000,"Revenue":466364845,"DirectorName":"Lana Wachowski, Lilly Wachowski"},
{"ID":8,"Moviename":"Gladiator","Genre":"Action","YearOfRelease":2000,"Budget":103000000,"Revenue":460583960,"DirectorName":"Ridley Scott"},
{"ID":9,"Moviename":"Avatar","Genre":"Sci-Fi","YearOfRelease":2009,"Budget":237000000,"Revenue":2847246203,"DirectorName":"James Cameron"},
{"ID":10,"Moviename":"Jurassic Park","Genre":"Adventure","YearOfRelease":1993,"Budget":63000000,"Revenue":1070000000,"DirectorName":"Steven Spielberg"},
{"ID":11,"Moviename":"The Lion King","Genre":"Animation","YearOfRelease":1994,"Budget":45000000,"Revenue":968483777,"DirectorName":"Roger Allers, Rob Minkoff"},
{"ID":12,"Moviename":"Interstellar","Genre":"Sci-Fi","YearOfRelease":2014,"Budget":165000000,"Revenue":701729206,"DirectorName":"Christopher Nolan"},
{"ID":13,"Moviename":"The Avengers","Genre":"Action","YearOfRelease":2012,"Budget":220000000,"Revenue":1518812988,"DirectorName":"Joss Whedon"},
{"ID":14,"Moviename":"Frozen","Genre":"Animation","YearOfRelease":2013,"Budget":150000000,"Revenue":1276480335,"DirectorName":"Chris Buck, Jennifer Lee"},
{"ID":15,"Moviename":"Titanic II","Genre":"Drama","YearOfRelease":2010,"Budget":5000000,"Revenue":12300000,"DirectorName":"Shane Van Dyke"},
{"ID":16,"Moviename":"Guardians of the Galaxy","Genre":"Sci-Fi","YearOfRelease":2014,"Budget":170000000,"Revenue":773328629,"DirectorName":"James Gunn"},
{"ID":17,"Moviename":"Incredibles 2","Genre":"Animation","YearOfRelease":2018,"Budget":200000000,"Revenue":1242805359,"DirectorName":"Brad Bird"}
]

class Movie():
    ID: int
    MovieName: str
    Genre: str
    YearOfRelease: int
    Budget: int
    Revenue: float
    DirectorName: str

    def __init__(self, ID:int, Moviename:str, Genre: str, YearOfRelease:int, Budget:int, Revenue:float, DirectorName:str):
        self.ID = ID
        self.MovieName = Moviename
        self.Genre = Genre
        self.YearOfRelease = YearOfRelease
        self.Budget = Budget
        self.Revenue = Revenue
        self.DirectorName = DirectorName

@app.get("/movies")
def get_all_movies():
    return MOVIES

@app.get("/movies/{ID}")
def get_movie(ID:int):
    movieByID=None
    for movie in MOVIES:
        if movie["ID"] == ID:
            movieByID = movie
            break
    return movieByID

@app.get("/moviesgenres")
def get_movie_genres(genre:str):
    movieGenresByID=[]
    for movie in MOVIES:
        if movie["Genre"].lower() == genre.lower():
            movieGenresByID.append(movie)

    return movieGenresByID

@app.get("/year_of_release/{year_of_release}")
def get_year_of_release(year:int):
    movieYearOfRealease=[]
    for movie in MOVIES:
        if movie["YearOfRelease"] == year:
            movieYearOfRealease.append(movie)
    return movieYearOfRealease

@app.post("/movies")
def create_movie(new_movie: dict = Body(...)):
    MOVIES.append(new_movie)
    return "Movie added"

@app.put("/movies/{ID}")
def update_movie(ID:int, new_movie: dict = Body(...)):
    for movie in MOVIES:
        if movie["ID"] == ID:
            MOVIES.remove(movie)
            MOVIES.append(new_movie)
    return "Movie updated"

@app.delete("/movies/{ID}")
def delete_movie(ID:int):
    for movie in MOVIES:
        if movie["ID"] == ID:
            MOVIES.remove(movie)
    return "Movie deleted"