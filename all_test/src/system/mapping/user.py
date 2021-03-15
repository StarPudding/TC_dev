from all_test.src.system.models import user


def getAllUser(current_page, page_size):
    out = user.objects.raw("select * from test_user LIMIT %s,%s",
                           params=[(current_page-1)*page_size, page_size])

    count = user.objects.filter().count()
    return out, count

