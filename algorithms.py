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


@time_elapsed
def kmp_search(pattern, text):
    pattern_len, text_len = len(pattern), len(text)
    found_indices = []
    lps_table = compute_lps_array(pattern)
    pattern_index, text_index = 0, 0

    while text_index < text_len:
        if pattern[pattern_index] == text[text_index]:
            text_index += 1
            pattern_index += 1

            if pattern_index == pattern_len:
                found_indices.append((text_index-pattern_index))
                pattern_index = lps_table[pattern_index-1]

        else:
            if pattern_index != 0 :
                pattern_index = lps_table[pattern_index-1]
            else:
                text_index += 1
            
        
    return found_indices                  


def compute_lps_array(pattern):
    # lps stands for longest_prefix_suffix
    prev_lps_len = 0

    pattern_index = 1
    pattern_len = len(pattern)
    lps_table = pattern_len * [0]

    while pattern_index < pattern_len:
        if pattern[pattern_index] == pattern[prev_lps_len]:
            prev_lps_len += 1
            lps_table[pattern_index] = prev_lps_len
            pattern_index += 1
        
        else:  
            if prev_lps_len != 0:
                prev_lps_len = lps_table[prev_lps_len - 1]

            else:
                lps_table[pattern_index] = 0
                pattern_index += 1 

    return lps_table
    

@time_elapsed
def rabin_karp(pattern, text):
    BASE, PRIME = 256, pow(9,10)+7
    pattern_len, text_len = len(pattern), len(text)
    found_indices = []
    pattern_hash = current_text_hash = 0

    h = pow(BASE, pattern_len - 1, PRIME)

    for i in range(pattern_len):
        pattern_hash = (BASE * pattern_hash + ord(pattern[i])) % PRIME
        current_text_hash = (BASE * current_text_hash + ord(text[i])) % PRIME

    for i in range(text_len - pattern_len + 1):
        if pattern_hash == current_text_hash:
            if text[i : i + pattern_len] == pattern:
                found_indices.append(i)

        if i < text_len - pattern_len:
            current_text_hash = (BASE * (current_text_hash - ord(text[i]) * h) + ord(text[i + pattern_len])) % PRIME
            
    return found_indices

