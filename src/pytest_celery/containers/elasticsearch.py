from typing import Optional

from kombu.utils import cached_property

from pytest_celery import defaults
from pytest_celery.api.container import CeleryTestContainer
from elasticsearch import Elasticsearch


class ElasticsearchContainer(CeleryTestContainer):
    @cached_property
    def client(self) -> Optional[Elasticsearch]:
        client = Elasticsearch(
            self.celeryconfig["local_url"],
        )
        return client

    @cached_property
    def celeryconfig(self) -> dict:
        return {
            "url": self.url,
            "local_url": self.local_url,
            "hostname": self.hostname,
            "port": self.port,
            "vhost": self.vhost,
        }

    @property
    def url(self) -> str:
        return f"elasticsearch://{self.hostname}/{self.vhost}"

    @property
    def local_url(self) -> str:
        return f"elasticsearch://localhost:{self.port}/{self.vhost}"

    @property
    def hostname(self) -> str:
        return self.attrs["Config"]["Hostname"]

    @property
    def port(self) -> int:
        return self._wait_port("9200/tcp")

    @property
    def vhost(self) -> str:
        return "1"

    @classmethod
    def version(cls) -> str:
        return cls.image().split(":")[-1]

    @classmethod
    def env(cls) -> dict:
        return defaults.DEFAULT_ELASTICSEARCH_BACKEND_ENV

    @classmethod
    def image(cls) -> str:
        return defaults.DEFAULT_ELASTICSEARCH_BACKEND_IMAGE

    @classmethod
    def ports(cls) -> dict:
        return defaults.DEFAULT_ELASTICSEARCH_BACKEND_PORTS

    @property
    def ready_prompt(self) -> Optional[str]:
        """This prompt is used to compare the actual container outputs.
        By comparing the ready_prompt with container logs, we can
        understand whether the server has started."""
        return "Copyright (c) 2022 Elasticsearch BV"
