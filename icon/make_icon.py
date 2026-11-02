from PIL import Image, ImageDraw, ImageFont
import glob,sys
S=1024
im=Image.new('RGBA',(S,S),(0,0,0,0))
d=ImageDraw.Draw(im)
d.rounded_rectangle((32,32,S-32,S-32),radius=200,fill=(17,24,39,255))
# film strip: sprocket holes left and right
for i in range(5):
    y=150+i*150
    d.rounded_rectangle((70,y,130,y+80),radius=14,fill=(55,65,81,255))
    d.rounded_rectangle((S-130,y,S-70,y+80),radius=14,fill=(55,65,81,255))
# frame
d.rounded_rectangle((190,190,S-190,640),radius=60,fill=(37,99,235,255))
# play triangle
d.polygon([(450,300),(450,530),(650,415)],fill=(255,255,255,255))
# text GIF
fp=None
for c in glob.glob('/usr/share/fonts/**/*.ttf',recursive=True):
    n=c.lower()
    if 'bold' in n and ('dejavusans' in n or 'liberationsans' in n) and 'oblique' not in n and 'italic' not in n and 'mono' not in n and 'condensed' not in n:
        fp=c;break
print('font',fp)
f=ImageFont.truetype(fp,230) if fp else ImageFont.load_default()
tw=d.textlength('GIF',font=f)
d.text(((S-tw)/2,690),'GIF',font=f,fill=(255,255,255,255))
im.save('icon_1024.png')
im.resize((512,512),Image.LANCZOS).save('app/icon.png')
sizes=[16,24,32,48,64,128,256]
im.resize((256,256),Image.LANCZOS).save('app/icon.ico',sizes=[(s,s) for s in sizes])
print('ok')
