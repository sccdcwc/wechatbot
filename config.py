import configparser

# 读取配置文件
cf = configparser.ConfigParser()
cf.read("./conf.ini", encoding='UTF-8')

# 设置女友的微信名称，记住，不是微信ID也不是微信备注
# 你女友的微信名称，记住，不是微信ID也不是微信备注
group_name = cf.get("configuration", "group_name")

# 设置早上起床时间，中午吃饭时间，下午吃饭时间，晚上睡觉时间
say_good_morning = cf.get("configuration", "say_good_morning")
# say_good_lunch = cf.get("configuration", "say_good_lunch")
say_good_dinner = cf.get("configuration", "say_good_dinner")
say_good_dream = cf.get("configuration", "say_good_dream")

# # 设置女友生日信息
# # 几月，注意补全数字，为两位数，比如6月必须写成06
# birthday_month = cf.get("configuration", "birthday_month")
# # 几号，注意补全数字，为两位数，比如6号必须写成08
# birthday_day = cf.get("configuration", "birthday_day")
#
# # 读取早上起床时间，中午吃饭时间，下午吃饭时间，晚上睡觉时间的随机提示语
# # 一般这里的代码不要改动，需要增加提示语可以自己打开对应的文件修改
# # 早上起床问候语列表，数据来源于新浪微博
# str_list_good_morning = ''
# with open("./remind_sentence/sentence_good_morning.txt", "r", encoding='UTF-8') as f:
#     str_list_good_morning = f.readlines()
# print(str_list_good_morning)
#
# # 中午吃饭问候语列表，数据来源于新浪微博
# str_list_good_lunch = ''
# with open("./remind_sentence/sentence_good_lunch.txt", "r", encoding='UTF-8') as f:
#     str_list_good_lunch = f.readlines()
# print(str_list_good_lunch)
#
# # 晚上吃饭问候语列表，数据来源于新浪微博
# str_list_good_dinner = ''
# with open("./remind_sentence/sentence_good_dinner.txt", "r", encoding='UTF-8') as f:
#     str_list_good_dinner = f.readlines()
# print(str_list_good_dinner)

# # 晚上睡觉问候语列表，数据来源于新浪微博
# str_list_good_dream = ''
# with open("./remind_sentence/sentence_good_dream.txt", "r", encoding='UTF-8') as f:
#     str_list_good_dream = f.readlines()
# print(str_list_good_dream)
#
# # 设置晚上睡觉问候语是否在原来的基础上再加上每日学英语精句
# # False表示否 True表示是

if ((cf.get("configuration", "flag_learn_english")) == '1'):
    flag_learn_english = True
else:
    flag_learn_english = False
print(flag_learn_english)

# # 设置所有问候语结束是否加上表情符号
# # False表示否 True表示是
# str_emoj = "(•‾̑⌣‾̑•)✧˖°----(๑´ڡ`๑)----(๑¯ิε ¯ิ๑)----(๑•́ ₃ •̀๑)----( ∙̆ .̯ ∙̆ )----(๑˘ ˘๑)----(●′ω`●)----(●･̆⍛･̆●)----ಥ_ಥ----_(:qゝ∠)----(´；ω；`)----( `)3')----Σ((( つ•̀ω•́)つ----╰(*´︶`*)╯----( ´´ิ∀´ิ` )----(´∩｀。)----( ื▿ ื)----(｡ŏ_ŏ)----( •ิ _ •ิ )----ヽ(*΄◞ิ౪◟ิ‵ *)----( ˘ ³˘)----(; ´_ゝ`)----(*ˉ﹃ˉ)----(◍'౪`◍)ﾉﾞ----(｡◝‿◜｡)----(ಠ .̫.̫ ಠ)----(´◞⊖◟`)----(。≖ˇェˇ≖｡)----(◕ܫ◕)----(｀◕‸◕´+)----(▼ _ ▼)----( ◉ืൠ◉ื)----ㄟ(◑‿◐ )ㄏ----(●'◡'●)ﾉ♥----(｡◕ˇ∀ˇ◕）----( ◔ ڼ ◔ )----( ´◔ ‸◔`)----(☍﹏⁰)----(♥◠‿◠)----ლ(╹◡╹ლ )----(๑꒪◞౪◟꒪๑)"
# str_list_emoj = str_emoj.split('----')
# if ((cf.get("configuration", "flag_wx_emoj")) == '1'):
#     flag_wx_emoj = True
# else:
#     flag_wx_emoj = False
# print(str_list_emoj)
#
#     # 设置节日祝福语
#     # 情人节祝福语
# str_Valentine = cf.get("configuration", "str_Valentine")
# print(str_Valentine)
#
#     # 三八妇女节祝福语
# str_Women = cf.get("configuration", "str_Women")
# print(str_Women)
#
# # 平安夜祝福语
# str_Christmas_Eve = cf.get("configuration", "str_Christmas_Eve")
# print(str_Christmas_Eve)
#
# # 圣诞节祝福语
# str_Christmas = cf.get("configuration", "str_Christmas")
# print(str_Christmas)
