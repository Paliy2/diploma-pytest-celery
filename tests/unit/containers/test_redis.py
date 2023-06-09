from pytest_celery import RedisContainer
from pytest_celery import defaults


class test_redis_container:
    def test_client(self, redis_test_container: RedisContainer):
        assert redis_test_container.client

    def test_celeryconfig(self, redis_test_container: RedisContainer):
        expected_keys = {"url", "local_url", "hostname", "port", "vhost"}
        assert set(redis_test_container.celeryconfig.keys()) == expected_keys

    def test_version(self, redis_test_container: RedisContainer):
        assert redis_test_container.version() == "latest"

    def test_env(self, redis_test_container: RedisContainer):
        assert redis_test_container.env() == defaults.REDIS_ENV

    def test_image(self, redis_test_container: RedisContainer):
        assert redis_test_container.image() == defaults.REDIS_IMAGE
