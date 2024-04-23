import csv

input_csv_path = "/home/navanaeedh/Documents/account_data.csv"
# output_csv_path = "/home/navanaeedh/Documents/output.csv"
data = []
with open(input_csv_path) as csvfileip:
    csv_reader = csv.reader(csvfileip)
    print(csv_reader)
    print(type(csv_reader))
    for row in csv_reader:
        # print(row)
        # print(type(row))
        data.append(row)
print("data",data)
# ac_no = "IBI00S00147"hs@123

ac_no = input("Enter the Account Number: ")
flag = False
user_details = []
for acn_rec in data:
    if ac_no in acn_rec:
       flag=True
       user_details = acn_rec
    else:
        pass
if flag:
    print("acount number exists in file",user_details)
else:
    print("acount number not exists in file")
# user = input("Enter the Account Number: ")
# user1 = input("1.Deposit\n2.WithDraw\n3.Check Balance\n")

# if Acc_num == user:
#     print("Account number: {user}.")


# with open(output_csv_path, 'w') as csvfileop:
#     csv_writer = csv.writer(csvfileop)
#     csv_writer.writerows(rows) 
# print("Data Successfully written to:", output_csv_path)    

# print (csvfileop)