kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#with input
#convert miles to kms
kms=input("Enter number of Kms to be converted to miles: ")
convert=1.61
miles=convert*float(kms)
print(kms,"kms in miles is: ",miles)
#convert kms to miles
print("\n")
print("Converting miles to kms")
miles2=input("Enter number of miles to convert to kms: ")
kms2=float(miles2)/convert
print(miles2, "in kms is: ",round(kms2,2))