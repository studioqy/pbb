'''
QY
December 5 2020
PBB

Week 11/12
Life Expetancy Assignment
Focus: Files
'''

with open("life-expectancy.csv") as life_expectancies:
    lowest_exp = 999
    year_low_exp = 999
    highest_exp = 0
    year_high_exp = 0
    tracker = 0

    picked_year = int(input("Enter a year:"))
    avg_counter = 0
    year_expectancy = 0

    picked_country = input("Enter a country:")
    c_low_exp = 999
    c_high_exp = 0
    c_expectancy = 0
    c_avg_counter = 0

    for single_line in life_expectancies:
        if tracker == 0:
            tracker += 1
        else:
            single_word = single_line.split(",")
            country = single_word[0]
            country_code = single_word[1]
            year = int(single_word[2])
            life_exp = float(single_word[3])
            if life_exp < lowest_exp:
                lowest_country = country
                lowest_code = country_code
                lowest_year = year
                lowest_exp = life_exp
            if life_exp > highest_exp:
                highest_country = country
                highest_code = country_code
                highest_year = year
                highest_exp = life_exp
            if year == picked_year:
                year_expectancy += life_exp
                avg_counter += 1
                if life_exp < year_low_exp:
                    year_low_country = country
                    year_low_code = country_code
                    year_low_exp = life_exp
                if life_exp > year_high_exp:
                    year_high_country = country
                    year_high_code = country_code
                    year_high_exp = life_exp
            if country == picked_country:
                c_expectancy += life_exp
                c_avg_counter += 1
                if life_exp < c_low_exp:
                    c_low_year = year
                    c_low_exp = life_exp
                if life_exp > c_high_exp:
                    c_high_year = year
                    c_high_exp = life_exp
print(
    f"Lowest Life Expectancy: {lowest_country} {lowest_code} {lowest_year} {lowest_exp}")
print(
    f"Highest Life Expectancy: {highest_country} {highest_code} {highest_year} {highest_exp}")
print(f"{picked_year} Life Expectancy Average: {year_expectancy/avg_counter}")
print(F"{picked_year} Lowest Life Expectancy: {year_low_country} {year_low_code} {year_low_exp}")
print(F"{picked_year} Highest Life Expectancy: {year_high_country} {year_high_code} {year_high_exp}")
print(f"{picked_country} Lowest Life Expectancy: {c_low_year} {c_low_exp}")
print(f"{picked_country} Highest Life Expectancy: {c_high_year} {c_high_exp}")
print(f"{picked_country} Average Life Expectancy: {c_expectancy/c_avg_counter}")
