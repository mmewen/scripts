import requests
import shutil # to write raw images to file
import time
import os

url = "http://www.bing.com"
path = "/home/IBEO.AS/mem/Pictures/Wallpapers/Bing/"
current = "current"
ext = ".jpg"

# os.system(". /home/mewen/dev/scripts/get-wallpaper/discover_session_bus_address.sh")

# print "Ok, let's go"
# today = now.strftime("%Y-%m-%d")
try:
	r = requests.get(url, stream=True) # , params=payload, headers=headers, cookies=cookies, stream=True)
	if r.status_code == 200:
		imgUrl = r.content.split("g_img=")[1].split("'")[1] # /something....../imageName.jpg OR http://s.cn.bing.net/something....../imageName.jpg
		print imgUrl
		if imgUrl[0] is not "/" and imgUrl[0] is not "h":
			imgUrl = r.content.split("g_img=")[1].split("\"")[1]
			imgUrl = imgUrl.replace("\/", "/")
			if imgUrl[0] is not "/" and imgUrl[0] is not "h":
				print("Error in the img url : {0}".format(r.content.split("g_img=")[1][:100]))

		imgUrl = imgUrl.replace("\/", "/")

		fullImgUrl = imgUrl
		if imgUrl[0] is "/": # image hosted on http://www.bing.com
			fullImgUrl = url + imgUrl # http://www.bing.com/something....../imageName.jpg

		ext = "." + imgUrl.split(".")[-1] # .jpg
		fileName = ".".join(imgUrl.split(".")[:-1]).split("/")[-1] # imageName
		imgFile = path + fileName + ext # /home/usename/Images/Wallpapers/Bing/imageName.jpg
		
		# check if the background has changed
		if not os.path.exists(imgFile):
			# if not, than dowload it, dude !
			# print "Downloading " + fullImgUrl
			image = requests.get(fullImgUrl, stream=True)

			if image.status_code == 200:
				with open(imgFile, 'wb') as f:
					shutil.copyfileobj(image.raw, f)
				os.system("cp " + imgFile + " " + path + current + ext)
				# print "Image correctly downloaded at " + imgFile + " !"
				print "New wallpaper set"
				# time.sleep(0.2)
				# os.system("gsettings set org.gnome.desktop.background picture-uri file://" + imgFile)
			else:
				print "ERROR: Got {0} code from bing.".format(r.status_code)
		else:
			print "ERROR: Image already downloaded"
	else:
		print "ERROR: Got " + r.status_code + " code from bing."
except requests.exceptions.ConnectionError, e:
	# raise e
	print e #"No internet, so bad :/"

#print "Waiting a minute"
#time.sleep(60) # wait a minute
