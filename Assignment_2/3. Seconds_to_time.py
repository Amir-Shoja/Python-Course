seconds = int(input("Enter seconds : "))


hour = int(seconds // 3600)
min = int((seconds % 3600) // 60)
second = int((seconds % 3600) % 60)

print(str(hour).zfill(2), ":", str(min).zfill(2), ":", str(second).zfill(2))
