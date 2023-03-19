import math

def build_heap(data):
    swaps = []
    for j in range (math.floor(len(data)/2), -1, -1):
        siftDown(data, j,swaps)
    for end in range(len(data), 0, -1):
        # swap(data, 0, end, swaps)
        siftDown(data, end, swaps) 
    return swaps

def swap(data, i, j, swaps):
    data[i], data[j] = data[j], data[i]
    swaps.append([j, i])
    return swaps
def siftDown(data, i,swaps):
    l, r = i*2+1, i*2+2
    smallest_num = i
    if(l < len(data) and data[l] < data[smallest_num]):
        smallest_num = l
    if(r < len(data) and data[r] < data[smallest_num]):
        smallest_num = r
    if(smallest_num != i):
        swap(data, smallest_num, i, swaps)
        siftDown(data, smallest_num, swaps)
    return swaps



    


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
                        print(data)
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
