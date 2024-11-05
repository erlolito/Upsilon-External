from PIL import Image

def q(a):
	e=[hex(i)[2:] for i in a]
	for i in range(len(e)):
		while len(e[i])!=2:e[i]='0'+e[i]
	s=int(''.join(e),16)
	r=hex(((s&0xF80000)>>8)|((s&0x00FC00)>>5)|((s&0x0000F8)>>3))
	while len(r)!=6:
		r=r[:2]+'0'+r[2:]
	return r
a=Image.open('img.jpg')

print('const unsigned int img_len='+str(a.height*a.width)+';\nconst uint16_t img[]={',end='',file=open('img.h','a'))
print(a.height,a.width)
for i in range(a.height):
	for j in range(a.width):print(q(a.getpixel((j,i))),end=',',file=open('img.h','a'))
print('};',end='',file=open('img.h','a'))