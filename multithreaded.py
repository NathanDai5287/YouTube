from youtube import download, videos

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
	[executor.submit(download, link, path='C:\\Users\\natha\\Downloads\\小欢喜')  for link in videos]
