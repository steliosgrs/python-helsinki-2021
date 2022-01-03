# Write your solution here
student = int(input("How many students on the course? "))
g_size = int(input("Desired group size? "))
modulo = student%g_size
if modulo == 0:
    r = student/g_size
else:
    r = student//g_size
    r += 1

print(f"Number of groups formed: {r}")
