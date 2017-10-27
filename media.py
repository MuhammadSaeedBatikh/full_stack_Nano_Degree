class VisualMedia:
    """this class is a super class that holds common 
    fields/functionality of Movies, TVSeries or whatever to be added later and considered to
    be some sort of a Visual media"""

    def __init__(self, title, story_line, youtube_trailer_url,
                 poster_image_url, genre):
        self.title = title
        self.story_line = story_line
        self.youtube_trailer_url = youtube_trailer_url
        self.poster_image_url = poster_image_url
        self.genre = genre


class Movie(VisualMedia):
    """This is a Movie Class that contains some attributes specific to movies
     such as duration time, rating, etc.
     it also inherits VisualMedia 
     """
    RATINGS = ['G', 'PG', 'PG-13', 'R', 'UNRATED']

    def __init__(self, title, story_line, youtube_trailer_url, poster_image_url,
                 release_date, genre, duration_time, rating=RATINGS[3]):
        """instantiate a Movie object with these attributes: title, story_line, youtube_trailer_url, poster_image_url,
                 release_date, genre, duration_time, rating"""

        VisualMedia.__init__(self, title, story_line, youtube_trailer_url, poster_image_url, genre)
        self.release_date = release_date
        self.duration_time = duration_time
        self.rating = rating


class TVSeries(VisualMedia):
    """ This is a TVSeries Class that contains some attributes specific to TV Series
        such as running date , number of seasons, etc.
        it also inherits VisualMedia 
        """
    RATINGS = ['TV-Y', 'TV-Y7', 'TV-G', 'TV-PG', 'TV-14', 'TV-MA']

    def __init__(self, title, story_line, youtube_trailer_url, poster_image_url,
                 running_date, genre, seasons_number, rating=RATINGS[4]):
        """instantiate a Movie object with these attributes: title, story_line, youtube_trailer_url, poster_image_url,
                 running_date, genre, seasons_number, rating"""

        VisualMedia.__init__(self, title, story_line, youtube_trailer_url, poster_image_url, genre)

        self.running_date = running_date
        self.seasons_number = seasons_number
        self.rating = rating