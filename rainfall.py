years = int(input("Enter number of years: "))

total_rainfall = 0
months = 0

for year in range(1, years + 1):
    print("Year", year)

    for month in range(1, 13):
        rainfall = float(input("Enter rainfall for month " + str(month) + ": "))
        total_rainfall += rainfall
        months += 1

average = total_rainfall / months

print("Months:", months)
print("Total rainfall:", total_rainfall)
print("Average rainfall:", round(average, 2))