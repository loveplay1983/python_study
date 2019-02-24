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













