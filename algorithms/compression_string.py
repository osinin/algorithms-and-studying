"""
Write compress algorithm for string.
AaaAAAAA -> Aa2A5
"""


text = 'AaaAAAAA'


def compress_text(text: str) -> str:
    if len(text) > 0:
        compressed_s = text[0]
        cnt = 1
        i = 1
        while i <= (len(text)-1):
            if text[i-1] != text[i] and cnt == 1:
                compressed_s += text[i]
            elif text[i-1] != text[i] and cnt != 1:
                compressed_s += str(cnt)+text[i]
                cnt = 1
            elif text[i-1] == text[i]:
                cnt += 1
            i += 1
        if cnt > 1:
            compressed_s += str(cnt)
    return compressed_s


print(compress_text(text))
