import sys
import os
from PIL import Image
 
txt = 'MaidakeCTF{We_can_hide_various_things_in_the_image}!'
 
#元画像を開く
img = Image.open("fire.jpg")
rgba_img = img.convert('RGBA')
size = rgba_img.size
result = Image.new('RGBA',size)
result.paste(rgba_img, (0, 0))
 
flag = False
cnt = 0
for y in range(size[1]):
	for x in range(size[0]):
 
		r,g,b,a = rgba_img.getpixel((x,y))
		r = r // 4 * 4
		g = g // 5 * 5
		b = b // 5 * 5
 
		get_ord = ord(txt[cnt])
		#Rの処理
		# 空白 . ? 数字 a ~ l
		if get_ord == 32 or get_ord == 46 or get_ord == 63 \
			or (get_ord >= 48 and get_ord <= 57) \
			or (get_ord >= 97 and get_ord <= 108):
			r += 1
		# m ~ z , A ~ K
		elif (get_ord >= 109 and get_ord <= 122) \
			or (get_ord >= 65 and get_ord <= 75):
			r += 2

 		# L ~ Z , [\]^_`{|}!
		elif (get_ord >= 76 and get_ord <= 90) \
			or (get_ord >= 91 and get_ord <= 96) \
			or (get_ord >= 123 and get_ord <= 125) \
			or get_ord == 33:
			r += 3

		#Gの処理
		# 2~6 , r~v , Q~U
		if (get_ord >= 50 and get_ord <= 54) \
			or (get_ord >= 81 and get_ord <= 85) \
			or (get_ord >= 114 and get_ord <= 118):
			g += 1
		# 7~9 , a~b , w~z , A , V~Z
		elif (get_ord >= 55 and get_ord <= 57) \
			or get_ord == 65 or get_ord == 97 or get_ord == 98 \
			or (get_ord >= 119 and get_ord <= 122) \
			or (get_ord >= 86 and get_ord <= 90):
			g += 2
		# c~g , B~F , [\]^_
		elif (get_ord >= 99 and get_ord <= 103) \
			or (get_ord >= 119 and get_ord <= 122) \
			or (get_ord >= 66 and get_ord <= 70) \
			or (get_ord >= 91 and get_ord <= 95):
			g += 3
		# h~l , G~K , `{|}~
		elif (get_ord >= 104 and get_ord <= 108) \
			or (get_ord >= 71 and get_ord <= 75) \
			or (get_ord >= 123 and get_ord <= 125) \
			or get_ord == 96 or get_ord == 33:
			g += 4
 
		#Bの処理
		if r % 4 == 1:
			# .
			if get_ord == 46: b += 1
			# ?
			elif get_ord == 63:b += 2
			# 数字
			elif (get_ord >= 48 and get_ord <= 57):
				b += (get_ord - 45) % 5
			# a ~ l
			elif (get_ord >= 97 and get_ord <= 108):
				b += (get_ord - 94) % 5
		elif r % 4 == 2:
			# m ~ z
			if get_ord >= 109 and get_ord <= 122:
				b += (get_ord - 104) % 5
			# A ~ K
			elif get_ord >= 65 and get_ord <= 75:
				b += (get_ord - 61) % 5
		elif r % 4 == 3:
			# L ~ Z
			if get_ord >= 76 and get_ord <= 96:
				b += (get_ord - 71) % 5
			elif get_ord >= 123 and get_ord <= 125:
				b += (get_ord - 122) % 5
			elif get_ord == 33:
				b += 4
 
		result.putpixel((x,y),(r,g,b,a))
		#終了処理
		if cnt == len(txt) - 1 or (r % 4 == 3 and g % 5 == 4 and b % 5 == 4):
			flag = True
			break
 
		if cnt < len(txt) - 1:
			cnt += 1
 
	if flag:
		break
 
#画像の出力
result.save('flag.png')