import os,re,requests,time

path = "D:/jianshu/blogs" # 所有博客md文件

images = []
for root,dirs,files in os.walk(path):
	for name in files:
		file = os.path.join(root,name)
		with open(file,'r',encoding="utf8") as stream:
			content = stream.read()

		regex = r'!\[Paste_Image.png\]\((.+)\)'
		urls = re.findall(regex,content)
		images.extend(urls)

for image in images:
	print("正在下载---> " + image)
	matcher = re.search(r'http://upload-images.jianshu.io/upload_images/(.+)\?imageMogr2',image)
	filename = matcher.group(1)
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'Referer': 'http://www.jianshu.com'}
	response = requests.get(image, headers=headers)

	dest = "D:/jianshu/images/" + filename
	with open(dest, "wb") as fout:
		fout.write(response.content)
	print(filename + " 下载完成！")
	time.sleep(3)