import pytest
from pytest_docker_tools import container

from pytest_celery import CeleryTestBackend, CeleryTestContainer
from pytest_celery.containers import RedisContainer


@pytest.fixture
def celery_elasticsearch_backend(default_elasticsearch_backend):
    backend = CeleryTestBackend(default_elasticsearch_backend)
    yield backend
    backend.teardown()


# default_elasticsearch_backend = container(
#     # image="hpfeeds/hpfeeds-broker:latest",
#     image="redis:latest",
#     ports={"6379/tcp": None},
#     # image="elasticsearch:7.12.0",
#     # image="{elasticsearch:latest}",
#     # ports={"20000/tcp": None},  # will map the hostport to a random open port on the host (just like running dockerrun-P)
#     # ports={"9200/tcp": None},  # will map the hostport to a random open port on the host (just like running dockerrun-P)
#     # network="{DEFAULT_NETWORK.name}",
# )


default_elasticsearch_backend = container(
    image="redis:latest",
    # ports=fxtr("default_redis_backend_ports"),
    ports={"6379/tcp": None},
    # environment=fxtr("default_redis_backend_env"),
    # network="{DEFAULT_NETWORK.name}",
    wrapper_class=CeleryTestContainer,
    # timeout=defaults.REDIS_CONTAINER_TIMEOUT,
)
