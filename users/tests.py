import jwt
import json
import unittest

from django.test import Client, TestCase
from django.conf import settings

from unittest.mock import MagicMock, patch
from .models import User, Platform
from my_settings import ALGORITHM

class SocialLoginViewTest(TestCase):
    def setUp(self):
        Platform.objects.create(
            name      = 'Kakao',
            id        = 1
        )

        platform = Platform.objects.get(id=1)

        User.objects.create(
            id                = 1,
            social_id         = 777777,
            nickname          = 'wooju',
            profile_image_url = 'http://k.kakaocdn.net/dn/hvPKi/btrcs8enuXr/w9W1caGT2Gc7kyNv1AEpM1/img_640x640.jpg',
            platform_id       = platform.id
        )

    def tearDown(self):
        Platform.objects.all().delete()
        User.objects.all().delete()

    @patch("users.views.requests")
    def test_kakao_signin_post_succes(self, mocked_requests):

        class FakeKakaoLogin:
            def json(self):
                return {
                    "id": 777777,
                    "kakao_account": {
                        "profile": {
                            "nickname": "wooju",
                            "profile_image_url": "http://k.kakaocdn.net/dn/hvPKi/btrcs8enuXr/w9W1caGT2Gc7kyNv1AEpM1/img_640x640.jpg",
                        },
                    }
                }
        
        mocked_requests.get = MagicMock(return_value = FakeKakaoLogin())

        client   = Client()
        headers  = {"HTTP_Authorization" : "fake_token"}
        response = client.post("/users/sign-in/kakao",content_type = 'application/json', **headers)
        user = User.objects.get(id = 1)
        
        token = jwt.encode({"id" : user.id}, settings.SECRET_KEY, algorithm = ALGORITHM)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message" : "SUCCESS", "access_token": token})

    @patch("users.views.requests")
    def test_kakao_signin_post_fail(self, mocked_requests):

        class FakeKakaoLoginFail:
            def json(self):
                return {
                    "code": -401
                }

        mocked_requests.get = MagicMock(return_value = FakeKakaoLoginFail())
        client   = Client()
        headers  = {"HTTP_Authorization" : "fail_token"}
        response = client.post("/users/sign-in/kakao",content_type = 'application/json', **headers)

        self.assertEqual(response.status_code, 401)

    @patch("users.views.requests")
    def test_kakao_signin_post_key_error(self, mocked_requests):

        class FakeKakaoLoginKeyError:
            def json(self):
                return{
                }

        mocked_requests.get = MagicMock(return_value = FakeKakaoLoginKeyError())
        client  = Client()
        headers = {"HTTP_Authorization" : "key_error_token"}
        response = client.post("/users/sign-in/kakao",content_type = 'application/json', **headers)

        self.assertEqual(response.status_code, 400)