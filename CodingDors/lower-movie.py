#lower_movie('The Lord of the Rings') -> 'the lord of the rings'

#lower_movie('STAR WARS') -> 'star wars'

def lower_movie(movie: str)->str:
    result = movie.lower()
    return result

print(lower_movie("STaR wARS"))
print(lower_movie("SCREAM"))
print(lower_movie("THE LORD OF THE RINGS"))