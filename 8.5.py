def nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False
    
nam = 2024
if nam_nhuan(nam):
    print(f"{nam} là năm nhuận.")
else:
    print(f"{nam} không phải là năm nhuận.")
