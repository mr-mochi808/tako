import sys
from PIL import Image
P={
 # octopus
 'p':'#E86A88','l':'#F7A3B8','d':'#C2486A','D':'#7E2645','s':'#FBD0DB',
 'w':'#FFFFFF','k':'#1F1B2E',
 # crab
 'r':'#E9573F','o':'#F79478','R':'#B23A26','Q':'#6E1F14',
 # gull
 'W':'#F4F6FA','g':'#C3CAD8','G':'#7D879C','H':'#3E4557','a':'#F5A623','A':'#B86E0F',
 # hermit shell
 'm':'#CDA8EA','n':'#9A72C4','N':'#5B3E85',
 # duck
 'y':'#FFD84D','Y':'#E0A82A','Z':'#8A6110','b':'#F59A23','B':'#A85A0B',
 # tree
 'f':'#3F9A4C','h':'#68C063','F':'#2B6E37','T':'#1C4A25','t':'#8A5A33','u':'#5A3820','e':'#E8505B','E':'#9E2F38',
}
def mirror(half, center_dup=False):
    rows=[]
    for r in half:
        rows.append(r + (r[::-1] if center_dup else r[-2::-1]))
    return rows
S={}
S['octo']=mirror([
"........DDD",
"......DDppp",
".....Dplllp",
"....Dplllpp",
"....Dpllppp",
"...Dppppppp",
"...Dppppppp",
"...Dpwwwppp",
"...Dpwkwppp",
"...Dpwkkppp",
"....Dpppppp",
"....Ddppppp",
"...DDDdpppp",
"..DpdDpdDpd",
".DpsDDpsDps",
".DpdD.DpdDp",
"DpsD..DpsDp",
"DpdD..DpdDp",
"DpsD...DpsD",
".DpD...DpdD",
"..DD....DpD",
".........D.",
], center_dup=True)
S['crab']=mirror([
"QQQ....",
"QroQ...",
"QrrQ...",
".QrQ..Q",
"..QRQ.Q",
"...QrQQ",
"..QrrrrQ",
".QrwkrrrQ",
], center_dup=False)
# crab drawn explicitly (simpler than mirror)
S['crab']=[
"QQQ........QQQ",
"QroQ......QorQ",
"QrrQ......QrrQ",
".QrQ.Q..Q.QrQ.",
"..QRQQ..QQRQ..",
"...QQrrrrQQ...",
"..QrrwkrwkrrQ.",
".QrrrrrrrrrrrQ",
".QoorrrrrrrooQ",
".QRrrrrrrrrrRQ",
"..QRRRRRRRRQ..",
".Q.Q.Q..Q.Q.Q.",
]
S['gull']=[
"HHH............HHH",
"HggHH........HHggH",
".HgggHH.HHH.HHgggH",
"..HGggHHWWWHHggGH.",
"...HGGHWWkWWHGGH..",
"....HHWWWWWWaaAH..",
"......HWWWWWHHH...",
".......HHHHH......",
]
S['hermit']=[
"....NNNNN.....",
"...NmmnmmN....",
"..NmnNNnmmN...",
".NmmNmmNnmmN..",
".NnmNnNNmmnN..",
"NmmnmmmmmnmmN.",
"NnmmnmmmnmmnN.",
"QQQNNNNNNNNNN.",
"QrwkQ.........",
"QrrrrQ........",
"QroorrQ.......",
".Q.Q.Q........",
]
S['duck']=[
"......ZZZZ....",
".....ZyyyyZ...",
".....ZyykyZBB.",
".....ZyyyyZbbB",
"......ZyyZ.BB.",
"ZZ....ZyyZ....",
"ZyZZZZyyyyZ...",
"ZyyyyyyyyyyZ..",
"ZYyyyyyyyyyZ..",
".ZYyyyyyyyYZ..",
"..ZZYYYYYZZ...",
"....BZ.BZ.....",
"....BB.BB.....",
]
S['tree']=[
"......TTTTTTTT......",
"....TTffhhhhffTT....",
"...TfffhhhhffffeT...",
"..TffhhfffffffeET...",
".TfeffffffhhffffFT..",
".TfEfhhffffhhffffT..",
"TffffhhfffffffeffFT.",
"TfffffffffeffffEFFT.",
"TFfffhhfffEfffffFFT.",
".TFfffffffffffFFFT..",
".TFFFffffeffFFFFFT..",
"..TTFFFFFEFFFFFTT...",
"....TTTTTTTTTTT.....",
"........utu.........",
"........ttu.........",
"........ttu.........",
".......uttu.........",
"......utttuu........",
]
S['food']=[
".QQQ.",
"QrooQ",
"QRrrQ",
".QQQ.",
]
S['fruit']=[
"..F.",
".EeE",
"EeeE",
".EE.",
]
def png(name,rows,scale=8):
    w=max(len(r) for r in rows); h=len(rows)
    im=Image.new('RGBA',(w,h),(0,0,0,0))
    for y,r in enumerate(rows):
        for x,c in enumerate(r):
            if c in P:
                v=P[c].lstrip('#'); im.putpixel((x,y),tuple(int(v[i:i+2],16) for i in (0,2,4))+(255,))
    return im.resize((w*scale,h*scale),Image.NEAREST)
if __name__=='__main__':
    ims=[png(k,v) for k,v in S.items()]
    W=sum(i.width for i in ims)+20*len(ims); H=max(i.height for i in ims)+20
    sheet=Image.new('RGBA',(W,H),(242,212,155,255)); x=10
    for i in ims: sheet.paste(i,(x,10),i); x+=i.width+20
    sheet.save('sheet.png')
