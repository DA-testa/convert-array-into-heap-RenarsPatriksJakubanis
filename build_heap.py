# python3
def build_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        while (i * 2) + 1 < len(data):
            heap_ch = 2 * i + 1
            if len(data) > heap_ch + 1 and data[heap_ch] > data[heap_ch + 1]:
                heap_ch = heap_ch + 1
            if data[heap_ch] >= data[i]:
                break
            swaps.append((i, heap_ch))
            data[heap_ch], data[i] = data[i], data[heap_ch]
            i = heap_ch
    return swaps

def main():
    data = []
    i = input()
    if i == "I":
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

    elif i == "F":
        input_key = input()
        location  = "tests/" + input_key
        with open(location) as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
