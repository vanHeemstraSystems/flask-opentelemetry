flask-opentelemetry
# Flask OpenTelemetry

> OpenTelemetry (OTel) is an open-source, vendor-neutral observability framework designed to work with any backend system. It provides standardized APIs, libraries, and tools to collect telemetry data, such as metrics, logs, and traces. This talk is intended to provide a starting point for working with OpenTelemetry in Flask.

[References](./REFERENCES.md)

**Executive Summary**

After [installation](./300/100/README.md), run it with:

```
$ cd flask_opentelemetry/src/example
$ flask run
```

Open a web browser at http://localhost: 5000

Stop the server (CTRL+C) and in the same terminal run:

```
$ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
```

Followed by:

```
opentelemetry-instrument \
  --traces_exporter console \
  --metrics_exporter console \
  --logs_exporter console \
  --service_name todo \
  flask run -p 8080
```

Alternatively, you can use environment variables to configure the agent:

```
OTEL_SERVICE_NAME=todo \
OTEL_TRACES_EXPORTER=console \
OTEL_METRICS_EXPORTER=console \
OTEL_LOG_EXPORTER=console
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:8080
opentelemetry-instrument \
    flask run
```

## 100 - Introduction

See [README.md](./100/README.md)

## 200 - Requirements

See [README.md](./200/README.md)

## 300 - Building Our Application

See [README.md](./300/README.md)

## 400 - Conclusion

See [README.md](./400/README.md)
