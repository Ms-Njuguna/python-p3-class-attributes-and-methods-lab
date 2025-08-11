class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        Song.artists.append(artist)
        self.genre = genre
        Song.genres.append(genre)
        self.add_song_to_count()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls, increament = 1):
        cls.count += increament

    @classmethod
    def add_to_genres(cls):
        cls.genres = list(dict.fromkeys(cls.genres))

    @classmethod
    def add_to_artists(cls):
        cls.artists = list(dict.fromkeys(cls.artists))

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count[cls.genres[-1]] = cls.genre_count.get(cls.genres[-1], 0) + 1

    @classmethod
    def add_to_artist_count(cls):
        cls.artist_count[cls.artists[-1]] = cls.artist_count.get(cls.artists[-1], 0) + 1