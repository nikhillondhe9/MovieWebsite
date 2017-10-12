import webbrowser


class Movie(object):

    """The class Movie returns the instance variables
    with values passed in the function call"""
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """This is the __init__ method which calls
        the constructor to create instance variables"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def play_trailer(self):
        """play_trailer() method opens the movie trailer video,
        It takes exactly one parameter i.e the Youtube URL for the video"""
        webbrowser.open(self.trailer_youtube_url)
