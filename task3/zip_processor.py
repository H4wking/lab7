import shutil
import zipfile
from pathlib import Path


class ZipProcessor:
    def __init__(self, zipname, object):
        self.zipname = zipname
        self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))
        self.object = object

    def process_zip(self):
        self.unzip_files()
        self.object.process_files()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))
