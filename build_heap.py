def build_heap(data):
    swaps = []
    for j in range ((len(data)-2)//2, -1, -1):
        siftDown(data, j, len(data),swaps)
    for end in range(len(data)-1, 0, -1):
        swap(data, 0, end, swaps)
        siftDown(data, 0, end, swaps) 
    return swaps

def swap(data, i, j, swaps):
    data[i], data[j] = data[j], data[i]
    swaps.append([i, j])
def siftDown(data, i, length,swaps):
    l, r = i*2+1, i*2+2
    while (True):
        if max(l, r) < length:
            if data[i] >= min(data[l],data[r]): break
            elif data[l] > data[r]:
                swap(data, i, l,swaps)
                i = l
            else:
                swap(data, i, r,swaps)
                i = r
        elif l < length:
            if data[l] > data[i]:
                swap(data, i, l, swaps)
                i = l
            else: break
        elif r < length:
            if data[r] > data[i]:
                swap(data, i, r, swaps)
                i = r
            else: break
        else: break


def main():
    
     try:
        text = input("Enter I or F: ")
        if text not in ["I", "F"]:
            raise ValueError("Invalid input, expected 'I' or 'F'")
        if text == "I":
            n = int(input())
            data = list(map(int, input().split()))
            if len(data) != n:
                raise ValueError(f"Invalid input, expected {n} elements")
            swaps = build_heap(data)
            print(len(swaps))
            for i, j in swaps:
                print(i, j)
        elif text == "F":
            filename = input()
            file_path = f"./text/{filename}"
            if "a" not in filename:
                try:
                    with open(file_path) as f:
                        n = int(f.readline())
                        data = list(map(int, f.readline().split()))
                        if len(data) != n:
                            raise ValueError(f"Invalid input, expected {n} elements")
                        swaps = build_heap(data)
                        print(len(swaps))
                        for i, j in swaps:
                            print(i, j)
                except FileNotFoundError:
                    print(f"Error: File {filename} not found")
                except:
                    print("Error: Invalid input in file")
     except ValueError as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
