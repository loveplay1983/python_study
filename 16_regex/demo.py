"""
If you want to use regular expressions in Python, you have to import the re module, which provides methods and functions to deal with regular expressions.
"""

"""
From other languages you might be used to represent regular expressions within Slashes "/", e.g. that's the way Perl, SED or AWK deals with them. In Python there is no special notation. Regular expressions are represented as normal strings.

I notice javascript has the '/' syntax for `regex`
"""

# Notice there are "over matching" and "under matching"    - :) similar to "over-fitting" and "under-fitting" in
# Deep learning field which is I am getting involved, just a joke for comparing these two things...

# OK, so "over matching" - You want to data set `A` and `A` is a subset of `B`, so we often get wrong matched i
# pattern which is data set `B`.  e.g. we want `cat`, but we encoutering `education, ramification...`
# "under matching"- Your matched data set is `A` and your searching `pattern` is missing of the content that
# actually match the desired result. e.g. we want `  cat  `, but we encoutering ` cat`

# simple syntax
"""
re.search(expr,s)
If a match has been possible, we get a so-called match object as a result, otherwise the value will be None.
"""
import re
x = re.search('cat', 'A cat and a rat can\'t be friends.')
print(x)
y = re.search('cow', 'A cat and a rat can\'t be friends.')
print(y)

"""
If a regular expression matches, we get an SRE object returned, which is taken as a True value, and None,
which is the return value if it doesn't match, is taken as False.
"""
if re.search('cat', 'A cat and a rat cannot be friends.'):
    print('rat friendly cat has been found.')
else:
    print('cat always eat rats without any hesitation.')

if re.search('cow', 'A cat and a rat cannot be friends.'):
    print('cow, cat and rat will become friends.')
else:
    print('No cow around.')


# Any character  "."

# Character classes  [xyz]
r'M[ae][iy]er'
# Using middle content omission for readable search pattern. e.g. A to Z [A-Z]
# Notice that "-" symbol will be used to omit the middle content <=> "-" is positioned right in the middle
# [-abc] or [abc-] only stands for different options for seach pattern. e.g. "-, a, b, c" or "a, b, c, -"
"""
What character class is described by [-a-z]?
Answer The character "-" and all the characters "a", "b", "c" all the way up to "z".
"""

# "^" in `[]`
# [^abc] means anything but an "a", "b" or "c", i.e. the result will match anything beside "a, b, c"
# [a^bc] means an "a", "b", "c" or a "^"

#############################################################################################################
# A practical exercise
if False:
    print('A practical exercise')
    import re
    phone_book = open('phone.book')
    for line in phone_book:
        if re.search(r'J.*Neu*', line):
            print(line.rstrip())
    phone_book.close()

# It is also possible to use url directly instead of the local text file
import re

#from urllib.request import urlopen
#with urlopen('https://www.python-course.eu/simpsons_phone_book.txt') as phone_book:
#    for line in phone_book:
#        # line is a byte string so it needs to be transormed as utf-8
#        # [why line is a byte string??? Because they were transmitted through network which uses binary or byte data format]
#        line = line.decode('UTF-8').rstrip()
#        if re.search(r'J.*Neu*', line):
#            print(line)
# encoding example
#print(b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'.decode('utf-16'))
#print('τoρνoς'.encode('utf-8'))

# Predefined character classes
"""
\d any decimal digit [0-9]
\D complement of \d, i.e. the opposite data set of \d
\s any whitespace character [\t\n\r\f\v]
\S complement of \s
\w any alphanumeric character [0-9A-Za-z_]
\W complement of \w
\b empty strings, only at the start or end of a word
\B empty strings, but not at the start or end of a word
\\ matches a literal backslash
"""

# Matching beginning and end    -  `^` and `$`
import re
s1 = 'Mayer is a very common Name'
s2 = 'He is called Meyer but he is not German'

print(re.search(r'^M[ae][iy]er',s1))
print(re.search(r'^M[ae][iy]er',s2))

s = s2 + '\n' + s1
print(s)
print(re.search(r'^M[ae][iy]er',s))  # None - since `Mayer` wasn't positioned right at the beginning of the whole string.

# By adding the `re.MULTILINE` argument, the result will be redefined as to search the multiple lines instead of oneline
print(re.search(r'^M[ae][iy]er', s, re.MULTILINE))
print(re.search(r'^M[ae][iy]er', s, re.M))
print(re.match(r'^M[ae][iy]er', s, re.M))   # match method doesn't show the success of matching since match() only checks for beginning

# The ending pattern is similar to beginning pattern by using `$` dollar sign


























