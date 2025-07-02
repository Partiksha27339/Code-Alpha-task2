portfolio={"apple":650,"tesla":750}
stock_number_apple=int(input("enter the number of stocks of apple="))
stock_number_tesla=int(input("enter the number of stocks of tesla="))
var=stock_number_apple*portfolio["apple"]
var1=stock_number_tesla*portfolio["tesla"]
var2=var+var1
print(f"total investment={var2}")

with open("total_investment.txt", "w") as f:
    f.write(f"Total investment: {var2}\n")