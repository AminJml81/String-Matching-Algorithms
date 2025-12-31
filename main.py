from algorithms import naive_search, naive_search_with_slices, kmp_search


pattern = 'abc'
text = 'dddddddddddddddddd'
fi1 = naive_search(pattern=pattern, text=text)
fi2 = naive_search_with_slices(pattern=pattern, text=text)
fi3 = kmp_search(pattern=pattern, text=text)
print(fi1 == fi2 == fi3)
print(fi1[:10])