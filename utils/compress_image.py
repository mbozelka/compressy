from PIL import Image
 
def compress_image(image_path, output_path, quality=70, subsampling=1, image_format='JPEG'):
    im = Image.open(image_path)
    temp_im = im.copy()
    temp_im.save(output_path, format=image_format, subsampling=subsampling, quality=quality, optimize=True)