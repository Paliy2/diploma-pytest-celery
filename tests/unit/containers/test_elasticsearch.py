from elasticsearch import Elasticsearch

from pytest_celery import ElasticsearchContainer
from pytest_celery import defaults


class test_elasticsearch_test_backend:
    def test_client(self, default_elasticsearch_container: ElasticsearchContainer):
        assert isinstance(default_elasticsearch_container.client, Elasticsearch)

    def test_celeryconfig(self, default_elasticsearch_container: ElasticsearchContainer):
        expected_keys = {"url", "local_url", "hostname", "port", "vhost"}
        assert set(default_elasticsearch_container.celeryconfig.keys()) == expected_keys

    def test_version(self, default_elasticsearch_container: ElasticsearchContainer):
        assert default_elasticsearch_container.version() == "8.2.2"

    def test_env(self, default_elasticsearch_container: ElasticsearchContainer):
        assert default_elasticsearch_container.env() == {}

    def test_image(self, default_elasticsearch_container: ElasticsearchContainer):
        assert default_elasticsearch_container.image() == defaults.ELASTICSEARCH_IMAGE
