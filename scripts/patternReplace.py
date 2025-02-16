import re

# Pattern to match a single digit number only if it's not part of a larger number
pattern = r'\b(\d)\b(?!\d)'

# Replacement pattern to add a leading zero
replacement = r'0\1.abc'

regex = re.compile(pattern)

filename = '3 sample files, 12 folders, and 7 more files'

# Substituting the pattern with the replacement
new_filename = regex.sub(replacement, filename)

print(new_filename)
