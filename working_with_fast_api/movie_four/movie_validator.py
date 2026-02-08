from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel, Field, validator
from datetime import datetime, date

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

class Movie(BaseModel):
    ID: int = Field(None, ge=1)
    MovieName: str = Field(..., min_length=1, max_length=100)
    Genre: str = Field(..., min_length=1, max_length=100)
    YearOfRelease: int = Field(..., ge=1800)
    Budget: int = Field(..., ge=0)
    Revenue: int = Field(..., ge=0)
    DirectorName: str = Field(..., min_length=1, max_length=100)

    @validator("YearOfRelease")
    def validate_year_of_release(cls, value):
        current_year = datetime.now().year
        if value > current_year:
            raise ValueError ("Year of release cannot be greater than current year")
        return value


@app.get("/movies")
def get_all_movies():
    return MOVIES

@app.post("/movies")
def create_movie(new_movie: Movie):
    movie_data = new_movie.dict()
    MOVIES.append(movie_data)
    return "Movie added"

@app.get("/movies/{movie_id}")
async def get_movie(movie_id: int = Path(..., ge=0)):
    movieByID=None
    for movie in MOVIES:
        if movie["ID"] == movie_id:
            movieByID = movie
            break
    return movieByID

@app.get("/moviesgenres")
async def get_movie_genres(genre:str = Query(..., min_length=3, max_length=40)):
    movieGenresByID=[]
    for movie in MOVIES:
        if movie["Genre"].lower() == genre.lower():
            movieGenresByID.append(movie)

    return movieGenresByID