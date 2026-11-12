from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
import arabic_reshaper
from bidi.algorithm import get_display

W,H=1080,1350
im=Image.new("RGB",(W,H))
pix=im.load()
for y in range(H):
    t=y/H
    c=(int(8+13*t),int(45+22*t),int(58+15*t))
    for x in range(W): pix[x,y]=c
d=ImageDraw.Draw(im)
gold=(223,190,125)
cream=(250,244,225)
teal=(30,110,111)
for i in range(7):
    margin=40+i*12
    d.rounded_rectangle((margin,margin,W-margin,H-margin),radius=45,outline=(36+i*5,91+i*4,92+i*3),width=2)
d.ellipse((220,95,860,735),outline=gold,width=5)
d.arc((260,125,820,695),180,360,fill=(116,152,138),width=4)
d.ellipse((520,190,750,420),fill=gold)
d.ellipse((560,160,790,390),fill=(13,57,65))
# stylized mosque silhouette
d.rectangle((240,600,840,850),fill=(11,35,46))
d.pieslice((310,445,770,790),180,360,fill=(11,35,46))
for x in (190,835):
    d.rectangle((x,460,x+55,850),fill=(11,35,46))
    d.polygon([(x-12,460),(x+28,370),(x+68,460)],fill=(11,35,46))
d.line((120,875,960,875),fill=gold,width=4)
font_ar="/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf"
font_en="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def f(path,size):return ImageFont.truetype(path,size)
def ar(s):return get_display(arabic_reshaper.reshape(s))
def center(s,y,font,fill):
    b=d.textbbox((0,0),s,font=font)
    d.text(((W-(b[2]-b[0]))/2,y),s,font=font,fill=fill,stroke_width=0)
center(ar("جمعة مباركة"),900,f(font_ar,104),cream)
center("Wishing you a blessed",1070,f(font_en,37),cream)
center("and peaceful Friday",1125,f(font_en,37),cream)
d.line((300,1210,780,1210),fill=gold,width=2)
center("ClinicWell",1245,f(font_en,36),gold)
out=Path("posts/clinicwell-friday-rendered-1080x1350.png")
out.parent.mkdir(parents=True,exist_ok=True)
im.save(out,optimize=True)
print(out, out.stat().st_size)
