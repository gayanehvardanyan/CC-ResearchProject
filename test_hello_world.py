import json

from hello_user import hello_user_handler


def test_hello_user():
    expected_output = {"message": "Hello CI CD Developer!"}
    actual = hello_user_handler({"queryStringParameters": {"user": "CI CD Developer"}}, {})
    assert json.loads(actual["body"]) == expected_output
    assert actual["statusCode"] == 200