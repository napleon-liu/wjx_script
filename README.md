# wjx_auto(问卷星自动填写)
**文档更新时间(2023/8/14)**
>
>模拟selenium浏览器打开问卷星网址，模拟点击选项，提交
>
>仅支持**单选**和**多选**和**填空**
>
>支持选项权重

# 使用说明
>
>1.确保目录下的chromedriver.exe版本和chrome浏览器版本一致（或相差一个版本）。
当前驱动版本:116
>[驱动下载地址](https://registry.npmmirror.com/binary.html?path=chromedriver/)
>
>2.修改config.py里的参数。
>
>>  base_url为问卷地址
>> 
>>  max_num为题目数量
>> 
>>  loop_time为想要刷取的次数
>
>3.根据问卷内容，修改main.py中的auto_choose()里的choose_click(browser,type,num,questions,weights)
>>browser默认；
>>
>>type是题目类型，2为填空，3为单选，4为多选；
>>
>>num为题目序号；
>>
>>questions为题目选项个数；
>>
>>weights为每个选项的权重, 格式为 [ ]
