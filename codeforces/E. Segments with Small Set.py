n,k = map(int,input().split())
a = list(map(int,input().split()))
def count_segments_small_set(a,k):
    left = 0
    count = 0
    freq = {}
    for right in range(len(a)):
        freq[a[right]] = freq.get(a[right], 0) + 1
        while len(freq) > k:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1
        count += (right - left + 1)
    print(count)
count_segments_small_set(a,k)
