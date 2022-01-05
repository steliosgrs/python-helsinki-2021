# Write your solution here
year = int(input("Year: "))
nyear = year+1
while True:
    if nyear%4 == 0:
        if nyear%100 == 0:
            if nyear%400 == 0:
                print(f"The next leap year after {year} is {nyear}")
                break
        else:
            print(f"The next leap year after {year} is {nyear}")
            break
    nyear+=1