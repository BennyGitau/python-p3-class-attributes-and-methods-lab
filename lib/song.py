class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    def __init__(self,name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_artists(self.artist)
        self.add_to_genres(self.genre)
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_artists(cls, artist_name):
        if artist_name not in cls.artists:
            cls.artists.append(artist_name)

        return cls.artists
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        return cls.genres
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
        return cls.genre_count
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
        return cls.artist_count

        
        

    
