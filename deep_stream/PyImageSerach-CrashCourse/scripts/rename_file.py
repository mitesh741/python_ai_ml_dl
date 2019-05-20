# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
      
    for filename in os.listdir("./"):
        print("Filename : {}".format(filename))
        dst ="motorcycle_" + filename
        src = filename
        # dst ='../helmet'+ dst 
        print("Source File : {},  New File : {}".format(src,dst))
        
        # rename() function will 
        # rename all the files 
        os.rename(src, dst)
        # break
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
