from PIL import Image
import pyheif
import os

#this works assuming all non-jpg images are heics, which is the case for the test/train data
#basically this program converts all file names to uppercase regardless and converts heics to jpgs

def convert(img_path):
    heif_file = pyheif.read(img_path) #reads in heic img
    image = Image.frombytes( #make new image object
        heif_file.mode, #gets color space and pixel format (rgb)
        heif_file.size, #gets dimensions of image
        heif_file.data, #gets raw pixel data of the image 
        "raw", #states that the data is in raw form (idk tbh)
        heif_file.mode, #mode again for osme reason idk y
        heif_file.stride, #number of bytes per row idk exactly why this is necessary but yea
    )
    
    return image #returns new heic image
    
for folder in sorted(os.listdir("2023_Cursive")): #iterate over every folder
    for image in sorted(os.listdir("2023_Cursive/" + folder)): #iterate over every file
        os.rename("2023_Cursive/" + folder + "/" + image, "2023_Cursive/" + folder + "/" + image.upper()) #makes all names uppercase before doing anything so that in the end every file will be entirely uppercase and stuff will be consistent
        image = image.upper() #makes it so that the file name we're working with now is upper case because we just made it uppercase so the lower case version doesnt exist
        if "JPG" not in image and "JPEG" not in image: #if img not alr jpeg
            convert("2023_Cursive/" + folder + "/" + image).save("2023_Cursive/" + folder + "/" + image[:-4] + "JPG", format="JPEG", ) #runs the image thru the function to convert it to jpg and then saves it
            os.remove("2023_Cursive/" + folder + "/" + image) #removes the old heic file since saving the file with a different file extension doesnt override the old file
            print("2023_Cursive/" + folder + "/" + image + "  converted --------------> " + image[:-4] + "JPG") #debug sake
        else:
            print("2023_Cursive/" + folder + "/" + image + "  is fine") #debug sake
        
