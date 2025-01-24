from countryinfo import CountryInfo

# Demander le nom du pays à l'utilisateur
country = CountryInfo(input("Enter Country Name: ").strip())

# Informations sur le pays
print("Country Name:", country.name())
print("Capital:", country.capital())
print("Population:", country.info().get("population", "Unknown"))
print("Area (in square kilometers):", country.info().get("area", "Unknown"))
print("Region:", country.info().get("region", "Unknown"))
print("Subregion:", country.info().get("subregion", "Unknown"))
print("Demonym:", country.info().get("demonym", "Unknown"))
print("Timezones:", country.info().get("timezones", "Unknown"))
print("Currencies:", country.currencies())  
print("Languages:", country.languages())
print("Borders:", country.borders())
