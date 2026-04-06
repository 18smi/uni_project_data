import csv

DEFALT_YEAR = 0
DEFALT_QUATER = 0
DEFALT_REGION = "blank"

def main():
    with open('five_year_dataset.csv', mode='r') as file:
        year = DEFALT_YEAR
        quater = DEFALT_QUATER
        region = DEFALT_REGION

        print("opening sqrall 'skip' skips the field")

        
        while True:# date
            date = input("input date form 1/1/2021 to 31/12/2025 (optional)")
            if date == "skip":
                break

            if not valid_date(date):
                print("invalid date")
                continue
            
            year = year_finder(date)
            quater = quater_finder(date)
            

        while True:# region
            input_region = input("input region (optional)")
            if input_region == "skip":
                break

            if not valid_region(input_region): #invalid region
                print("invalid date")
                continue
            
            region = input_region

        
        while True:# region code
            region_code = input("enter region code (optional)")
            if region_code == "skip":
                break
            
            if not valid_region_code:
                print("invalid region code")
                continue

            if region != region_code_to_region(region_code) and region != "blank":
                print("region vs region code conflict")
                continue
            
            region = region_code_to_region(region_code)

        if region == "blank":
            region = "United Kingdom"

        print("region, year, quater")
        print(region, year, quater)

        
        # defalt date = avrage over all
        # output expected New dwellings Price,New dwellings average advance,New dwellings average recorded income of borrowers,Other dwellings Price,Other dwellings average advance,Other dwellings average recorded income of borrowers,All dwellings Price,All dwellings average advance,All dwellings average recorded income of borrowers,First time buyers Price,First time buyers average advance,First time buyers average recorded income of borrowers,Former owner occupiers Price,Former owner occupiers average advance,Former owner occupiers average recorded income of borrowers




def valid_date(date):
    date.split('/')
    if len(date) != 3:
        return False
    if 2021 > int(date[2]) or 2025 < int(date[2]):
        return False
    if 1 > int(date[1]) or 12 < int(date[1]):
        return False
    if 1 > int(date[0]) or 31 < int(date[0]):
        return False

    return True
def year_finder(date):
    return int(date.split('/')[2])
def quater_finder(date):
    if int(date.split('/')[1]) < 4:
        return 1
    if 3 < int(date.split('/')[1]) < 7:
        return 2
    if 6 < int(date.split('/')[1]) < 10:
        return 3
    if 9 < int(date.split('/')[1]) < 13:
        return 4
    return 0

def valid_region(input_region):
    valid_regions = ["United Kingdom", "Great Britain", "England and Wales", "England", "North East", "North West", "Yorkshire and the Humber", "East Midlands", "West Midlands", "East of England", "London", "South East", "South West", "Wales", "Scotland", "Northern Ireland"]
    return bool(input_region in valid_regions)

def valid_region_code(region_code):
    valid_region_codes = ["K02000001", "K03000001", "K04000001", "E92000001", "E12000001", "E12000002", "E12000003", "E12000004", "E12000005", "E12000006", "E12000007", "E12000008", "E12000009", "W92000004", "S92000003", "N92000001"] 
    return bool(region_code in valid_region_codes)
def region_code_to_region(region_code):
    valid_regions = ["United Kingdom", "Great Britain", "England and Wales", "England", "North East", "North West", "Yorkshire and the Humber", "East Midlands", "West Midlands", "East of England", "London", "South East", "South West", "Wales", "Scotland", "Northern Ireland"]
    valid_region_codes = ["K02000001", "K03000001", "K04000001", "E92000001", "E12000001", "E12000002", "E12000003", "E12000004", "E12000005", "E12000006", "E12000007", "E12000008", "E12000009", "W92000004", "S92000003", "N92000001"] 

    return valid_regions[valid_region_codes.index("region_code")]



main()