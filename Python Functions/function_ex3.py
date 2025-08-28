def convert_inr(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =",inr_val,"INR")
    
n = int(input("Enter number:"))
convert_inr(n) 