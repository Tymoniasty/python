#use nested if to check for country first and then if 'Canada' apply tax condition
country = input('What country are you from? ')
#capitalize input
country = country.capitalize()
tax = 0
province = None
#if statement
if country == 'Canada':
    province = input('What province do you live in? ')
#changing input to upper letter to ensure text is copmpared correctly
    province = province.capitalize()
    if province in('Alberta','Nunavut','Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
print(country,province,tax)