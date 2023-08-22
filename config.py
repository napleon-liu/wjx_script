base_url='https://www.wjx.cn/vm/riVDodY.aspx'   #问卷地址
path =  'chromedriver.exe'     # 驱动目录。这里的驱动版本是114，我测试用的浏览器版本是115。根据自己电脑上chrome浏览器的版本选择下载对应的版本驱动替换
#下载地址：https://registry.npmmirror.com/binary.html?path=chromedriver/
max_num=15      #题目数量
loop_time=1024     #循环次数
#auto_choose()里的choose_click(browser,type,num,questions,weights)要根据不同的题目来添加修改
#browser默认；type是题目类型，3为单选，4为多选；num为题目序号；questions为题目选项个数；weights为每个选项的权重