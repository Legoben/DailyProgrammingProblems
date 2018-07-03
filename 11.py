# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

class AutoCompleter():
    def __init__(self):
        self.total_words = set()
        self.store = {}

    def add_word(self, word):
        store = self.store

        for char in word:
            if char not in store:
                store[char] = {}

            store = store[char]

    def narrow_words(self, prefix):
        if prefix == "":
            # ew
            words = set()
            self._gather_words("", self.store, words)
            return words

        store = self.store

        for char in prefix:
            if char not in store:
                return set()
            store = store[char]

        words = set()
        self._gather_words(prefix, store, words)
        return words

    def _gather_words(self, curword, store, words):
        for key in store:
            if store[key] == {}:
                words.add(curword + key)
                continue
            self._gather_words(curword + key, store[key], words)


if __name__ == "__main__":
    ac = AutoCompleter()
    [ac.add_word(x) for x in ["dog", "deer", "deal", "done"]]
    assert ac.narrow_words("de") == {'deer', 'deal'}
    assert ac.narrow_words("") == {"dog", "deer", "deal", "done"}
    assert ac.narrow_words("h") == set()