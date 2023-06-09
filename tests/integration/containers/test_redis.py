import pytest
from pytest_lazyfixture import lazy_fixture

from pytest_celery import RedisContainer
from pytest_celery import defaults


@pytest.mark.parametrize("container", lazy_fixture(defaults.ALL_REDIS_FIXTURES))
class test_redis_container:
    def test_client(self, container: RedisContainer):
        assert container.client
        assert container.client.ping()
        assert container.client.set("ready", "1")
        assert container.client.get("ready") == "1"
        assert container.client.delete("ready")
