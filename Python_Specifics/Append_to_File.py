appendMe='\n New Bit of informaion'

appendFile=open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()