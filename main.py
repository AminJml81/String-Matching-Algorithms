
from algorithms import naive_search, naive_search_with_slices


pattern = 'kd'
text = 'abcdeamskdmacdasdkoakodk'*1_000_0000
fi1, d1 = naive_search(pattern=pattern, text=text)
fi2, d2 = naive_search_with_slices(pattern=pattern, text=text)

print(f'Method 1 found in {d1} seconds')
print(f'Method 2 found in {d2} seconds')

print(fi1 == fi2)
print(fi1[:10])