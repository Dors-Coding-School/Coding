#upper_movie('The Lord of the Rings') -> 'THE LORD OF THE RINGS'

#upper_movie('star wars') -> 'STAR WARS'

def upper_movie(movie: str)->str:
    final = movie.upper()
    return final

print(upper_movie("star wars"))
print(upper_movie("scream"))