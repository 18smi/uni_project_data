import pandas as pd

CSV_NAME = "five_year_dataset.csv"

DEFALT_YEAR = 0
DEFALT_QUATER = 0
DEFALT_REGION = "United Kingdom"
STARTING_REGION = "blank"

def main():    
    year = DEFALT_YEAR
    quater = DEFALT_QUATER
    region = STARTING_REGION

    print("how to use guide 'skip' skips the field")

        
    while True:# date
        date = input("input date form 1/1/2021 to 31/12/2025 (optional):  ")
        if date.lower() == "skip":
            break

        if not valid_date(date):
            print("invalid date")
            continue
            
        year = year_finder(date)
        quater = quater_finder(date)
        break
            

    while True:# region
        input_region = input("input region (optional):  ")
        if input_region.lower() == "skip":
            break

        if not valid_region(input_region): #invalid region
            print("invalid region")
            continue
            
        region = input_region.title()
        break

        
    while True:# region code
        region_code = input("enter region code (optional):  ")
        if region_code.lower() == "skip":
            break
            
        if not valid_region_code(region_code):
            print("invalid region code")
            continue

        if region != region_code_to_region(region_code) and region != "blank":
            print("region vs region code conflict")
            continue
            
        region = region_code_to_region(region_code)
        break

    if region == STARTING_REGION:
        region = DEFALT_REGION

    print('\n')

    display_prices(region, year, quater)


def valid_date(date):
    date = date.split('/')
    if len(date) != 3:
        return False
    if 2021 > int(date[2]) or 2025 < int(date[2]):
        return False
    if 1 > int(date[1]) or 12 < int(date[1]):
        return False
    if 1 > int(date[0]) or 31 < int(date[0]):
        return False
    if (date[1] == '4' or date[1] == '6' or date[1] == '9' or date[1] == "11") and date[0] == "31":
        return False
    if date[1] == '2' and date[0] > "29":
        return False
    return True

def year_finder(date):
    try:
        year = int(date.split('/')[2])
        return year
    except:
        return -1

def quater_finder(date):
    if 0 < int(date.split('/')[1]) < 4:
        return 1
    if 3 < int(date.split('/')[1]) < 7:
        return 2
    if 6 < int(date.split('/')[1]) < 10:
        return 3
    if 9 < int(date.split('/')[1]) < 13:
        return 4
    return 0

def valid_region(input_region):
    valid_regions = ["United Kingdom", "Great Britain", "England And Wales", "England", "North East", "North West", "Yorkshire And The Humber", "East Midlands", "West Midlands", "East Of England", "London", "South East", "South West", "Wales", "Scotland", "Northern Ireland"]
    return bool(input_region.title() in valid_regions)

def valid_region_code(region_code):
    valid_region_codes = ["K02000001", "K03000001", "K04000001", "E92000001", "E12000001", "E12000002", "E12000003", "E12000004", "E12000005", "E12000006", "E12000007", "E12000008", "E12000009", "W92000004", "S92000003", "N92000001"] 
    return bool(region_code in valid_region_codes)

def region_code_to_region(region_code):
    valid_regions = ["United Kingdom", "Great Britain", "England and Wales", "England", "North East", "North West", "Yorkshire and the Humber", "East Midlands", "West Midlands", "East of England", "London", "South East", "South West", "Wales", "Scotland", "Northern Ireland"]
    valid_region_codes = ["K02000001", "K03000001", "K04000001", "E92000001", "E12000001", "E12000002", "E12000003", "E12000004", "E12000005", "E12000006", "E12000007", "E12000008", "E12000009", "W92000004", "S92000003", "N92000001"] 
    try:
        return valid_regions[valid_region_codes.index(region_code)]
    except:
        return "not found"

def display_prices(region, year, quater):
    try:# checks all inputs are in the corect type
        region = str(region)
        year = int(year)
        quater = int(quater)
    except (ValueError, TypeError):
        return
    
    if not 0 < quater < 5 and quater != DEFALT_QUATER:
        print("invalid quater")
        return
    if not 2020 < year < 2026 and year != DEFALT_YEAR:
        print("invalid year")
        return
    if not valid_region(region):
        print("invalid region")
        return

    date = str(year) + " Q" + str(quater)

    csv = pd.read_csv(CSV_NAME)

    row_name = ["New dwellings Price", "New dwellings average advance", "New dwellings average recorded income of borrowers", 
                "Other dwellings Price", "Other dwellings average advance", "Other dwellings average recorded income of borrowers", 
                "All dwellings Price", "All dwellings average advance", "All dwellings average recorded income of borrowers", 
                "First time buyers Price", "First time buyers average advance", "First time buyers average recorded income of borrowers", 
                "Former owner occupiers Price", "Former owner occupiers average advance", "Former owner occupiers average recorded income of borrowers"]

    chosen_row = []
    if year == DEFALT_YEAR:
        inportant_row = csv[csv["Region"] == region]
        if inportant_row.empty:
            print("no rows found")
            return
        for name in row_name:
            int_row = pd.to_numeric(inportant_row[name], errors="coerce")
            value = int_row.mean(skipna=True)
            chosen_row.append(value)
    else:
        inportant_row = csv[(csv["Period"] == date) & (csv["Region"] == region)]
        if inportant_row.empty:
            print("no rows found")
            return
        for i in range(0, len(row_name)):
            chosen_row.append((inportant_row.iloc[0])[row_name[i]])

    

    for i in range(0, len(row_name)):
        print(row_name[i], '£', chosen_row[i])

    
    


if __name__ == "__main__":
    main()