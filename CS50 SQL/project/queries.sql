-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database

INSERT INTO Artists (name, birth_day, birth_month, birth_year)
VALUES ('Lady Gaga', 28, 3, 1986);

INSERT INTO Artists (name, birth_day, birth_month, birth_year)
VALUES ('Justin Bieber', 1, 3, 1994);

INSERT INTO Songs (name, released_year)
VALUES ('One Time', '2010');

INSERT INTO Songs (name, released_year)
VALUES ('What Do You Mean', '2015');

INSERT INTO Songs (name, released_year)
VALUES ('Bad Romance', '2008');

INSERT INTO ArtistSong (artist_id, song_id)
VALUES (2,1);

INSERT INTO ArtistSong (artist_id, song_id)
VALUES (2,2);

INSERT INTO ArtistSong (artist_id, song_id)
VALUES (1,3);

SELECT artists.name, songs.name FROM artists
JOIN artistsong ON artistsong.artist_id = artists.id
JOIN songs ON artistsong.song_id = songs.id;
