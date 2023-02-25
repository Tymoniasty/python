#calculate tax based on the province and nartionality
#using multiple conditions

province = input('What province do you live in? ')
#changing input to upper letter to ensure text is copmpared correctly
province = province.capitalize()
tax = 0

#below using multiple if statements with 'elif' (else if)
    # if province == 'Alberta':
    #     tax = 0.05
    # elif province == 'Nunavut':
    #     tax = 0.05
#below using or to apply one condition for provinces with the same tax rate
    # if province == 'Alberta' or province == 'Nunavut':
#below instead of listing variable and its value we can use 'in' operator to apply the same logic with shorter code
if province in('Alberta','Nunavut','Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)
print(province)