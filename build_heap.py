# python3
def build_heap(data):
    swaps = []

    for i in range(len(data) // 1, -1, -1):
        while (i * 2) + 1 < len(data):
            heap_ch = 1 + (2 * i)
            if data[heap_ch] > data[i]:
                break
            elif len(data) > heap_ch + 1 and data[heap_ch] > data[heap_ch + 1]:
                heap_ch = heap_ch + 1
            swaps.append((i, heap_ch))
            data[heap_ch], data[i] = data[i], data[heap_ch]
            i = heap_ch
    return swaps

def main():
    i = input()
    if i == "I":
        n = input()
        data = list(map(int, input().split()))
        swaps = build_heap(data)
        
    elif i == "F":
        input_key = input()
        location  = "tests/" + input_key
        with open(location) as f:
            n = f.readline()
            data = list(map(int, f.readline().split()))
            swaps = build_heap(data)
    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
