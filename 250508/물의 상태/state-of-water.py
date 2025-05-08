inp = input()
arr = inp.split()
n = int(arr[0])

-200<n<200

if n<0:
    print("ice")
elif 0<n<100:
    print("water")
else:
    n > 100
    print("vaper")
