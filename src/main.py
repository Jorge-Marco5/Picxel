import os
import core.convert_to_pixerlart as convert_to_pixelart
import core.create_ascii as create_ascii
import core.select_file as select_file

def main():
    file_path = select_file.select_file()
    if not file_path:
        print("No file selected.")
        return

    path = os.getcwd()+"/pictures/"
    # Check if directory exists, if not create it
    if not os.path.exists(path):
        os.makedirs(path)
        
    image_result = convert_to_pixelart.convert_to_pixelart(file_path, 10, path+"result.png")
    image_result.show()
    create_ascii.create_ascii(path+"result.png")



if __name__ == "__main__":
    main()
