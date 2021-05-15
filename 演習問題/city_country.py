def formatted_city_country(city, country):
	"""フォーマットされた国、都市を返す"""
	if city:
		city_country = f"{city} {country}"

	else:
		city_country = f"{city} {country}"
	return city_country.title()

country_city = formatted_city_country("santiago", "chile")
print(country_city)

country_city = formatted_city_country("japan", "tokyo")
print(country_city)

country_city = formatted_city_country("china", "beijing")
print(country_city)
