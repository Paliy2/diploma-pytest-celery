from celery import Celery

from pytest_celery.api.components.cluster.node import CeleryTestNode
from pytest_celery.api.container import CeleryTestContainer
from pytest_celery.containers.worker import CeleryWorkerContainer


class CeleryTestWorker(CeleryTestNode):
    def __init__(self, container: CeleryTestContainer, app: Celery):
        super().__init__(container)
        self._app = app
        self.container: CeleryWorkerContainer

    @property
    def app(self) -> Celery:
        return self._app

    @property
    def version(self) -> str:
        if hasattr(self.container, "version"):
            return self.container.version()
        else:
            return "unknown"

    @property
    def log_level(self) -> str:
        return self.container.log_level()

    @property
    def worker_name(self) -> str:
        return self.container.worker_name()

    @property
    def worker_queue(self) -> str:
        return self.container.worker_queue()
