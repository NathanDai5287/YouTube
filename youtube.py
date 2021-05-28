from pytube import YouTube

import uuid
import os

def download(link: str, path='C:\\Users\\natha\\Downloads', **kwargs):
	youtube  = YouTube(link)

	folder = str(uuid.uuid4())

	video = youtube.streams.get_by_itag(137).download(f'{path}\\{folder}_video')
	audio = youtube.streams.get_by_itag(140).download(f'{path}\\{folder}_audio')

	os.chdir(path)

	if ('filename' in kwargs):
		filename = kwargs['filename']
	else:
		filename = video.split('\\')[-1]

	with open(video) as f:
		os.system(f'ffmpeg -i "{video}" -i "{audio}" -map 0:v -map 1:a -c:v copy -c:a copy "{filename}" -y')

	os.remove(video)
	os.remove(audio)

	os.rmdir(f'{path}\\{folder}_video')
	os.rmdir(f'{path}\\{folder}_audio')

	print('DONE')

videos = [
	"https://www.youtube.com/watch?v=mTMb8e_gDzE&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=1",
	"https://www.youtube.com/watch?v=nnxSTdpBAV4&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=2",
	"https://www.youtube.com/watch?v=iRzQkfyxl2c&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=3",
	"https://www.youtube.com/watch?v=yzs5YShQdrY&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=4",
	"https://www.youtube.com/watch?v=2WNpWUfr4XY&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=5",
	"https://www.youtube.com/watch?v=M7hR8hjYcMo&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=6",
	"https://www.youtube.com/watch?v=uSlT6dSkRC8&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=7",
	"https://www.youtube.com/watch?v=hkU2mXM_HBw&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=8",
	"https://www.youtube.com/watch?v=dcm3PxCe2vw&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=9",
	"https://www.youtube.com/watch?v=qLxcr6MBv_Q&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=10",
	"https://www.youtube.com/watch?v=gl_X7K7k-Is&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=11",
	"https://www.youtube.com/watch?v=CpdRY4155Ek&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=12",
	"https://www.youtube.com/watch?v=UKAvnPZ48Dg&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=13",
	"https://www.youtube.com/watch?v=tI-7-NQrsxQ&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=14",
	"https://www.youtube.com/watch?v=Os89K1octlo&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=15",
	"https://www.youtube.com/watch?v=E-U8ONs4ENI&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=16",
	"https://www.youtube.com/watch?v=TwLI_PFZ7Z8&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=17",
	"https://www.youtube.com/watch?v=kAMCB069_u0&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=18",
	"https://www.youtube.com/watch?v=DWUQaA1tPW0&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=19",
	"https://www.youtube.com/watch?v=N5dWGcBz5dA&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=20",
	"https://www.youtube.com/watch?v=WPMFmCGaAeU&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=21",
	"https://www.youtube.com/watch?v=WlCOfngbVxA&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=22",
	"https://www.youtube.com/watch?v=k7BKeheImFk&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=23",
	"https://www.youtube.com/watch?v=sfRDaeT-bPU&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=24",
	"https://www.youtube.com/watch?v=87pDmWyhIXg&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=25",
	"https://www.youtube.com/watch?v=LmTQSwihXWY&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=26",
	"https://www.youtube.com/watch?v=e7x3qZBJc10&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=27",
	"https://www.youtube.com/watch?v=a6KaaUI6Zag&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=28",
	"https://www.youtube.com/watch?v=BtlhRZZBKS0&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=29",
	"https://www.youtube.com/watch?v=DX7X2gLYAlg&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=30",
	"https://www.youtube.com/watch?v=vuzJPY6BTQ4&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=31",
	"https://www.youtube.com/watch?v=oZQ3GCFHiMs&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=32",
	"https://www.youtube.com/watch?v=gVMD8ulMzLE&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=33",
	"https://www.youtube.com/watch?v=c53QC2eWzIk&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=34",
	"https://www.youtube.com/watch?v=B3eYEdnIxqE&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=35",
	"https://www.youtube.com/watch?v=-t67r1tFRjE&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=36",
	"https://www.youtube.com/watch?v=HydUsOrM8Gs&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=37",
	"https://www.youtube.com/watch?v=38aOIDwVy2A&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=38",
	"https://www.youtube.com/watch?v=D6UqgINWM3s&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=39",
	"https://www.youtube.com/watch?v=uA-XixQCSBg&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=40",
	"https://www.youtube.com/watch?v=0lgoebtgx18&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=41",
	"https://www.youtube.com/watch?v=jAIFsLgSJSI&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=42",
	"https://www.youtube.com/watch?v=vri_sknGXLc&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=43",
	"https://www.youtube.com/watch?v=qR9I9uOLcUA&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=44",
	"https://www.youtube.com/watch?v=JdezsRsd7zU&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=45",
	"https://www.youtube.com/watch?v=pdFiCZ2tHw4&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=46",
	"https://www.youtube.com/watch?v=fyBvD9FEgTM&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=47",
	"https://www.youtube.com/watch?v=3TcwNl1GG9w&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=48",
	"https://www.youtube.com/watch?v=5qzOx_V8ZmI&list=PLkvG4EWPDB0kkjJ-RBHMFdCLDFzn5UNlJ&index=49"
]

if __name__ == "__main__":
	for link in videos:
		download(link)
