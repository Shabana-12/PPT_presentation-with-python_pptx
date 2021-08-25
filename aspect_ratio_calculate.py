import os
from wand.image import Image
path1="./original images"
files = os.listdir("original images")

# aspect_ratio=width/height
for i in files:
    ny = Image(filename =i)

    aspect_ratio=ny.width/ny.height
    print(f"aspect ratio of {i} from original images ")
    print(aspect_ratio)
path2='./result images' 
result_files = os.listdir("result images") 
for j in result_files:
    im= Image(filename =j)

    aspect_result=im.width/im.height
    print(f"aspect ratio of {j} from result images ")
    print(aspect_result)
    