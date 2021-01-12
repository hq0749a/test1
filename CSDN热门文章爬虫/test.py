import re

titles = [
    '/a.png',
    '/a.png',
    r'\a.png',
    ':a.png',
    '*a.png',
    '<a.png',
    '>a.png',
    '|a.png',
    '?a.png',
]

for title in titles:
    title = re.sub(
        r'[/\\:*"<>|?]', '', title
    )
    print(title)