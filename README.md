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

In a separate terminal window run:

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

## 100 - Introduction

See [README.md](./100/README.md)

## 200 - Requirements

See [README.md](./200/README.md)

## 300 - Building Our Application

See [README.md](./300/README.md)

## 400 - Conclusion

See [README.md](./400/README.md)
