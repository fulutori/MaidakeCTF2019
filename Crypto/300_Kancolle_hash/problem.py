#coding: utf-8
import hashlib
from FLAG import FLAG

kancolle_server = ['横須賀鎮守府','呉鎮守府','佐世保鎮守府','舞鶴鎮守府','大湊警備府','トラック泊地','リンガ泊地','ラバウル基地','ショートランド泊地','ブイン基地','タウイタウイ泊地','パラオ泊地','ブルネイ泊地','単冠湾泊地','幌筵泊地','宿毛湾泊地','鹿屋基地','岩川基地','佐伯湾泊地','柱島泊地']
md5_server = [hashlib.md5(server.encode()).hexdigest() for server in kancolle_server]

key = 0
for md5 in md5_server:
	for moji in md5:
		key += ord(moji)

enc_flag = ''
amari_list = []
for moji in FLAG:
	to_ord = key // ord(moji)
	enc_flag += chr(to_ord)

with open('result.txt', 'w') as f:
	f.write(enc_flag)
