def linearSearchProduct(productList, targetProduct):
   indices = []

   for index, product in enumerate(productList):
   	  if product == targetProduct:
   	  	indices.append(index)

   return indices


prducts = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(prducts, target)
print(result)