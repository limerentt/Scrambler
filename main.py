import sys
import argparse
from encryptor import Encryptor, InfoManager
from caesar_hacker import CaesarCipher


# def create_parser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('command')
#     parser.add_argument('--cipher', default="caesar")
#     parser.add_argument('--key', default="1")
#     parser.add_argument('--input_file', default=None)
#     parser.add_argument('--output_file', default=None)
#     return parser

class Parser:
    parser = argparse.ArgumentParser()

    def __init__(self):
        self.modulename = sys.argv[1:]
        self.parser.add_argument('module')
        self.parser.add_argument('--cipher', default="caesar")
        self.parser.add_argument('--key', default="1")
        self.parser.add_argument('--input_file', default=None)
        self.parser.add_argument('--output_file', default=None)

    def get_arguments(self):
        args = vars(self.parser.parse_args())
        args['input_text'] = input() if args['input_file'] is None else args['input_file'].read()
        return args


if __name__ == "__main__":
    parser = Parser()
    namespace = parser.parser.parse_args()
    manager = InfoManager(namespace.input_file, namespace.output_file)
    manager.read_text()

    if namespace.module == "encode":
        if namespace.cipher == "caesar":
            manager.text = [Encryptor.encode_word_caesar(line, namespace.key) for line in manager.text]
        elif namespace.cipher == "vigenere":
            manager.text = [Encryptor.encode_word_vigenere(line, namespace.key) for line in manager.text]
    elif namespace.module == "decode":
        if namespace.cipher == "caesar":
            manager.text = [Encryptor.decode_word_caesar(line, namespace.key) for line in manager.text]
        elif namespace.cipher == "vigenere":
            manager.text = [Encryptor.decode_word_vigenere(line, namespace.key) for line in manager.text]
    elif namespace.module == "hack":
        manager.text = [CaesarCipher.hack(line) for line in manager.text]

    manager.write_text()
