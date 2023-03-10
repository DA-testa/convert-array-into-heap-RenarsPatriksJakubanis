# python3
def build_heap(data):
    swaps = []

    for i in range(len(data) // 1, -1, -1):
        while i * 2 + 1 < len(data):
            heap_ch = 1 + 2 * i
            if data[heap_ch + 1] < data[heap_ch] and heap_ch + 1 < len(data):
                heap_ch = heap_ch + 1
            if data[i] < data[heap_ch] or heap_ch > len(data):
                break
            data[heap_ch], data[i] = data[i], data[heap_ch]
            swaps.append((i, heap_ch))
            i = heap_ch
    return swaps

def main():
    swaps = []
    i = input()
    if i == "I":
        n = input()
        data = list(map(int, input().split()))
        swaps = build_heap(data)
    elif i == "F":
        n = input()
        location  = "tests/" + n
        with open(location) as f:
            n = f.read()
            data = list(map(int, n.split()))
            swaps = build_heap(data)
   
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
