from task4.cursor import Cursor
from task4.document import Document
from task4.character import Character
d = Document()
d.insert('h')
d.insert('e')
d.insert(Character('l', bold=True))
d.insert(Character('l', bold=True))
d.insert('o')
d.insert('\n')
d.insert(Character('w', italic=True))
d.insert(Character('o', italic=True))
d.insert(Character('r', underline=True))
d.insert('l')
d.insert('d')
print(d.string)
d.cursor.home()
d.delete()
d.insert('W')
print(d.string)
d.characters[0].underline = True
print(d.string)
print(d.cursor.position)
for i in range(50):
    d.cursor.forward()
print(d.cursor.position)
a = "A"
d.insert(a)
print(d.string)
print(d.string)
# d.insert("ab")
print(d.string)
print(d.string)
d.save()
