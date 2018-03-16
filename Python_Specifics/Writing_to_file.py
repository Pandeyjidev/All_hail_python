text = 'Sample Text to Save\nNew Line!'

# read write and append
saveFile=open('exampleFile.txt','w')

saveFile.write(text)
saveFile.close()