import tesserocr
from tesserocr import PyTessBaseAPI

images = ['hello.jpg']

with PyTessBaseAPI() as api:
	for img in images:
		api.SetImageFile(img)
		print api.GetUTF8Text()
		print api.AllWordConfidences()