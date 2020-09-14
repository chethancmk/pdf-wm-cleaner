from pdf2image import convert_from_path
from PIL import Image
import image_cleaner as imgc
import img2pdf
import argparse
import io

def img2bytes(image):
    buf = io.BytesIO()
    image.save(buf, format='JPEG')
    byte_im = buf.getvalue()
    return byte_im
    
def process(filename):
    
    # filename = "CKM_EB_20200825_00003.pdf"
    images = convert_from_path(filename, 500)        
    print("Processing Started")
    print("PDF has {} pages".format(len(images)))
    
    processed_images=[]
    print("Cleaning Images with filters")
    for imgnum,image in enumerate(images):
        cleaned_image = imgc.cleanImage(image)   
        processed_images.append(cleaned_image)
    
    print("Converting images to PDF Bytes")
    pdfout = img2pdf.convert(*list(map(img2bytes, processed_images)))
    
    print("Saving PDF Bytes to File {}".format('out_'+filename))
    f = open('out_'+filename, mode="wb")
    f.write(pdfout)
    f.close()
    
    print("Processing Completed")
        

process("CKM_EB_20200821_00003.pdf")

