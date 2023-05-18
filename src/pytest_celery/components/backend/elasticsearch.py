import pytest
from pytest_docker_tools import container

from pytest_celery import CeleryTestBackend, defaults, CeleryTestContainer
from pytest_celery.containers.elasticsearch import ElasticsearchContainer

ElasticsearchBackend = CeleryTestBackend


@pytest.fixture
def celery_elasticsearch_backend(default_elasticsearch_container: ElasticsearchContainer) -> ElasticsearchBackend:
    backend = CeleryTestBackend(default_elasticsearch_container)
    yield backend
    backend.teardown()


default_elasticsearch_container = container(
    image=defaults.ELASTICSEARCH_IMAGE,
    # will map the hosostport to a random open port on the host (just like running dockerrun-P)
    ports=defaults.ELASTICSEARCH_PORTS,
    environment=defaults.ELASTICSEARCH_ENV,
    network="elastic",
    name="elastic-test-server",
    # wrapper_class=CeleryTestContainer,
    wrapper_class=ElasticsearchContainer,
    timeout=defaults.ELASTICSEARCH_CONTAINER_TIMEOUT,
)
