from PIL import Image
from pathlib import Path


class ScaleZip:

    def __init__(self, filename, size):
        self.filename = filename
        self.size = size
        self.temp_directory = Path("unzipped-{}".format(filename[:-4]))

    def process_files(self):
        '''Scale each image in the directory to given size'''
        for filename in self.temp_directory.iterdir():
            if str(filename)[-3:] == 'jpg':
                im = Image.open(str(filename))
                scaled = im.resize(self.size)
                scaled.save(str(filename))
