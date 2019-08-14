from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse

context = {'list':  [
    {
        "price": "639.00",
        "postal": "True",
        "title": "春季<font class=\"hl\">女装</font>V领套头羊绒针织衫 马甲毛衣背心",
        "shopNick": "shiningcrown女装旗舰店",
        "payNum": "6人付款"
    },
    {
        "price": "79.00",
        "postal": "True",
        "title": "夏季连衣裙V领T恤衬衫中年大码<font class=\"hl\">女装</font>妈妈装",
        "shopNick": "美壹度祺舰店",
        "payNum": "11人付款"
    },
    {
        "price": "575.00",
        "postal": "True",
        "title": "英国代购直邮COS SLEEVELESS",
        "shopNick": "lhjfish",
        "payNum": "0人付款"
    },
    {
        "price": "389.00",
        "postal": "True",
        "title": "春季新款女V领套头百搭羊绒针织衫 打底毛衣",
        "shopNick": "shiningcrown女装旗舰店",
        "payNum": "2人付款"
    },
    {
        "price": "79.00",
        "postal": "True",
        "title": "休闲套装女夏季2019新款时尚韩版大码运",
        "shopNick": "y8765432119818400",
        "payNum": "155人付款"
    },
    {
        "price": "19.90",
        "postal": "True",
        "title": "胖妹妹加肥加大码<font class=\"hl\">女装</font>宽松休闲运动套装女学",
        "shopNick": "兰格格丽人坊",
        "payNum": "580人付款"
    },
    {
        "price": "459.00",
        "postal": "True",
        "title": "欧洲站秋款欧货2019<font class=\"hl\">女装</font>新款潮阔腿裤套装女",
        "shopNick": "lilybaby125",
        "payNum": "0人付款"
    },
    {
        "price": "119.50",
        "postal": "True",
        "title": "<font class=\"hl\">女装</font>2019新款chic减龄学院风智熏裙",
        "shopNick": "xixi152103",
        "payNum": "2人付款"
    },
    {
        "price": "82.60",
        "postal": "True",
        "title": "be yourself潮牌 秋季<font class=\"hl\">女装</font>20",
        "shopNick": "yubin_i",
        "payNum": "0人付款"
    },
    {
        "price": "58.00",
        "postal": "True",
        "title": "2019夏新款职业装<font class=\"hl\">女装</font>白色衬衫短袖时尚",
        "shopNick": "秋风落叶13553896596",
        "payNum": "5人付款"
    },
    {
        "price": "93.80",
        "postal": "True",
        "title": "秋季<font class=\"hl\">女装</font>2019新款潮 原宿bf条纹长袖",
        "shopNick": "yubin_i",
        "payNum": "3人付款"
    },
    {
        "price": "105.00",
        "postal": "True",
        "title": "2019韩国夏装新款气质很仙小个子白色方",
        "shopNick": "海角淘衣",
        "payNum": "479人付款"
    },
    {
        "price": "19.90",
        "postal": "True",
        "title": "2019早春<font class=\"hl\">女装</font>韩版上衣chic紧身显瘦",
        "shopNick": "半瞳萍子",
        "payNum": "0人付款"
    },
    {
        "price": "69.00",
        "postal": "True",
        "title": "2019秋装新款蕾丝上衣<font class=\"hl\">女装</font>宽松大码长袖",
        "shopNick": "元素衣阁",
        "payNum": "17人付款"
    },
    {
        "price": "429.00",
        "postal": "True",
        "title": "LOFTSHINE珞炫潮牌<font class=\"hl\">女装</font>2019秋",
        "shopNick": "loftshine旗舰店",
        "payNum": "53人付款"
    },
    {
        "price": "138.00",
        "postal": "True",
        "title": "欧规则春夏<font class=\"hl\">女装</font>格纹针织衫女套头圆领宽松显",
        "shopNick": "欧规则服饰旗舰店",
        "payNum": "2人付款"
    },
    {
        "price": "93.20",
        "postal": "False",
        "title": "尾货清仓<font class=\"hl\">女装</font> 品牌2019夏季新款重工真",
        "shopNick": "尚园fashion",
        "payNum": "1人付款"
    },
    {
        "price": "218.00",
        "postal": "True",
        "title": "民族复古刺绣减龄背带长裙",
        "shopNick": "义玲相依",
        "payNum": "109人付款"
    },
    {
        "price": "29.90",
        "postal": "True",
        "title": "欧洲站<font class=\"hl\">女装</font>欧货潮2019新款内搭宽松白色",
        "shopNick": "天迅网",
        "payNum": "2人付款"
    },
    {
        "price": "69.00",
        "postal": "True",
        "title": "衬衫<font class=\"hl\">女装</font>秋2019新款娃娃领上衣波点雪纺",
        "shopNick": "时尚魅力早班车",
        "payNum": "0人付款"
    },
    {
        "price": "388.00",
        "postal": "False",
        "title": "2019春装新款高端气质<font class=\"hl\">女装</font>欧美大牌中长",
        "shopNick": "yan86fu",
        "payNum": "57人付款"
    },
    {
        "price": "218.00",
        "postal": "True",
        "title": "<font class=\"hl\">女装</font>2019新款潮韩版职场简约性冷淡in",
        "shopNick": "服饰批发零售",
        "payNum": "0人付款"
    },
    {
        "price": "259.00",
        "postal": "True",
        "title": "2019新款秋装不规则下摆<font class=\"hl\">女装</font>宽松设计感",
        "shopNick": "seven_ing",
        "payNum": "0人付款"
    },
    {
        "price": "199.00",
        "postal": "True",
        "title": "system9家19韩国东大门代购<font class=\"hl\">女装</font>夏",
        "shopNick": "mayrain8",
        "payNum": "0人付款"
    },
    {
        "price": "120.00",
        "postal": "False",
        "title": "2019年新款夏季秋季<font class=\"hl\">女装</font>大码可爱街头潮",
        "shopNick": "wttbifa8505",
        "payNum": "0人付款"
    },
    {
        "price": "369.00",
        "postal": "True",
        "title": "LOFTSHINE珞炫潮牌<font class=\"hl\">女装</font>2019秋",
        "shopNick": "loftshine旗舰店",
        "payNum": "18人付款"
    },
    {
        "price": "146.25",
        "postal": "True",
        "title": "风衣女中长款2019秋<font class=\"hl\">女装</font>新款韩版长袖连",
        "shopNick": "zy15155353884",
        "payNum": "1人付款"
    },
    {
        "price": "120.00",
        "postal": "True",
        "title": "2019夏季新品<font class=\"hl\">女装</font>西装领双排扣大长腿高",
        "shopNick": "t_1506590758661_0993",
        "payNum": "0人付款"
    },
    {
        "price": "62.00",
        "postal": "True",
        "title": "辰辰妈婴童装宝宝夏季儿童洋气<font class=\"hl\">女装</font>蕾丝花边",
        "shopNick": "tb4887553_2012",
        "payNum": "93人付款"
    },
    {
        "price": "117.00",
        "postal": "True",
        "title": "2019秋季新款<font class=\"hl\">女装</font>韩版长袖休闲翻领单排",
        "shopNick": "zy15155353884",
        "payNum": "0人付款"
    },
    {
        "price": "208.00",
        "postal": "True",
        "title": "羊毛衫女套头半高领针织打底衫修身薄毛衣",
        "shopNick": "欧规则服饰旗舰店",
        "payNum": "1人付款"
    },
    {
        "price": "21.45",
        "postal": "False",
        "title": "2019夏韩版潮流 衣佳人折扣<font class=\"hl\">女装</font>V字领",
        "shopNick": "qq89533211",
        "payNum": "11人付款"
    },
    {
        "price": "89.00",
        "postal": "True",
        "title": "超火cec短袖t恤<font class=\"hl\">女装</font>夏2019新款潮韩",
        "shopNick": "蓝色之旅36",
        "payNum": "1人付款"
    },
    {
        "price": "35.90",
        "postal": "True",
        "title": "时尚套装夏季19新款<font class=\"hl\">女装</font>短袖T恤两件套女",
        "shopNick": "tb6501030_00",
        "payNum": "15人付款"
    },
    {
        "price": "148.00",
        "postal": "True",
        "title": "chic轻熟风<font class=\"hl\">女装</font>复古过膝很仙ins法式",
        "shopNick": "摩登象旗舰店",
        "payNum": "2人付款"
    },
    {
        "price": "89.00",
        "postal": "True",
        "title": "短袖t恤<font class=\"hl\">女装</font>夏2019新款潮流韩版修身时",
        "shopNick": "蓝色之旅36",
        "payNum": "1人付款"
    },
    {
        "price": "39.00",
        "postal": "True",
        "title": "<font class=\"hl\">女装</font>新款2019绿高腰短袖纯棉T恤女韩版",
        "shopNick": "爱你123459",
        "payNum": "1人付款"
    },
    {
        "price": "89.00",
        "postal": "True",
        "title": "夏季<font class=\"hl\">女装</font>新款明星同款刺绣小飞象短袖冰丝针",
        "shopNick": "zhouzanfeng1213",
        "payNum": "32人付款"
    },
    {
        "price": "218.00",
        "postal": "True",
        "title": "新款<font class=\"hl\">女装</font>毛衣纯白红线简约性冷淡北欧ins",
        "shopNick": "服饰批发零售",
        "payNum": "0人付款"
    },
    {
        "price": "388.00",
        "postal": "True",
        "title": "2019春夏新款<font class=\"hl\">女装</font>复古西装领重磅真丝长",
        "shopNick": "枫林梦旗舰店",
        "payNum": "233人付款"
    },
    {
        "price": "49.00",
        "postal": "True",
        "title": "夏季韩版宽松百搭可爱短袖T恤<font class=\"hl\">女装</font>2019",
        "shopNick": "爱你123459",
        "payNum": "0人付款"
    },
    {
        "price": "156.00",
        "postal": "True",
        "title": "欧洲站2019夏季新款<font class=\"hl\">女装</font>V领短袖纯色简",
        "shopNick": "个孩子睡觉",
        "payNum": "0人付款"
    },
    {
        "price": "58.00",
        "postal": "True",
        "title": "2019秋季新款韩版宽松POLO领前短后",
        "shopNick": "人生1015409954",
        "payNum": "13人付款"
    },
    {
        "price": "440.10",
        "postal": "False",
        "title": "Forevercan2019夏季新款粉色",
        "shopNick": "littlecan1989",
        "payNum": "723人付款"
    },
    {
        "price": "118.00",
        "postal": "True",
        "title": "不规则法式智熏裙女原创个性厌世丧系暗黑裙",
        "shopNick": "chicsky服饰旗舰店",
        "payNum": "90人付款"
    },
    {
        "price": "98.00",
        "postal": "True",
        "title": "职业连衣裙女2019秋季新款气质ol职场",
        "shopNick": "蜜煕美旗舰店",
        "payNum": "16人付款"
    },
    {
        "price": "69.00",
        "postal": "True",
        "title": "雪纺上衣女长袖2019秋季新款<font class=\"hl\">女装</font>复古波",
        "shopNick": "时尚魅力早班车",
        "payNum": "0人付款"
    },
    {
        "price": "249.00",
        "postal": "True",
        "title": "LeeMonsan/枺上2018秋装新款",
        "shopNick": "leemonsan旗舰店",
        "payNum": "30人付款"
    },
    {
        "price": "79.00",
        "postal": "True",
        "title": "真丝上衣女2019夏季宽松气质连衣裙纯色",
        "shopNick": "88可可里小姐88",
        "payNum": "4人付款"
    },
    {
        "price": "249.00",
        "postal": "False",
        "title": "CHOCOOLATE<font class=\"hl\">女装</font>短袖连衣裙潮流休闲印花",
        "shopNick": "chocoolate官方旗舰店",
        "payNum": "93人付款"
    },
    {
        "price": "149.00",
        "postal": "False",
        "title": ": CHOCOOLATE<font class=\"hl\">女装</font>短袖T恤20",
        "shopNick": "chocoolate官方旗舰店",
        "payNum": "127人付款"
    },
    {
        "price": "248.00",
        "postal": "True",
        "title": "ZIM 2019新款碎花荷叶边连衣裙女海边度假裙",
        "shopNick": "小云cc55",
        "payNum": "65人付款"
    },
    {
        "price": "359.00",
        "postal": "True",
        "title": "玛玛绨新款<font class=\"hl\">女装</font>+8.14 AM 10:0",
        "shopNick": "maxmartin玛玛绨旗舰店",
        "payNum": "0人付款"
    },
    {
        "price": "189.00",
        "postal": "True",
        "title": "2019秋季新款<font class=\"hl\">女装</font>蝴蝶结系带雪纺上衣气",
        "shopNick": "身边得小幸福",
        "payNum": "0人付款"
    },
    {
        "price": "68.90",
        "postal": "True",
        "title": "秋装2019年新款<font class=\"hl\">女装</font>潮流时尚气质雪纺衬",
        "shopNick": "惠睿琦旗舰店",
        "payNum": "14人付款"
    },
    {
        "price": "298.00",
        "postal": "False",
        "title": "秋冬新款美容院珠宝店套裙职业<font class=\"hl\">女装</font>商场制服",
        "shopNick": "luoxpcaidie",
        "payNum": "5人付款"
    },
    {
        "price": "59.90",
        "postal": "True",
        "title": "2017春秋装新款<font class=\"hl\">女装</font>条纹弹力修身针织衫",
        "shopNick": "demm九州志",
        "payNum": "2人付款"
    },
    {
        "price": "180.00",
        "postal": "False",
        "title": "19早秋新款女拼色渐变羊毛混纺针织套装",
        "shopNick": "1987lwy0609",
        "payNum": "28人付款"
    },
    {
        "price": "329.00",
        "postal": "True",
        "title": "EP雅莹2019夏季新款<font class=\"hl\">女装</font>国内代购蕾丝",
        "shopNick": "tb705035590",
        "payNum": "65人付款"
    },
    {
        "price": "170.10",
        "postal": "True",
        "title": "2019夏季时尚<font class=\"hl\">女装</font>羽毛半身加T学院风小",
        "shopNick": "我的儿子是我的男神",
        "payNum": "0人付款"
    },
    {
        "price": "49.00",
        "postal": "True",
        "title": "V领纯色中袖<font class=\"hl\">女装</font>T恤上衣夏新款5分袖修身",
        "shopNick": "镜花水月joan",
        "payNum": "1人付款"
    },
    {
        "price": "188.00",
        "postal": "True",
        "title": "2019春夏棉麻<font class=\"hl\">女装</font>新品念百秀纺原创复古",
        "shopNick": "完美66278",
        "payNum": "0人付款"
    },
    {
        "price": "886.00",
        "postal": "True",
        "title": "牧衣游 原创设计<font class=\"hl\">女装</font>中式宽松连衣裙绣花",
        "shopNick": "现产007",
        "payNum": "32人付款"
    },
    {
        "price": "59.00",
        "postal": "True",
        "title": "夏季<font class=\"hl\">女装</font>韩版纯色短袖T恤简约基础款短款修",
        "shopNick": "吉品铺",
        "payNum": "2人付款"
    },
    {
        "price": "89.00",
        "postal": "True",
        "title": "大码<font class=\"hl\">女装</font>胖mm夏装2019新款潮洋气套装",
        "shopNick": "启恩旗舰店",
        "payNum": "27人付款"
    },
    {
        "price": "59.90",
        "postal": "True",
        "title": "胖妹妹弹力小脚裤大码<font class=\"hl\">女装</font>韩国高腰膝盖破洞",
        "shopNick": "王颖dy103",
        "payNum": "0人付款"
    },
    {
        "price": "59.90",
        "postal": "True",
        "title": "大码<font class=\"hl\">女装</font>牛仔裤胖妹妹夏八分裤松紧腰哈伦小",
        "shopNick": "王颖dy103",
        "payNum": "1人付款"
    },
    {
        "price": "57.90",
        "postal": "True",
        "title": "特肥特大码<font class=\"hl\">女装</font>300斤260胖mm250",
        "shopNick": "tb9953182",
        "payNum": "1人付款"
    },
    {
        "price": "245.00",
        "postal": "True",
        "title": "TeenieW19夏装新款<font class=\"hl\">女装</font>假两件刺绣",
        "shopNick": "牛1989牛6",
        "payNum": "0人付款"
    },
    {
        "price": "120.00",
        "postal": "True",
        "title": "2019秋冬新品<font class=\"hl\">女装</font>宽松印花单排扣翻领衬",
        "shopNick": "眯眯眼ace131415",
        "payNum": "0人付款"
    },
    {
        "price": "138.25",
        "postal": "True",
        "title": "mq正品夏韩版时尚<font class=\"hl\">女装</font>休闲长裙连衣裙女宽",
        "shopNick": "爱的就是奢华感",
        "payNum": "2人付款"
    },
    {
        "price": "149.00",
        "postal": "True",
        "title": "欧洲站t恤裙女欧货宽松潮牌个性连衣裙厌世",
        "shopNick": "宿风旗舰店",
        "payNum": "12人付款"
    },
    {
        "price": "48.90",
        "postal": "True",
        "title": "大码<font class=\"hl\">女装</font>2019新款宽松显瘦中长款胖mm",
        "shopNick": "tb9953182",
        "payNum": "1人付款"
    },
    {
        "price": "75.00",
        "postal": "True",
        "title": "大码<font class=\"hl\">女装</font>萝卜裤春装新款2019胖mm乱麻",
        "shopNick": "jolin8800",
        "payNum": "26人付款"
    },
    {
        "price": "128.00",
        "postal": "True",
        "title": "2019夏季新款流行<font class=\"hl\">女装</font>雪纺红色波点连衣",
        "shopNick": "美丽e家1",
        "payNum": "4人付款"
    },
    {
        "price": "176.00",
        "postal": "True",
        "title": "梵希蔓很仙的衬衣设计感上衣轻熟风<font class=\"hl\">女装</font>春秋",
        "shopNick": "梵希蔓旗舰店",
        "payNum": "43人付款"
    },
    {
        "price": "79.00",
        "postal": "True",
        "title": "2019春秋新款蕾丝微喇裤<font class=\"hl\">女装</font>长裤外穿打",
        "shopNick": "容情旗舰店",
        "payNum": "161人付款"
    },
    {
        "price": "29.90",
        "postal": "True",
        "title": "短袖t恤枣红色宽松<font class=\"hl\">女装</font>2019新款潮短袖",
        "shopNick": "his9899",
        "payNum": "49人付款"
    },
    {
        "price": "79.00",
        "postal": "True",
        "title": "女连衣裙长裙雪纺连衣裙桑蚕丝连衣裙<font class=\"hl\">女装</font>?",
        "shopNick": "fashion祺靓店",
        "payNum": "11人付款"
    },
    {
        "price": "29.90",
        "postal": "True",
        "title": "大码<font class=\"hl\">女装</font>新款吊带背心V领显瘦短款打底舒适",
        "shopNick": "棉夕旗舰店",
        "payNum": "0人付款"
    },
    {
        "price": "29.90",
        "postal": "True",
        "title": "衣服女2019新品大码宽松原宿港风<font class=\"hl\">女装</font>胖",
        "shopNick": "美嘉莉服饰旗舰店",
        "payNum": "17人付款"
    },
    {
        "price": "497.00",
        "postal": "True",
        "title": "真丝桑蚕丝连衣裙直筒2019春夏新款<font class=\"hl\">女装</font>",
        "shopNick": "恩纳斯旗舰店",
        "payNum": "792人付款"
    },
    {
        "price": "69.00",
        "postal": "True",
        "title": "夏季新款韩版卡通星空印花上衣体恤<font class=\"hl\">女装</font>大码",
        "shopNick": "刘国良wind",
        "payNum": "1人付款"
    },
    {
        "price": "229.00",
        "postal": "True",
        "title": "2019夏装新款欧洲站个性字母印花连衣裙",
        "shopNick": "zvbv旗舰店",
        "payNum": "39人付款"
    },
    {
        "price": "99.00",
        "postal": "True",
        "title": "潮牌t恤女 欧美街头2019夏季新款个性",
        "shopNick": "宿风旗舰店",
        "payNum": "21人付款"
    },
    {
        "price": "59.00",
        "postal": "True",
        "title": "夏季<font class=\"hl\">女装</font> 黑色双V领露背中袖T恤纯棉修身",
        "shopNick": "吉品铺",
        "payNum": "0人付款"
    },
    {
        "price": "19.90",
        "postal": "True",
        "title": "大码<font class=\"hl\">女装</font>微胖女孩穿搭胖MM冰丝针织打底内",
        "shopNick": "棉夕旗舰店",
        "payNum": "0人付款"
    },
    {
        "price": "388.00",
        "postal": "True",
        "title": "欧洲站夏季2019新款<font class=\"hl\">女装</font>极简主义小黑裙",
        "shopNick": "不了了了了之",
        "payNum": "2人付款"
    },
    {
        "price": "38.00",
        "postal": "True",
        "title": "酒店工作服T恤短袖上衣餐饮奶茶店前台保洁",
        "shopNick": "迪麦丝旗舰店",
        "payNum": "33人付款"
    },
    {
        "price": "69.00",
        "postal": "True",
        "title": "秋装2019年新款<font class=\"hl\">女装</font>潮流时尚v领雪纺衬",
        "shopNick": "娇雅芬旗舰店",
        "payNum": "4人付款"
    },
    {
        "price": "159.00",
        "postal": "True",
        "title": "2019秋季风格款OL气质韩版时尚<font class=\"hl\">女装</font>长",
        "shopNick": "505367319shu",
        "payNum": "13人付款"
    },
    {
        "price": "89.00",
        "postal": "True",
        "title": "200斤加肥大码<font class=\"hl\">女装</font>胖mm夏装2019新",
        "shopNick": "启恩旗舰店",
        "payNum": "18人付款"
    },
    {
        "price": "255.00",
        "postal": "True",
        "title": "2019夏季新款<font class=\"hl\">女装</font>两件套圆领短袖荷叶边",
        "shopNick": "ab丶崇拜",
        "payNum": "2人付款"
    },
    {
        "price": "298.00",
        "postal": "True",
        "title": "气质减龄英伦范儿 韩国19年夏 小狗皇冠",
        "shopNick": "纤百家好一号店",
        "payNum": "3人付款"
    },
    {
        "price": "158.00",
        "postal": "True",
        "title": "夏季<font class=\"hl\">女装</font>新款三亚海边度假旅游必备复古港味",
        "shopNick": "雪地欧旗舰店",
        "payNum": "76人付款"
    },
    {
        "price": "238.00",
        "postal": "True",
        "title": "2019新款秋装连衣裙性感<font class=\"hl\">女装</font>夜店修身包",
        "shopNick": "安雨彤旗舰店",
        "payNum": "1人付款"
    },
    {
        "price": "129.00",
        "postal": "True",
        "title": "春哥大码<font class=\"hl\">女装</font>新款胖mm宽松显瘦不规则半身",
        "shopNick": "杀了春哥",
        "payNum": "34人付款"
    },
    {
        "price": "29.90",
        "postal": "True",
        "title": "上衣女2019新款宽松夏季大码<font class=\"hl\">女装</font>胖mm",
        "shopNick": "美嘉莉服饰旗舰店",
        "payNum": "7人付款"
    },
    {
        "price": "99.00",
        "postal": "True",
        "title": "大码女胖妹妹遮肚收腰显瘦性感一字肩连衣裙",
        "shopNick": "杀了春哥",
        "payNum": "24人付款"
    },
    {
        "price": "51.00",
        "postal": "True",
        "title": "2019年新款<font class=\"hl\">女装</font>四色入学生大码白色高腰",
        "shopNick": "wttbifa8505",
        "payNum": "0人付款"
    }
]}


def index(request):
    return render(request, 'items/list.html', context)
    # return render_to_response('items/list.html')
