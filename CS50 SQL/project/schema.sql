-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it

-- Create Artists table
CREATE TABLE Artists (
    id INTEGER,
    name TEXT NOT NULL,
    birth_day INTEGER,
    birth_month INTEGER,
    birth_year INTEGER,
    PRIMARY KEY (id)
);

-- Create Songs table
CREATE TABLE Songs (
    id INTEGER,
    name TEXT NOT NULL,
    released_year INTEGER,
    PRIMARY KEY (id)
);

-- Create Connections between Artist and Song
CREATE TABLE ArtistSong (
    artist_id INTEGER,
    song_id INTEGER,
    PRIMARY KEY (artist_id, song_id),
    FOREIGN KEY (artist_id) REFERENCES Artists(id),
    FOREIGN KEY (song_id) REFERENCES Songs(id)
);


-- Create View to See The name of the artist and the name of the song
CREATE VIEW "artistsandsongs" AS
SELECT artists.name, songs.name FROM artists
JOIN artistsong ON artistsong.artist_id = artists.id
JOIN songs ON artistsong.song_id = songs.id;
