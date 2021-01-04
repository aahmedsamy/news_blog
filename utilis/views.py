from blogs.models import Category


def _header_context():
    ret = dict()
    ret['header_categories'] = Category.objects.all().values('id', 'name')

    return ret


def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}
