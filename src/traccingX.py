import logging
import os
from jaeger_client import Config
from flask_opentracing import FlaskTracing, FlaskTracer
import opentracing

# JAEGER_HOST = os.getenv("JAEGER_HOST", "jaeger")
# JAEGER_PORT = os.getenv("JAEGER_PORT", "6831")
# JAEGER_SERVICE_NAME = os.getenv("JAEGER_SERVICE_NAME", "gerador-rg")
JAEGER_SERVICE_NAME = 'apimon'

def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                'reporting_host': 'jaeger',
                'reporting_port': 6831
            },            
            'logging': True,
        },
        service_name=service,
    )

    return config.initialize_tracer()

opentracing_tracer = init_tracer(JAEGER_SERVICE_NAME)
tracing = FlaskTracer(opentracing_tracer)
