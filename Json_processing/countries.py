from json import load

f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\JSON_FILES\\countries.json",encoding="UTF-8")

data=load(f)

#print no of countries

print(len(data))


#print all country names

all_country_names=[country.get('name') for country in data]
print(all_country_names)

#print all regions

all_regions=[country.get('region')   for country in data]

print(set(all_regions))


region_count={reg:all_regions.count(reg)  for reg in all_regions}

print(region_count)

# maximum count   
max_count=max(region_count.items(),key=lambda x:x[1])[0]
print(max_count)

# or 

            # max_count=max(region_count,key=lambda x:region_count.get(x))
            # print(max_count)
            
            
            
#sort on basis of region  
sorted_regions=sorted(region_count,key=lambda x:region_count.get(x),reverse=True)
print(sorted_regions)

#print capital of a country

user_country="India"
country_capitals=[country.get('capital')  for country in data if country.get('name')==user_country]
print(country_capitals)


#print country with maximum no of borders

country_bordrder_count={country.get("name"):len(country.get("borders",[]))for country in data }
print(max(country_bordrder_count,key=lambda x:country_bordrder_count.get(x)))

# country_bordrder_count={country.get("name"):len(country.get("borders",[]))for country in data }
# print(max(country_bordrder_count.items(),key=lambda x:x[1]))


#most populated country

# most_populated_count=max([country.get('population')  for country in data])
# most_pop_country=[coun.get('name')   for coun in data if coun.get('population')==most_populated_count]
# print(most_pop_country)


most_populated_country=max(data,key=lambda country:country.get('population',[]))['name']
print(most_populated_country)


#border share by a country
country_name_by_user='China'
alpha_3_code=next(country.get('borders')  for country in data if country.get('name')==country_name_by_user)

country_names_border=[country.get('name') for country in data  if country.get('alpha3Code') in alpha_3_code]
print(country_names_border)

