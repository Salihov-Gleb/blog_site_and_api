from django.db import models
from django.contrib.auth.models import User


class BlogNote(models.Model):
    title = models.CharField(max_length=80, unique=True, verbose_name='Название')
    img = models.ImageField(verbose_name='Изображение', blank=True, upload_to='resources/images/%Y/%m/%d/')
    category = models.ManyToManyField('Category', verbose_name='Категории')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    txt = models.TextField(blank=False, verbose_name='Текст')
    create_date = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    update_date = models.DateField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f"'{self.title}': {self.author}"

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('-update_date', 'title')
    #
    # def get_absolute_url(self):
    #     return reverse('blog:note', kwargs={'blog_slug': self.slug})
    #
    # def save(self, force_insert=False, force_update=False, using=None, update_field=None):
    #     if not self.slug:
    #         slug = '-'.join(filter(lambda x: x != '', str(self.title).lower().split(' ')))
    #         while len(BlogNote.objects.filter(slug=slug)) > 0:
    #             last = slug.split('-')[-1]
    #             if last.isdigit():
    #                 slug = slug[:-len(last)] + str(int(last) + 1)
    #             else:
    #                 slug += '-1'
    #         self.slug = slug
    #     super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class Category(models.Model):
    title = models.CharField(max_length=60, unique=True, verbose_name='Название', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)
