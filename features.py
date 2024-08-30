def  search_by_date(transactions):
  date=input("enter the date")
  for transaction in transactions:
    if transaction["date"]==date:
      return transaction
  return "transaction not found."


def sort(transactions):
  n=len(transactions)
  for i in range(n):
    for j in range(n-1):
      if transactions[j]["amount"]>transactions[j+1]["amount"]:
        transactions[j],transactions[j+1]=transactions[j+1],transactions[j]
  return transactions

def add_date(transactions):
  desc={"date":input("enter the date "),
      "amount":int(input("enter the amount")),
      "desc":input("enter the disc")}
  transactions.append(desc)
  return transactions

def delete_date(transactions):
  date=input('enter the date')
  for transaction in transactions:
    if transaction["date"]==date:
      transactions.remove(transaction)
  return transactions

def sum_amount(transactions):
  year=input("enter year: ")
  sum=0
  for transaction in transactions:
    if transaction["date"][0:4]==year:
        sum=+transaction["amount"]
  return sum




