counties = ["Arapahoe", "Denver", "Jefferson"]

my_list = list(counties)
print(counties[0])

print(len(counties))

counties.append("El Paso")
print(counties)

counties.insert(2,"El Paso")
print(counties)

counties.remove("El Paso")
print(counties)

counties.pop(3)
print(counties)

counties[2] = "El Paso"
print(counties)

counties_dict = dict({  'Arapahoe' : 422829,
                        'Denver': 463353,
                        'Jefferson' : 423438
                    }
    )

print(counties_dict.get('Arapahoe'))
