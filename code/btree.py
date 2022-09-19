from collections import defaultdict

head = defaultdict()


def add(word, head):
    cur = head
    for ch in word:
        if ch not in cur:
            cur[ch] = {}
        cur = cur[ch]
    cur['_end'] = word


def add_list(words):
    for w in words:
        add(w, head)
    return


def delete(word, head):
    cur = head
    for letter in word:
        cur = cur[letter]
    del cur['_end']


def find_letter(letter, cur):
    list_d = []

    def search_(sym, dict_list):
        second_list = []
        for child in dict_list:
            keys = child.keys()
            for key in keys:
                if key == sym:
                    list_d.append(child[key])
                elif key == '_end':
                    continue
                else:
                    second_list.append(child[key])

        if len(second_list) > 0:
            search_(letter, second_list)

    for d in cur:
        search_(letter, [d])
    return list_d


def get_keys(list_dict):
    keys = []
    for every_dictionary in list_dict:
        keys += every_dictionary.keys()
    return keys


def tree_search(word, trie):
    cur = []
    middle = []
    cur.append(trie)
    last = len(word) - 1
    sym_index = 0
    for i, letter in enumerate(word):
        keys = get_keys(cur)
        if sym_index > last:
            return 1, cur
        letter = word[sym_index]
        if letter == '?':
            for d in cur:
                keys = d.keys()
                for key in keys:
                    if key != '_end':
                        middle.append(d[key])
            sym_index += 1
        elif letter == '*':
            if sym_index == last:
                middle = cur
            else:
                while sym_index <= last:
                    sym_index += 1
                    if word[sym_index] != '*' and word[sym_index] != '?':
                        middle = find_letter(word[sym_index], cur)
                        sym_index += 1
                        break
                    else:
                        sym_index += 1
        elif letter not in keys:
            return 2, f"\n2 File not found index = ({i}) : sym : '{letter}'\n {cur}"
        else:
            for d in cur:
                keys = d.keys()
                if letter in keys:
                    middle.append(d[letter])
            sym_index += 1
        cur = middle
        middle = []
    return 3, cur


def search(word, trie):
    answer_code, list_dict = tree_search(word, trie)

    if answer_code == 2:
        exit('\nFile not found: \n')

    names_list = []

    def get_names(dict_list):
        second_list = []
        for d in dict_list:
            keys = d.keys()
            for key in keys:
                if key == '_end':
                    names_list.append(d['_end'])
                else:
                    second_list.append(d[key])

        if len(second_list) > 0:
            get_names(second_list)

    get_names(list_dict)
    return names_list
