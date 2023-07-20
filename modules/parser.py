#  guild: https://discord.gg/python
#  idea: https://discord.com/channels/267624335836053506/470884583684964352/1098351969468428338


class LetterParser:
    def __init__(self):
        self.table = {
            "q": "str(quit)[-~-~-~-~int()]",
            "w": "str(pow)[-~-~-~-~-~(-~int() << int('100', int('10', 2)))]",
            "e": "str(bool())[~int()]",
            "r": "str(round)[-~-~-~(-~int() << 4)]",
            "t": "str(pow)[-~(-~int() << int('10', int('10', 2)))]",
            "y": "str(bytes)[-~(-~int() << int('11', 2))]",
            "u": "str(quit)[-~-~-~-~-~int()]",
            "i": "str(quit)[-~-~-~-~-~-~int()]",
            "o": "str(ord)[-~int() << int('100', 2)]",
            "p": "str(pow)[-~-~-~(-~int() << int('100', int('10', 2)))]",
            "a": "str(float)[-~-~-~int()]",
            "s": "str(bytes)[-~int() << int('10', int('10', 2))]",
            "d": "str(dict)[~-~-~-~-~-~int()]",
            "f": "str(float)[-~-~-~-~-~-~-~-~int()]",
            "g": "str(globals)[-~-~-~(-~int() << 4)]",
            "h": "str(hex)[-~-~-~(-~int() << int('100', 2))]",
            "j": "str(object)[(-~int() << int('11', 2)) + int('10', int('10', 2))]",
            "k": "str(breakpoint)[((-~int() << int('100', 2)) + ((-~int() << int('10', 2)) << int('1', 2))) - int("
                 "'1', 2)]",
            "l": "str(float)[-~-~int()]",
            "z": "str(zip)[-~int() << int('11', 2)]",
            "x": "str(hex)[-~-~-~(-~int() << int('100', 2))]",
            "c": "str(str)[-~int()]",
            "v": "str(eval)[-~-~-~(-~int() << int('100', 2))]",
            "b": "str(bytes)[-~int() << int('11', 2)]",
            "n": "str(bin)[-~int() << 3]",
            "m": "str(map)[-~int() << int('11', 2)]",
            " ": "str(bytes)[-~-~(-~int() << 2)]"
        }

    def parse_sentence(self, sentence: str):
        sentence = self.clear_text(sentence=sentence)
        code = []

        for letter in sentence:
            code.append("({code_snipper})".format(code_snipper=self.table[letter]))

        value = code[0]
        for item in code[1:]:
            value += f".__add__({item})"

        return value

    def clear_text(self, sentence: str) -> str:
        return "".join(letter for letter in sentence.lower() if letter in self.table.keys())


if __name__ == "__main__":
    parser = LetterParser()
    print(parser.parse_sentence("hello my dear world"))
