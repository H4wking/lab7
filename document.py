class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor]

    def save(self):
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

    def forward(self):
        self.cursor += 1

    def back(self):
        self.cursor -= 1

    @property
    def string(self):
        return "".join(self.characters)


class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[
                self.position-1] != '\n':
            self.position -= 1
            if self.position == 0:
                   # Got to beginning of file before newline
                break

    def end(self):
        while self.position < len(self.document.characters
             ) and self.document.characters[self.position] != '\n':
            self.position += 1


class Character:
    def __init__(self, character,
                 bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character

    def insert(self, character):
        if not hasattr(character, 'character'):
            character = Character(character)

    @property
    def string(self):
        return "".join((str(c) for c in self.characters))

    def home(self):
        while self.document.characters[self.position - 1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        while self.position < len(
                self.document.characters) and \
                self.document.characters[
                    self.position
                ].character != '\n':
            self.position += 1


if __name__ == "__main__":
    doc = Document()
    doc.filename = "test_document"
    doc.insert('h')
    doc.insert('e')
    doc.insert('l')
    doc.insert('l')
    doc.insert('\n')
    doc.cursor.home()
    doc.insert('O')
    print(doc.string)
