class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        """
        Move the cursor one position forward.
        """
        self.position += 1

    def back(self):
        """
        Move the cursor one position backwards.
        """
        self.position -= 1

    def home(self):
        """
        Move the cursor to the beginning of the document.
        """
        while self.document.characters[self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        """
        Move the cursor to the ending of the document.
        """
        while self.position < len(self.document.characters) and self.document.characters[self.position].character != '\n':
            self.position += 1
