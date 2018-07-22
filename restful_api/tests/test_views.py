from django.urls import reverse, resolve


class TestViews:
    def test_user_detail_auth(self):
        path = reverse('user-detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'user-detail'