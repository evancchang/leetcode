def dup_encoder(s: str) -> str:
    char_count = {}
    s = s.lower()
    for c in s:
        if c not in char_count.keys():
            char_count[c] = 1
        else:
            char_count[c] += 1

    encode_str = ''
    for c in s:
        if char_count[c] == 1:
            encode_str += '('
        else:
            encode_str += ')'

    return encode_str

print(dup_encoder('din') == '(((')
print(dup_encoder('recede') == '()()()')
print(dup_encoder('Success') == ')())())')
print(dup_encoder('(( @') == '))((')
