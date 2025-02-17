time_input = input()

h,m = time_input.split(":")
h = int(h)+1

print(f"{h}:{m}")