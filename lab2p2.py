def get_temperature_input(prompt):
    while True:
        try:
            temperature = float(input(prompt))
            return temperature
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        try:
            num_years = int(input("Enter the number of years: "))
            if num_years > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    total_yearly_highs = 0
    total_monthly_highs = 0
    num_months = 12

    for year in range(1, num_years + 1):
        print(f"\nEnter temperatures for year {year}:")
        yearly_highs = 0

        for month in range(1, num_months + 1):
            temperature = get_temperature_input(f"Enter the high temperature for month {month}: ")
            yearly_highs += temperature
            total_monthly_highs += temperature

        average_yearly_high = yearly_highs / num_months
        print(f"Average high temperature for year {year}: {average_yearly_high:.2f}")
        total_yearly_highs += average_yearly_high

    average_monthly_high = total_monthly_highs / (num_years * num_months)
    print(f"\nAverage monthly high temperature over {num_years} years: {average_monthly_high:.2f}")

    average_yearly_high_overall = total_yearly_highs / num_years
    print(f"Average yearly high temperature over {num_years} years: {average_yearly_high_overall:.2f}")

if __name__ == "__main__":
    main()