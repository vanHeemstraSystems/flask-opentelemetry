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

Open a web browser at http://localhost:5000

You will see a ```To-Do List``` app. You can add or delete tasks.

Stop the server (CTRL+C) and in the same terminal run:

```
$ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
```

Followed by starting the application via the agent (see reference) and keep a text log file:

```
opentelemetry-instrument \
  --traces_exporter console \
  --metrics_exporter console \
  --logs_exporter console \
  --service_name todo \
  flask run -p 5000 | tee output.log
```

Alternatively, you can use environment variables to configure the agent:

```
OTEL_SERVICE_NAME=todo \
OTEL_TRACES_EXPORTER=console \
OTEL_METRICS_EXPORTER=console \
OTEL_LOG_EXPORTER=console \
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317 \
OTEL_EXPORTER_OTLP_INSECURE=true \
opentelemetry-instrument \
    flask run -p 5000 | tee output.log
```

Open a web browser at http://localhost:5000

You will see the same ```To-Do List``` app. You can add or delete tasks.

But on port 4317, the OpenTelemetry server is listening.

The collector runs on port 4317, so any other error message than a timeout/connection error (e.g. ```Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.```), means that the application is running:

```
$ curl localhost:4317
curl: (1) Received HTTP/0.9 when not allowed
```

If the collector is not running you get:

```
$ curl localhost:4317
curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused
```

With this setup, in addition to the open telemetry collector, we also get [Jaeger UI](https://github.com/jaegertracing/jaeger-ui) running under http://0.0.0.0:16686/ which will help in visualizing the calls.

The client and server send data directly to the OTel Collector;
The OTel Collector then sends the data to the appropriate backend, in this demo Jaeger.

You can grep any urls from the text logfile:

```
$ cat output.log | grep http.url
```

The collected telemetry is helpful to understand the amount and latency of the requests over time. Let’s filter in Jaeger UI (http://0.0.0.0:16686/) for one of the URLs using the tag ``` url goes here ```.



## 100 - Introduction

See [README.md](./100/README.md)

## 200 - Requirements

See [README.md](./200/README.md)

## 300 - Building Our Application

See [README.md](./300/README.md)

## 400 - Conclusion

See [README.md](./400/README.md)
