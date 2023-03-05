import qrcode

#we open the CSV file
with open('data.csv', 'r') as csv_file:
    
    #read the data from a line
    csv_reader = csv.reader(csv_file)
    
    #we go through each line 
    for line in csv_reader:
        
        #we get the data
        data = line[0]
        
        #we generate a QR code 
        qr = qrcode.QRCode(
            version = 1,
            box_size = 10,
            border = 5
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill = "black", back_color = "white")
        
        #save the image in png format
        img.save("qrcode_"+data+".png")
