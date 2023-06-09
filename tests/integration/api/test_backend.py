import pytest
from pytest_lazyfixture import lazy_fixture

from pytest_celery import CeleryBackendCluster
from pytest_celery import CeleryTestBackend
from pytest_celery import defaults


@pytest.mark.parametrize("node", [lazy_fixture(defaults.CELERY_BACKEND)])
class test_celey_test_backend:
    def test_ready(self, node: CeleryTestBackend):
        assert node.ready()


@pytest.mark.parametrize("cluster", [lazy_fixture(defaults.CELERY_BACKEND_CLUSTER)])
class test_celery_backend_cluster:
    def test_ready(self, cluster: CeleryBackendCluster):
        assert cluster.ready()
