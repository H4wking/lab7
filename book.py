class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current = 1
        self.bookmark = None

    def __str__(self):
        if self.pages == 1:
            return "Book<{} by {}: {} page, currently on page {}>".format(self.title, self.author, self.pages,
                                                                           self.current)
        if self.bookmark:
            return "Book<{} by {}: {} pages, currently on page {}, page {} bookmarked>".format(self.title,
                                                                                                self.author,
                                                                                                self.pages,
                                                                                                self.current,
                                                                                                self.bookmark)
        else:
            return "Book<{} by {}: {} pages, currently on page {}>".format(self.title, self.author, self.pages,
                                                                           self.current)

    def turnPage(self, pages):
        self.current += pages
        if self.current < 1:
            self.current = 1
        if self.current > self.pages:
            self.current = self.pages

    def getCurrentPage(self):
        return self.current

    def placeBookmark(self):
        self.bookmark = self.current

    def getBookmarkedPage(self):
        return self.bookmark

    def removeBookmark(self):
        self.bookmark = None

    def turnToBookmark(self):
        if self.bookmark:
            self.current = self.bookmark

    def __eq__(self, other):
        if isinstance(self, Book):
            return self.title == other.title and self.author == other.author and self.pages == other.pages and\
                   self.current == other.current and self.bookmark == other.bookmark
        return False
