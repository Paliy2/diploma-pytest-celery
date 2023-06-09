import pytest
from celery import Celery
from pytest_lazyfixture import lazy_fixture

from pytest_celery import CeleryTestWorker
from pytest_celery import CeleryWorkerCluster
from pytest_celery import defaults
from pytest_celery.containers.worker import CeleryWorkerContainer


@pytest.mark.parametrize("node", [lazy_fixture(defaults.CELERY_WORKER)])
class test_celey_test_worker:
    def test_ready(self, node: CeleryTestWorker):
        assert node.ready()

    def test_app(self, node: CeleryTestWorker, celery_setup_app: Celery):
        assert node.app is celery_setup_app

    def test_version(self, node: CeleryTestWorker):
        assert node.version == CeleryWorkerContainer.version()


@pytest.mark.parametrize("cluster", [lazy_fixture(defaults.CELERY_WORKER_CLUSTER)])
class test_celery_worker_cluster:
    def test_ready(self, cluster: CeleryWorkerCluster):
        assert cluster.ready()

    def test_app(self, cluster: CeleryWorkerCluster, celery_setup_app: Celery):
        node: CeleryTestWorker
        for node in cluster:
            assert node.app is celery_setup_app

    def test_versions(self, cluster: CeleryWorkerCluster):
        assert cluster.versions == {CeleryWorkerContainer.version()}
