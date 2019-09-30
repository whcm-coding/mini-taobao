from django.db import models


class ItemList(models.Model):
    price = models.CharField(
        max_length=200, verbose_name="价格", help_text="输入数字，例如：168")
    postal = models.CharField(
        max_length=200, verbose_name="包邮", help_text="输入True 或 False")
    title = models.CharField(
        max_length=200, verbose_name="服装标题", help_text="例如：真丝小衫女")
    shopNick = models.CharField(
        max_length=200, verbose_name="店铺名", help_text="Lee官方旗舰店")
    payNum = models.CharField(
        max_length=200, verbose_name="付款人数", help_text="例如：6人付款")
    count = models.PositiveIntegerField(verbose_name="库存", help_text="例如：10")
    image = models.CharField(max_length=200, verbose_name="图片链接",
                             help_text="https://img.alicdn.com/imgextra/i1/123814384/O1CN01u2VMux1iFutwj2tl4_!!0-saturn_solar.jpg_220x220.jpg_.webp")
