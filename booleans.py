population_in_seoul = 10_000_000
population_in_united_states = 300_000_000

yes = True
no = False

#print(True or False)

#print(population_in_seoul)

if population_in_seoul < 100:
    print("Seoul is a small city")
    
elif population_in_seoul <= 10_000 and population_in_seoul >= 1_000_000:
    print("Seoul is medium")
    
else:
    print("Seoul is huge")