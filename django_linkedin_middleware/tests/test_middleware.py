import os
from unittest import TestCase

from django.test import override_settings
from mock import MagicMock

from django_linkedin_middleware.middleware import LinkedinMiddleware


class MiddlewareTests(TestCase):

    def setUp(self):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'django_linkedin_middleware.tests.settings'
        self.request_mock = MagicMock()
        self.middleware = LinkedinMiddleware(self.request_mock)

    def test_is_authorized_pages_with_default_configuration(self):
        assert self.middleware.is_authorized_page('any page') is True

    @override_settings(PAGES_WITH_LINKEDIN_AUTH_REQUIRED=['page'])
    @override_settings(PAGES_WITHOUT_LINKEDIN_AUTH_REQUIRED=[])
    def test_is_authorized_pages_with_pages_required(self):
        assert self.middleware.is_authorized_page('page') is True

    @override_settings(PAGES_WITH_LINKEDIN_AUTH_REQUIRED=['mypage'])
    @override_settings(PAGES_WITHOUT_LINKEDIN_AUTH_REQUIRED=[])
    def test_is_authorized_pages_with_other_page(self):
        assert self.middleware.is_authorized_page('otherpage') is False

    @override_settings(PAGES_WITH_LINKEDIN_AUTH_REQUIRED=['mypage'])
    @override_settings(PAGES_WITHOUT_LINKEDIN_AUTH_REQUIRED=['mypage'])
    def test_is_authorized_pages_with_same_page_ok_and_ko(self):
        assert self.middleware.is_authorized_page('mypage') is False

    @override_settings(PAGES_WITH_LINKEDIN_AUTH_REQUIRED=['*'])
    @override_settings(PAGES_WITHOUT_LINKEDIN_AUTH_REQUIRED=['not_authorized_page'])
    def test_is_authorized_pages_complete_test(self):
        assert self.middleware.is_authorized_page('page_1') is True
        assert self.middleware.is_authorized_page('page_2') is True
        assert self.middleware.is_authorized_page('not_authorized_page') is False

    @override_settings(PAGES_WITH_LINKEDIN_AUTH_REQUIRED=[])
    def test_is_authorized_pages_with_empty_authorized_page(self):
        assert self.middleware.is_authorized_page('mypage') is False
