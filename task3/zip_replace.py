from pathlib import Path


class ZipReplace:
    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.temp_directory = Path("unzipped-{}".format(filename[:-4]))
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        for filename in self.temp_directory.iterdir():
            if str(filename)[-3:] == 'txt':
                with filename.open() as file:
                    contents = file.read()
                contents = contents.replace(self.search_string, self.replace_string)
                with filename.open("w") as file:
                    file.write(contents)


# if __name__ == "__main__":
#     ZipReplace(*sys.argv[1:4]).process_zip()
