from encryptor import Encryptor

class CaesarCipher:
    english_frequencies = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
                           0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                           0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                           0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    @classmethod
    def shifted_forward_text(cls, shift, text):
        result = ""
        for symbol in text:
            if symbol.isalpha():
                if symbol.isupper():
                    result += chr((ord(symbol) + shift - 65) % 26 + 65)
                else:
                    result += chr((ord(symbol) + shift - 97) % 26 + 97)
            else:
                result += symbol
        return result

    @classmethod
    def shifted_backwards_text(cls, shift, text):
        decoded = ''
        for key in range(len(cls.alphabet)):
            decoded = ''
            for symbol in text:
                if symbol.isalpha:
                    num = cls.alphabet.find(symbol)
                    num = num - key
                    num %= 26
                    decoded = decoded + cls.alphabet[num]
                else:
                    decoded = decoded + symbol
        return decoded

    @classmethod
    def decode(cls, arguments):
        return CaesarCipher.shifted_backwards_text(arguments['key'], arguments['input_text'])

    @classmethod
    def encode(cls, arguments):
        return CaesarCipher.shifted_forward_text(arguments['key'], arguments['input_text'])

    @classmethod
    def get_frequencies(cls, text):
        dict = {}
        for alpha in cls.alphabet:
            dict[alpha.lower()] = 0
        for alpha in text:
            if alpha.isalpha():
                dict[alpha.lower()] += 1
        if len(text) != 0:
            for value in dict.values():
                value /= len(text)
        return dict

    @classmethod
    def error_function(cls, frequencies):
        sum_of_diff = 0
        for i in range(len(cls.alphabet)):
            sum_of_diff += (frequencies[cls.alphabet[i]] - cls.english_frequencies[i])**2
        sum_of_diff /= len(cls.alphabet)
        return sum_of_diff**0.5
    
    @classmethod
    def hack(cls, arguments):
        best_shift = 0
        shifted_text = cls.shifted_forward_text(0, arguments)
        frequencies = cls.get_frequencies(shifted_text)
        best_error = cls.error_function(frequencies)
        for shift in range(-26, 26):
            shifted_text = cls.shifted_forward_text(shift, arguments)
            frequencies = cls.get_frequencies(shifted_text)
            error = cls.error_function(frequencies)
            if best_error > error:
                best_error = error
                best_shift = shift
        return cls.shifted_forward_text(best_shift, arguments)
