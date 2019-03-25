from task4.cursor import Cursor
from task4.character import Character


class Document:
    """
    Class for documnents' handling.
    """

    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        """
        Insert character into current position. If current position is beyond the beginning/ending of a document,
        character will be inserted into the end of the document. Raises error if more than 1 characters are given.
        """
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.position += 1

    def delete(self):
        """
        Delete the character in the current position. Raises error if there is no character.
        """
        del self.characters[self.cursor.position]

    def save(self):
        """
        Save the document in file with given name. Raises error if there is no such a file.
        """
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

    @property
    def string(self):
        return "".join((str(c) for c in self.characters))
