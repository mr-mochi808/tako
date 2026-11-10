from sprites2 import S,P,png
from PIL import Image
S['shell']=[
"....QQQQQQ....",
"..QQrrooorQQ..",
".QrrooorrrrrQ.",
"QRrrrrrrrrrRRQ",
"QQRRRRRRRRRRQQ",
]
S['bill']=[
"BBBBBB",
"BbbbbB",
".BbbB.",
]
S['claw']=[
"QQQ.QQ",
"QroQorQ",
"QrrQQrQ",
"QRrrrRQ",
".QRRRQ.",
"..QrQ..",
]
S['legs']=[
"Q..........Q",
".Q........Q.",
"QrQ......QrQ",
]
def compose():
    base=png('octo',S['octo'],1).copy()
    canvas=Image.new('RGBA',(30,26),(0,0,0,0))
    canvas.paste(base,(4,2),base)
    for k,(x,y) in {'shell':(8,0),'bill':(12,12),'claw':(22,13),'legs':(9,22)}.items():
        im=png(k,S[k],1); canvas.paste(im,(x,y),im)
    return canvas
if __name__=='__main__':
    c=compose().resize((240,208),Image.NEAREST)
    bg=Image.new('RGBA',c.size,(242,212,155,255)); bg.paste(c,(0,0),c); bg.save('crabtopus.png')
