# Filename: auto_vigenere.py
# Coding: utf8
# 用于破解足够长的 Vigenere 密文
# 密钥长度只能支持十位
# 直接选取最大密钥长度


#cipher = "OCWYIKOOONIWUGPMXWKTZDWGTSSAYJZWYEMDLBNQAAAVSUWDVBRFLAUPLOOUBFGQHGCSCMGZLATOEDCSDEIDPBHTMUOVPIEKIFPIMFNOAMVLPQFXEJSMXMPGKCCAYKWFZPYUAVTELWHRHMWKBBNGTGUVTEFJLODFEFKVPXSGRSORVGTAJBSAUHZRZALKWUOWHGEDEFNSWMRCIWCPAAAVOGPDNFPKTDBALSISURLNPSJYEATCUCEESOHHDARKHWOTIKBROQRDFMZGHGUCEBVGWCDQXGPBGQWLPBDAYLOOQDMUHBDQGMYWEUIK"
cipher = "ktbueluegvitnthuexmonveggmrcgxptlyhhjaogchoemqchpdnetxupbqntietiabpsmaoncnwvoutiugtagmmqsxtvxaoniiogtagmbpsmtuvvihpstpdvcrxhokvhxotawswquunewcgxptlcrxtevtubvewcnwwsxfsnptswtagakvoyyak"

def get_key_len(s):
	# 获取密钥长度 即最大重合度
	# 假设密钥不超过10位
	overlap = []
	for i in range(1, 16):
		count = 0
		for j in range(len(s)):
			if s[j] == s[(i + j) % len(s)]: # 模运算保证越界后从头开始
				count = count + 1
		overlap.append(count)
	return(int(overlap.index(max(overlap))) + 1)

def frequency_analysis(key_len, s):
	# 进行频率分析 并确定密钥
	# 运用重合指数法 与标准重合指数 与0.065尽可能接近
	key = [] # 存放密钥
	dataset = [] # 暂时存放某个分组
	Standard = {'A':0.08167,'B':0.01492,'C':0.02782,'D':0.04253,'E':0.12702,'F':0.02228,'G':0.02015,'H':0.06094,'I':0.06966,'J':0.00153,'K':0.00772,'L':0.04025,'M':0.02406,'N':0.06749,'O':0.07507,'P':0.01929,'Q':0.00095,'R':0.05987,'S':0.06327,'T':0.09056,'U':0.02758,'V':0.00978,'W':0.02360,'X':0.00150,'Y':0.01974,'Z':0.00074}
	for i in range(key_len):
		dataset = []
		overSumSet = []
		for j in range(i, len(s), key_len):
			dataset.append(s[j])
		for dif in range(26): # 位移位数 
			oper_data = []
			overSum = 0 # 重合指数
			for j in dataset:
				oper_data.append(chr((ord(j) + dif - 65) % 26 + 65)) # 位移后的新串 要注意是否越界
			for let_index in range(26): # 统计每个字母重合指数 
				let = chr(let_index + 65)
				pi = Standard[let] # 自然语言字母频率
				fi = oper_data.count(let) # 字母在该该子串的频率
				sub_sum = pi * fi / len(oper_data) 
				overSum = overSum + sub_sum
			if overSum > 0.065:
				overSumSet.append(overSum - 0.065)
			else:
				overSumSet.append(0.065 - overSum)
		key.append(overSumSet.index(min(overSumSet)))
	return(key)

def cipher_to_plain(cipher, key):
	# 将密文转换为明文
	final_plain = ""
	for i in range(len(cipher)):
		initial_index = int(ord(cipher[i]) + int(key[i % len(key)]))
		result_index = (initial_index - 65) % 26 + 65 # 防止字母越界 
		final_plain = final_plain + chr(result_index) # 注意这里不能越界
	return(final_plain)


# 对于密文处理 全部置为大写
cipher = cipher.upper()
# 找出最可能的密钥长度
key_len = get_key_len(cipher)
# 分组后进行频率分析
key = frequency_analysis(key_len, cipher)
# 翻译密钥
key_word = ""
for i in key:
	key_word = key_word + chr((26 - i) % 26 + 65) # 注意不要越界
print("该密钥为：")
print(key_word)
# 译码
plain = cipher_to_plain(cipher, key)
result = plain
print("破译结果为:\n" + result)