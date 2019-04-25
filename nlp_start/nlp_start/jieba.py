import jieba
import re
from tokenizer import cut_hanlp
jieba.load_userdict('dict.txt') 
def merge_tow_list(a, b):
    c = []
    len_a, len_b = len(a), len(b)
    minlen = min(len_a , len_b)
    for i in range(minlen):
        c.append(a[i])
        c.append(b[i])

    if len_a > len_b:
        for i in range(minlen, len_a):
            c.append(a[i])
    else:
        for i in range(minlen, len_a):
            c.append(b[i])
    return c


