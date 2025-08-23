from discount import calculate_discount
def main():
  try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percent: "))

    final_price = calculate_discount(price,discount_percent)

    if discount_percent >=20:
      print(f"Final price after applying {discount_percent}% discount: ${final_price: .2f}")
    else:
      print(f"No discount applied. The price remains: {final_price:.2f}")
  except ValueError:
    print("Please enter valid numeric values for price and discount. ")

if __name__=="__main__":
  main()