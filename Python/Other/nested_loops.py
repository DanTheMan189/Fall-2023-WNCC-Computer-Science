print ("=============================")

for i in range(0, 4):
    print (f"-------- Exterior Loop {i} --------")
    print (f"-------- Interior Loop --------")

    for j in range(0, 5):
        print (f"{j}", end="\t")

    print ("\n")
