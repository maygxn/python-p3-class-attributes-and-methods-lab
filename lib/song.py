class Song:
    # class attribute initialize
    count = 0
    genres = []
    artists = []
    # initialize empty dictionary keep count of Songs for genre/artist
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        # need to add song to count
        self.add_song_to_count()
        # need to add genre to genres / pass genre
        self.add_to_genres(genre)
        # need to add artist to artists / pass artist
        self.add_to_artists(artist)
        # need to add genre/artist to count
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        # need to increment when new song is made
        cls.count += 1
        
    @classmethod
    def add_to_genres(cls, genre):
        # need to add genre to genres
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # need to add artist to artists
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # if/else statement to add genre to count or increment if have already
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
        
    @classmethod
    def add_to_artist_count(cls, artist):
        # if/else statement to add artist to count or increment if have already
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1