print("How many miles did you drive today?")
miles= input()
kms = float(miles)*1.60934
kms = round(kms, 2) # round(some float, to this many decimal places)
print(f"Your {miles} mile drive is {kms} kilometers.")