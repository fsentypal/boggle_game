class BoggleWordlist():
    def __init__(self, filename="ospd.txt"):
        self.words = self.get_file_lines(filename)
        
    def get_file_lines(self,filename):
        file = open(filename, "r", encoding="utf-8")
        fileLines = file.readlines()
        lines = []
        for line in fileLines:
            lines.append(line.strip()) # str.strip() removes leading/trailing whitespace, such as '\n'
        file.close()
        return lines
