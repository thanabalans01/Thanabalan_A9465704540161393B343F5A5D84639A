def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = [
    "ROYALENFIELD", "HELLCAT", "CARRERA", "STRADALE", "SENNA", "VANTAGE",
    "STRADALE", "ROYALENFIELD", "ROYALENFIELD"
]
target = "ROYALENFIELD"
result = linearSearchProduct(products, target)
print(result)