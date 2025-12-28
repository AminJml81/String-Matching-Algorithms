from algorithms import naive_search, naive_search_with_slices


pattern = 'kd'
text = 'abcdeamskdmacdasdkoakodk'*1_000_000
fi1 = naive_search(pattern=pattern, text=text)
fi2 = naive_search_with_slices(pattern=pattern, text=text)

print(fi1 == fi2)
print(fi1[:10])