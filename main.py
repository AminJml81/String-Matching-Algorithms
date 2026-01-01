from algorithms import naive_search, naive_search_with_slices, kmp_search, rabin_karp


if __name__ == '__main__':
    pattern = 'AAAAAB'
    text = 'AAAAAAAAAAAAAAAAAAAAAB' * 1000000
    fi1 = naive_search(pattern=pattern, text=text)
    fi2 = naive_search_with_slices(pattern=pattern, text=text)
    fi3 = kmp_search(pattern=pattern, text=text)
    fi4 = rabin_karp(pattern=pattern, text=text)

    print(fi1 == fi2 == fi3 == fi4)
    print(fi1[:10])