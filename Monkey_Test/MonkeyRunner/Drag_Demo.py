#encoding:utf-8
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
import random
''' 模擬手機APP上下滑動'''

# 取得裝置設定
device = MonkeyRunner.waitForConnection()
result = device.shell('dumpsys activity | grep mFocusedActivity')

LoginActivity = 'com.any-company.productAPP/.login.LoginActivity')
device.startActivity(component=LoginActivity)

# 登入
def login(device):
	print( ' long function ')
	
	result = device.shell('dumpsys activity | grep mFocusedActivity')	
	
	if( '.login.LoginActivity' in result ):
		''' Execute login '''
		
	else	
		''' Do Nothing '''
		print(' Do Nothing ')

# Drage Test
#模擬滑動
#device.drag(X,Y,D,S)
#X 開始坐標
#Y 結束坐標
#D 拖動持續時間(以秒為單位)，默認1.0秒
#S 插值點時要採取的步驟。默認值是10

print('Drag Test ')
x =  500
y =  800
x2 = x
y2 = y + 700

# 模擬 上 下 滑動
device.drag((x,y),(x2,y2),1,20)
MonkeyRunner.sleep(1)
device.drag((x2,y2),(x,y),1,20)
MonkeyRunner.sleep(3)
