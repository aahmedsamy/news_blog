from django.utils import timezone

from blogs.models import Category, Blog


class HeaderContext:
    def __new__(cls, *args, **kwargs):
        return {**cls._header_context()}

    @staticmethod
    def _header_context():
        ret = dict()
        ret['header_categories'] = Category.objects.filter(category_blogs__isnull=False).distinct("name", "pk").values(
            "id",
            "name",
            "icon")

        return ret


class HomeContext:
    def __new__(cls, *args, **kwargs):
        return {**cls._main_slider(), **cls._editors_pick(),
                **cls._top_picks_this_month(), **cls._topics_list()}

    @staticmethod
    def _main_slider():
        ret = dict()
        print(timezone.now())
        ret['main_slider_blogs'] = Blog.objects.filter(publish_date__lte=timezone.now()).distinct(
            "category__name").values("image", "title", "body",
                                     "category__name")
        return ret

    @staticmethod
    def _editors_pick():
        ret = dict()
        ret['editors_picked_blogs'] = \
            Blog.objects.filter(publish_date__lte=timezone.now()).values("id", "image", "author__image", "author__first_name", "author__last_name",
                                      "publish_date", "title", "body",
                                      "category__name")[:2]
        return ret

    @staticmethod
    def _top_picks_this_month():
        ret = dict()
        ret['top_picked_blogs_this_month'] = Blog.objects.filter(publish_date__lte=timezone.now()).values("id", "image", "author__image",
                                                                       "author__first_name",
                                                                       "author__last_name", "publish_date", "title")[:3]
        return ret

    @staticmethod
    def _topics_list():
        ret = dict()
        ret['topics_list_categories'] = Category.objects.filter(category_blogs__isnull=False).distinct("name",
                                                                                                       "pk").values(
            "id",
            "name",
            "icon")
        return ret
