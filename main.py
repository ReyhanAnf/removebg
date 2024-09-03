

# Importing Required Modules 
from rembg import remove 
from PIL import Image 
  
# Store path of the image in the variable input_path 
input_path = str(input("Masukan Path File Gambar : ")) 

path = input_path.split("\\")
headpath = path[0]
for i in path[1:len(path)-1]:
    headpath += "/" + i

filename = path[-1]

# Store path of the output image in the variable output_path 
output_path = headpath + "/" + filename.split(".")[0] + "_rbg.png"
  
# Processing the image 
input = Image.open(input_path) 
  
# Removing the background from the given Image 
output = remove(input) 
  
#Saving the image in the given path 
output.save(output_path)

# print(headpath)
# print(filename)
# print(output_path)
