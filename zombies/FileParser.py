import re


class ZombieParser:

    def __init__(self, file_name):
        self.__result = []
        self.parse_file(file_name)

    def add_to_array(self, char):
        self.__result.append(char)

    def increment_last_positiom(self, incremend_by):
        c = self.__result[-1]
        self.__result[-1] = chr(ord(c) + incremend_by)

    def parse_line(self, content):
        if content.startswith("kill zombie ->"):
            m = re.search("->\W?(\w)", content)
            c = m.groups()[0]
            self.add_to_array(c)
        if content.startswith("clean chainsaw"):
            self.increment_last_positiom(-3)
        if content.startswith("grab brain"):
            self.increment_last_positiom(2)

    def parse_file(self, file_name):
        txt_file = open(file_name)
        for line in txt_file:
            self.parse_line(line)

    def get_string(self):
        return ''.join(self.__result)


if __name__ == '__main__':
    assert ZombieParser('sample.txt').get_string() == 'Brain'
    print(ZombieParser('input.txt').get_string())
