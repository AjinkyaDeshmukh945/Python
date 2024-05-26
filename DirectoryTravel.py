import os

def main():
    print("eneter the name of directory that you want to scan :")
    DName = input()
    print("List of files in folder are :")

    for folderName, subfoldername , filename in os.walk(DName):
        for fname in filename :
            print(fname)

if __name__ == "__main__" :
    main()
