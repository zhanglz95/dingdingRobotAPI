from dingRobot import DingRobot

# 这里填webhook
url = 'https://oapi.dingtalk.com/robot/send?access_token=xxx'
# 这里填签名密钥
secret = 'xxx'
# 初始化机器人
dingRobot = DingRobot(url, secret)

# 发送markdown
dingRobot.sendMd(
    title="测试Markdown", 
    md="#### 测试"
    )

# 发送Link
dingRobot.sendLink(title="张氏家族崛起", text="具体人员有：张烈卓、张娟、张学龙...", msgUrl="https://www.baidu.com")

# 发送基本信息
dingRobot.sendText("测试", at=['15623059510'])