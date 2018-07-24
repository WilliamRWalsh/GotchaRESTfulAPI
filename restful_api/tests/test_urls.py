from django.urls import reverse, resolve


class TestViews:
    def test_user_detail_url(self):
        path = reverse('user-detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'user-detail'

    def test_user_list_url(self):
        path = reverse('user-list')
        assert resolve(path).view_name == 'user-list'
