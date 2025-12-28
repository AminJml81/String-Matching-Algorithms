from utils import time_elapsed


@time_elapsed
def naive_search(pattern, text):
    pattern_len, text_len = len(pattern), len(text)
    found_indices = []

    for text_index in range(text_len - pattern_len + 1):
        match_count = 0
        while match_count < pattern_len and text[text_index + match_count] == pattern[match_count]:
            match_count += 1
        
        if match_count == pattern_len:
            found_indices.append(text_index)
    
    return found_indices


@time_elapsed
def naive_search_with_slices(pattern, text):
    pattern_len, text_len = len(pattern), len(text)
    found_indices = []

    for text_index in range(text_len - pattern_len + 1):
        if text[text_index:text_index + pattern_len] == pattern:
            # This slicing is faster, because the C code which are compiled before runs.
            # It uses Boyer-Moore in the background
            found_indices.append(text_index)

    return found_indices
