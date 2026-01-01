from algorithms import naive_search, naive_search_with_slices, kmp_search, rabin_karp, boyer_moore


if __name__ == '__main__':
    pattern = 'AABC'
    text = 'AABCKLKLKAABCsuoauweiwqAABC '*100000
    print('Running algorithms with the following parameters:')
    print(f'pattern: {pattern}')
    print(f'text_length: {len(text)} characters')
    fi1 = naive_search(pattern=pattern, text=text)
    fi2 = naive_search_with_slices(pattern=pattern, text=text)
    fi3 = kmp_search(pattern=pattern, text=text)
    fi4 = rabin_karp(pattern=pattern, text=text)
    fi5 = boyer_moore(pattern=pattern, text=text)