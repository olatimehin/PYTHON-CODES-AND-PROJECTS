import os 
# my path                    # C:\Users\IGBEKELE OLATIMEHIN\Desktop\FUTURE CONNECT DATA ANALYSIS TRAINING\images
path = input("Enter path: ")
path = path.replace("\\", "/")
print(path)

print(os.listdir(path))

def main():
    i = 1
    for filename in os.listdir(path):
        new_name = path + str(i) + ".jpg"
        old_name = path + filename
        os.rename(old_name,new_name)
        i+=1
main()