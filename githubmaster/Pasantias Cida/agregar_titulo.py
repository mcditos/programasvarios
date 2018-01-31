with open("fort13.dat") as f1:
     data=f1.read() 
     data=data.replace("    ",",")  
     with open("HS13.dat", "w") as f2:
        f2.write("Longitud,Latitud ,HS \n")
        for line in data:
            f2.write(line)
