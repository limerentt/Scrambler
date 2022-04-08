from sys import stdin


class InfoManager:
    """Read and write into files or console"""
    def __init__(self, _in, _out):
        self.input = _in
        self.output = _out
        self.text = []

    def read_text(self):
        """read from input"""
        if self.input is None:
            while True:
                line = stdin.readline()
                if line.strip() == "":
                    break
                line = line.replace('\n', '')
                self.text.append(line)
        else:
            with open(self.input, "r") as file:
                self.text = [line.replace('\n', '') for line in file.readlines()]
                file.close()

    def write_text(self):
        """write in output"""
        if self.output is None:
            for line in self.text:
                print(line)
        else:
            with open(self.output, "w") as file:
                for line in self.text:
                    file.write(line + "\n")
                file.close()


class Encryptor(object):
    @staticmethod
    def encode_symbol(symbol, key):
        """Encode the symbol by the key symbol from ascii"""
        return chr((ord(symbol) + ord(key) - 64) % (127 - 32) + 32)

    @staticmethod
    def decode_symbol(symbol, key):
        """Decode the symbol by the key symbol from ascii"""
        return chr((ord(symbol) - ord(key)) % (127 - 32) + 32)

    @staticmethod
    def encode_word_caesar(word, key):
        """Encode the word by the key number"""
        code = ""
        for symbol in word:
            code += Encryptor.encode_symbol(symbol, chr(int(key) + 32))
        return code

    @staticmethod
    def encode_word_vigenere(word, key):
        """Encode the word by the key word"""
        code = ""
        it = 0
        for symbol in word:
            it = it + 1 if it < len(key) - 1 else 0
            code += Encryptor.encode_symbol(symbol, key[it])
        return code

    @staticmethod
    def decode_word_caesar(word, key):
        """Decode the word by the key number"""
        code = ""
        for symbol in word:
            code += Encryptor.decode_symbol(symbol, chr(int(key) + 32))
        return code

    @staticmethod
    def decode_word_vigenere(word, key):
        """Decode the word by the key word"""
        code = ""
        it = 0
        for symbol in word:
            it = it + 1 if it < len(key) - 1 else 0
            code += Encryptor.decode_symbol(symbol, key[it])
        return code
