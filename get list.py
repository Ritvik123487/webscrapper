import openpyxl
file = openpyxl.open("Forbes.xlsx")
sheet = file["Sheet1"]
i = 1
file = open("comps.txt","w")
print("[",file=file)
while i < sheet.max_row+1:
    try:
        print("'"+sheet.cell(row = i, column=2).hyperlink.target+"',",file=file)
        i+=1
    except Exception:
        print(i)
print("]",file=file)