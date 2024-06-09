# Store Stock
muffins = 10
cupcakes = 10

# Buying
buying = input ('Do you want to buy a muffin or a cupcake or press 0 to end. ')

while buying != "0":
    if buying == "muffin":
            if muffins > 0:
                    muffins -= 1
            else:
                    print ("Out of Stock")
    elif buying == "cupcake":
            if cupcakes > 0:
                    cupcakes -= 1
            else:
                    print ("Out of Stock")
    buying = input ('Do you want to buy a muffin or a cupcake or press 0 to end. ')

print ("muffins:", muffins, "cupcakes:", cupcakes)


 
            
