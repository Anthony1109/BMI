height = input('請輸入你的身高(cm)')
weight = input('請輸入你的體重(kg)')
height = int(height)
weight = int(weight)
height = height/100
BMI = weight/height/height
if BMI < 18.5:
    print('BMI值為', BMI, '你的體重過輕囉! 討厭的瘦子')
elif 18.5 <= BMI < 24:
    print('BMI值為', BMI, '你的體重在正常範圍!')
elif 24 <= BMI < 27:
	print('BMI值為', BMI, '你的體重過重囉! 驕傲的小胖子')
elif 27 <= BMI <30:
	print('BMI值為', BMI, '你輕度肥胖囉! 驕傲的中胖子')
elif 30 <= BMI <35:
	print('BMI值為', BMI, '你中度肥胖囉! 驕傲的大胖子')
elif BMI >= 35:
	print('BMI值為', BMI, '你重度肥胖囉! 討厭的死胖子')
