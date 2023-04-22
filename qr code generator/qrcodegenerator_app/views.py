from django.shortcuts import render
import qrcode
import os
from PIL import Image 
# Create your views here.
def index(request):
   # first check method is post or not 
   if request.method != 'POST':
      return render(request,"index.html")
   # if method is post & get the text
   text=request.POST.get('text')
   # generate the qrcode instance
   qr = qrcode.QRCode(version=1, box_size=8, border=3)
   # add the text in qrcode instance
   qr.add_data(text)
   qr.make(fit=True)
   # convert qr code instance into image 
   img=qr.make_image(fill_color='black',back_color='white')
   # save the image in static folder
   img_path = f"{os.getcwd()}/qrcodegenerator_app/static/img/qr_code.png"
   img.save(img_path)
   # making a context dictionary for render the image
   context={'qr_code_path': img_path}

   return render(request,"index.html",context)

