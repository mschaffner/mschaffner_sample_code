'''
Problem source: https://leetcode.com/problems/text-justification/

Description:
Given an array of words and a length L, format the text such that each line
has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words
as you can in each line. Pad extra spaces ' ' when necessary so that each line
has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the
number of spaces on a line do not divide evenly between words, the empty slots
on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is
inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Note: Each word is guaranteed not to exceed L in length.
'''
def full_justification(words, length):
    def inflate_line(queued_words, is_last_line):
        # Two cases that a line can end in whitespace, last line and single word line:
        if is_last_line or len(queued_words) == 1:
            base = " ".join(queued_words)
            return base + " "*(length - len(base))

        # Determine how many spaces to pad in between words
        gaps = len(queued_words) - 1
        spaces_needed = length - sum(map(len, queued_words))
        space_per = spaces_needed / gaps
        remainder = spaces_needed % gaps

        sentence_list = []
        for i, word in enumerate(queued_words):
            sentence_list.append(word)

            if i < gaps:
                spaces = space_per + 1 if i < remainder else space_per
                sentence_list.append(" "*(spaces))

        return "".join(sentence_list)  # Fast string concatenation

    if any(len(word) > length for word in words):
        raise ValueError("Must not provide words longer than length")

    num_words = len(words)
    sentences = []
    word_queue = []
    queue_len = 0

    for i, word in enumerate(words):
        # Need to account for space before this word in sentence if not the first word
        word_len = len(word) if i != 0 else len(word) + 1
        if queue_len + word_len <= length:
            queue_len += word_len
            word_queue.append(word)
        else:
            sentences.append(inflate_line(word_queue, False))

            word_queue = [word]
            queue_len = word_len
            last_line = num_words - 1 == i
            if last_line:
                sentences.append(inflate_line(word_queue, last_line))

    return sentences

import re
r_one_word = re.compile(r"^\S*\s*$$")
r_justified = re.compile(r"^\S.*\S$")
def test_full_justification():
    def verify_output(lines, length):
        def _verify(ln):
            is_correct_length = len(ln) == length
            is_justified = r_one_word.search(ln) or r_justified.search(ln)
            return is_justified and is_correct_length

        msg = "All lines must be of length l={} and full justified".format(length)
        assert all(map(_verify, lines)), msg

    # Small test
    small_test = ["This", "is", "an", "example", "of", "text", "justification."]
    small_test_lengths = [15, 16, 17, 18]
    for l in small_test_lengths:
        verify_output(full_justification(small_test, l), l)

    # Medium test
    medium_test = [
        'Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the',
        'printing', 'and', 'typesetting', 'industry.', 'Lorem', 'Ipsum',
        'has', 'been', 'the', "industry's", 'standard', 'dummy', 'text',
        'ever', 'since', 'the', '1500s,', 'when', 'an', 'unknown',
        'printer', 'took', 'a', 'galley', 'of', 'type', 'and', 'scrambled',
        'it', 'to', 'make', 'a', 'type', 'specimen', 'book.', 'It', 'has',
        'survived', 'not', 'only', 'five', 'centuries,', 'but', 'also',
        'the', 'leap', 'into', 'electronic', 'typesetting,', 'remaining',
        'essentially', 'unchanged.', 'It', 'was', 'popularised', 'in',
        'the', '1960s', 'with', 'the', 'release', 'of', 'Letraset',
        'sheets', 'containing', 'Lorem', 'Ipsum', 'passages,', 'and',
        'more', 'recently', 'with', 'desktop', 'publishing', 'software',
        'like', 'Aldus', 'PageMaker', 'including', 'versions', 'of',
        'Lorem', 'Ipsum.'
    ]
    medium_test_lengths = [20, 40, 60, 80]
    for l in medium_test_lengths:
        verify_output(full_justification(medium_test, l), l)

    long_test = [
        'Lorem', 'ipsum', 'dolor', 'sit', 'amet,',
        'consectetur', 'adipiscing', 'elit.', 'Nullam', 'porttitor', 'leo',
        'at', 'leo', 'sollicitudin,', 'sed', 'sollicitudin', 'urna',
        'pharetra.', 'Maecenas', 'nec', 'dapibus', 'turpis.', 'Curabitur',
        'dictum', 'porta', 'elementum.', 'Vivamus', 'consequat', 'tempus',
        'pretium.', 'Integer', 'venenatis', 'urna', 'placerat', 'interdum',
        'lacinia.', 'Nam', 'gravida', 'maximus', 'orci,', 'sit', 'amet',
        'luctus', 'sapien', 'convallis', 'facilisis.', 'Curabitur', 'eget',
        'magna', 'eget', 'mi', 'ultricies', 'vestibulum', 'tristique',
        'et', 'leo.', 'Vivamus', 'dignissim', 'ipsum', 'metus,', 'non',
        'posuere', 'massa', 'cursus', 'a.', 'Duis', 'efficitur', 'quis',
        'ex', 'nec', 'lobortis.', 'Nullam', 'blandit', 'enim', 'aliquet',
        'ligula', 'pellentesque', 'volutpat.', 'Sed', 'mollis', 'turpis',
        'mi,', 'non', 'viverra', 'urna', 'aliquet', 'in.', 'Fusce', 'sed',
        'sem', 'nunc.', 'Duis', 'ut', 'velit', 'eu', 'nisi', 'mollis',
        'tincidunt', 'quis', 'vitae', 'neque.', 'In', 'vitae', 'turpis',
        'enim.', 'Nulla', 'tincidunt', 'faucibus', 'libero', 'a',
        'feugiat.', 'Integer', 'ex', 'ipsum,', 'gravida', 'quis', 'ligula',
        'nec,', 'pharetra', 'tristique', 'enim.', 'Sed', 'condimentum',
        'vulputate', 'purus.', 'Nam', 'at', 'tincidunt', 'ligula,', 'et',
        'pellentesque', 'quam.', 'Praesent', 'nec', 'velit', 'ornare,',
        'interdum', 'nulla', 'nec,', 'sollicitudin', 'risus.', 'Sed',
        'semper', 'dolor', 'at', 'convallis', 'fermentum.', 'Quisque',
        'lectus', 'urna,', 'consectetur', 'vel', 'purus', 'et,', 'aliquet',
        'fringilla', 'risus.', 'Mauris', 'eu', 'sodales', 'augue.', 'Duis',
        'mattis', 'nibh', 'ut', 'urna', 'pharetra', 'congue.', 'Cras',
        'vitae', 'aliquam', 'orci.', 'Fusce', 'molestie', 'nisl', 'in',
        'leo', 'cursus', 'tempor.', 'Curabitur', 'iaculis', 'lorem',
        'malesuada', 'nisl', 'fermentum', 'dignissim', 'eu', 'et',
        'lacus.', 'Sed', 'consectetur', 'diam', 'id', 'purus', 'rutrum,',
        'ut', 'molestie', 'mauris', 'consequat.', 'Mauris', 'rhoncus',
        'est', 'id', 'massa', 'rhoncus', 'tempus.', 'Phasellus', 'at',
        'rutrum', 'metus,', 'id', 'fringilla', 'lorem.', 'Fusce',
        'placerat', 'congue', 'ullamcorper.', 'Etiam', 'dapibus',
        'malesuada', 'dui.', 'Donec', 'vitae', 'augue', 'nisl.', 'Proin',
        'vitae', 'consectetur', 'neque.', 'Donec', 'cursus', 'varius',
        'placerat.', 'Donec', 'sodales,', 'ligula', 'sed', 'fermentum',
        'dignissim,', 'tortor', 'augue', 'interdum', 'lorem,', 'id',
        'auctor', 'risus', 'odio', 'sed', 'turpis.', 'Duis', 'efficitur',
        'lectus', 'quis', 'fermentum', 'tristique.', 'Vivamus', 'ornare',
        'enim', 'lacus,', 'ut', 'porttitor', 'metus', 'ultricies', 'ut.',
        'Fusce', 'varius,', 'mauris', 'ut', 'congue', 'lobortis,', 'arcu',
        'velit', 'blandit', 'lorem,', 'vel', 'bibendum', 'lacus', 'quam',
        'et', 'felis.', 'Praesent', 'varius,', 'ligula', 'id', 'imperdiet',
        'iaculis,', 'leo', 'magna', 'vehicula', 'massa,', 'non',
        'placerat', 'leo', 'nisl', 'vitae', 'sapien.', 'Cras', 'eget',
        'nunc', 'magna.', 'Proin', 'id', 'eros', 'sollicitudin', 'diam',
        'condimentum', 'blandit.', 'Etiam', 'cursus', 'nisl', 'sed',
        'sapien', 'tempus', 'fringilla.', 'Interdum', 'et', 'malesuada',
        'fames', 'ac', 'ante', 'ipsum', 'primis', 'in', 'faucibus.',
        'Pellentesque', 'porttitor', 'bibendum', 'libero', 'facilisis',
        'rhoncus.', 'Sed', 'pulvinar', 'nunc', 'nec', 'risus', 'lacinia',
        'finibus.', 'Suspendisse', 'volutpat,', 'sapien', 'in', 'porta',
        'egestas,', 'lectus', 'nisl', 'suscipit', 'neque,', 'non', 'interdum',
        'ligula', 'lorem', 'at', 'eros.', 'Curabitur', 'interdum', 'leo', 'id',
        'nibh', 'pulvinar', 'efficitur.', 'Nullam', 'vel', 'leo', 'non', 'ligula',
        'iaculis', 'faucibus', 'eget', 'vitae', 'neque.', 'Pellentesque', 'nec',
        'maximus', 'metus,', 'in', 'ultrices', 'libero.', 'Pellentesque',
        'habitant', 'morbi', 'tristique', 'senectus', 'et', 'netus', 'et',
        'malesuada', 'fames', 'ac', 'turpis', 'egestas.', 'Phasellus', 'tempor',
        'sollicitudin', 'lobortis.', 'Praesent', 'varius', 'fermentum', 'quam',
        'quis', 'facilisis.', 'Aenean', 'ipsum', 'lectus,', 'tristique', 'nec',
        'lobortis', 'sed,', 'facilisis', 'et', 'justo.', 'Ut', 'a', 'ante',
        'pulvinar,', 'tempus', 'nulla', 'auctor,', 'faucibus', 'lectus.',
        'Vivamus', 'porttitor', 'viverra', 'dui,', 'vitae', 'efficitur', 'quam',
        'varius', 'quis.', 'Donec', 'ultricies', 'eu', 'quam', 'id', 'tincidunt.',
        'Duis', 'eu', 'vulputate', 'lectus.', 'Ut', 'in', 'arcu', 'lacinia,',
        'consequat', 'tortor', 'in,', 'malesuada', 'elit.', 'Cras', 'tellus',
        'lacus,', 'condimentum', 'nec', 'convallis', 'suscipit,', 'auctor', 'nec',
        'leo.', 'Aliquam', 'erat', 'volutpat.', 'Ut', 'ut', 'dapibus', 'nulla,',
        'sed', 'vulputate', 'ex.', 'In', 'malesuada', 'risus', 'orci,', 'dapibus',
        'congue', 'massa', 'porttitor', 'nec.', 'Ut', 'posuere', 'ipsum', 'quis',
        'magna', 'hendrerit', 'vestibulum.', 'Nam', 'ac', 'aliquet', 'enim.',
        'Integer', 'eu', 'auctor', 'lectus.', 'Lorem', 'ipsum', 'dolor', 'sit',
        'amet,', 'consectetur', 'adipiscing', 'elit.', 'Class.'
    ]
    long_test_lengths = [40, 80, 120, 160]

    for l in long_test_lengths:
        verify_output(full_justification(long_test, l), l)
    print "All tests passed :)"

if __name__ == "__main__":
    test_full_justification()

