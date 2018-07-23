class Node():
    def __init__(self):
        self.children = {}
        self.end = False

class WordFinder():
    def __init__(self, words):

        self.root = Node()

        for word in words:
            cur = self.root
            # add word

            for char in word:
                if char not in cur.children:
                    cur.children[char] = Node()
                cur = cur.children[char]

            cur.end = True

        print(self.root.children)

    def process_string(self, string):

        words = []

        cur = self.root
        cur_str = ""

        for char in string:
            if char not in cur.children:
                return None
            else:
                cur_str += char
                cur = cur.children[char]

            if cur.end:
                words.append(cur_str)
                cur = self.root
                cur_str = ""


        return words


if __name__ == "__main__":
    print(WordFinder(["quick", "brown", "the", "fox"]).process_string("thequickbrownfox"))
    print(WordFinder(["bed", "bedbath", "and", "beyond"]).process_string("bedbathandbeyond"))
