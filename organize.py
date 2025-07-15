import os
import shutil

def organize_images(source_dir):
  image_type={
    'jpg_Image': ['.jpg'],
    'jpeg_Image': ['.jpeg'],
    'png_Image': ['.png'],
    'others': []
  }

  for folder in image_type.keys():
    dir_path =os.path.join(source_dir,folder)
    if not os.path.exists(dir_path):
      os.makedirs(dir_path)


  for filename in os.listdir(source_dir):
    if os.path.isfile(os.path.join(source_dir, filename)):
      file_extension = os.path.splitext(filename)[1].lower()
      moved = False
      for folder, extensions in image_type.items():
        if file_extension in extensions:
          shutil.move(os.path.join(source_dir, filename), os.path.join(source_dir, folder, filename))
          moved = True
          break
      
      if not moved:
        shutil.move(os.path.join(source_dir, filename), os.path.join(source_dir, 'others', filename))

if __name__ == "__main__":
  source_dir = input("Enter the source directory path: ")
  organize_images(source_dir)
  print("Images organized successfully.")