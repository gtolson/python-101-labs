#!/usr/bin/python

#given vars
current_pop = 380123456
counter = 1
person_born = 6
person_die = 12
person_imm = 40

# math
sec_in_year = 60 * 60 * 24 * 365
people_born_year = sec_in_year / person_born
people_die_year = sec_in_year / person_die
people_imm_year = sec_in_year / person_imm
# convert float to int
people_born_year = int(people_born_year)
people_die_year = int(people_die_year)
people_imm_year = int(people_imm_year)

print(f"current population - {current_pop}")
print(f"Total of new births to the population per year: {people_born_year}")
print(f"Total of new immigrants to the population per year: {people_imm_year}")
print(f"Total of deaths in the population per year: {people_die_year}")

while (counter <= 3):
    population_value = (people_born_year * counter) + (people_imm_year) * counter - (people_die_year) *counter + current_pop
    print(f"The population after {counter} year(s) will be = {population_value}")
    counter += 1



    


