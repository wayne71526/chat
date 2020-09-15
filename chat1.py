# 讀取檔案
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			chat.append(line.strip().split(' '))
	return chat

# 對話計數分析			
def count(chat):
	Allen_word_count = 0
	Allen_sticker_count = 0
	Allen_image_count = 0
	Viki_word_count = 0
	Viki_sticker_count = 0
	Viki_image_count = 0
	for s in chat:
		time = s[0]
		name = s[1]
		if name == 'Allen': # -2 表示倒數第二個
			if s[2] == '貼圖':
				Allen_sticker_count += 1
			elif s[2] == '圖片':
				Allen_image_count += 1
			else:
				for line in s[2:]: # s[起始值, 最終值] 包含起始值 不包含最終值
					Allen_word_count += len(line)
		elif name == 'Viki':
			if s[2] == '貼圖':
				Viki_sticker_count += 1
			elif s[2] == '圖片':
				Viki_image_count += 1	
			else:
				for line in s[2:]:
					Viki_word_count += len(line)
	print('Allen說了', Allen_word_count, '個字')	
	print('Allen傳了', Allen_sticker_count, '張貼圖')
	print('Allen傳了', Allen_image_count, '張圖片')
	print('Viki說了', Viki_word_count, '個字')	
	print('Viki傳了', Viki_sticker_count, '張貼圖')
	print('Viki傳了', Viki_image_count, '張貼圖')


def main():
	chat = read_file('LINE-Viki.txt')
	count(chat)
	

main()	
