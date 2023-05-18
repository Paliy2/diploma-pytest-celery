class test_elasticsearch_test_backend:
    def test_ready(self, celery_elasticsearch_backend):
        assert celery_elasticsearch_backend.ready()
