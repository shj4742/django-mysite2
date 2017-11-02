from django.db import models

# Create your models here.


class FoodCalorie(models.Model):

    class Meta():
        # 默认的表名是:应用名_模型名
        db_table = 'foodCalorie'
        # 设置排序的字段
        ordering = ['-id']
    title = models.CharField('标题', max_length=100)
    content = models.CharField('内容', max_length=500)
    image_addr = models.URLField('链接')
    # 用于逻辑删除
    isDelete = models.BooleanField('是否逻辑删除', default=False)

    def __str__(self):
        return self.title