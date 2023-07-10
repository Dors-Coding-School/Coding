#title_movie('the lord of the rings') -> 'The Lord Of The Rings'

#title_movie('star wars') -> 'Star Wars'

def title_movie(movie: str)-> str:
    upper = movie.title()
    return upper

print(title_movie("star wars"))
print(title_movie("scream"))