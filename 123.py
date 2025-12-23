def sorted(arr,arr1,arr2):
    if arr1[0][0] ==0:
        c=arr2[0][1]-arr1[0][1]
        if c>0:
            c=c%len(arr)
            arr = arr[c:] + arr[:c]
            return arr
    else:
        c = arr1[0][1] - arr2[0][1]
        if c > 0:
            d = c%len(arr)
            arr = arr[-d:] + arr[:-d]
            return arr
    return arr
print(sorted([1,2,3,4,5,5],[(1,3)],[(0,2)]))

def version(v1,v2):
    try:
        v11 = list(map(int, v1.split(".")))
        v22 = list(map(int, v2.split(".")))
        if v11[0]>v22[0]:
            return v1
        elif v11[0]<v22[0]:
            return v2
        else:
            if v11[1]>v22[1]:
                return v1
            else:return v2
    except (ValueError, IndexError) as e:
        return f"错误:{e}"


if __name__ == '__main__':
    print(version("10","10"))