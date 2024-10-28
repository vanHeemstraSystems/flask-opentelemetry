flask-opentelemetry
# Flask OpenTelemetry

> OpenTelemetry (OTel) is an open-source, vendor-neutral observability framework designed to work with any backend system. It provides standardized APIs, libraries, and tools to collect telemetry data, such as metrics, logs, and traces. This talk is intended to provide a starting point for working with OpenTelemetry in Flask.

- [Glossary](./GLOSSARY.md)
- [References](./REFERENCES.md)

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

Followed by starting the application via the agent (see [reference](https://opentelemetry.io/docs/instrumentation/python/automatic/#configuring-the-agent)) and keep a text log file:

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
ELASTIC_APM_SERVER_ENDPOINT=0.0.0.0:4317 \
ELASTIC_APM_SECRET_TOKEN=secret \
OTEL_EXPORTER_OTLP_INSECURE=true \
opentelemetry-instrument \
    flask run -p 5000 | tee output.log
```

Open a web browser at http://localhost:5000

You will see the same ```To-Do List``` app. You can add or delete tasks.

In the terminal, you will see output alike:

```
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [28/Oct/2024 14:20:33] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [28/Oct/2024 14:20:37] "POST /add HTTP/1.1" 302 -
127.0.0.1 - - [28/Oct/2024 14:20:37] "GET / HTTP/1.1" 200 -
{
    "name": "GET /",
    "context": {
        "trace_id": "0xf70da0284034c5ea91a354e82ea3358f",
        "span_id": "0x791d76168f2219ef",
        "trace_state": "[]"
    },
    "kind": "SpanKind.SERVER",
    "parent_id": null,
    "start_time": "2024-10-28T14:20:33.591136Z",
    "end_time": "2024-10-28T14:20:33.598630Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "http.method": "GET",
        "http.server_name": "127.0.0.1",
        "http.scheme": "http",
        "net.host.name": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
        "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
        "net.host.port": 5000,
        "http.target": "/",
        "net.peer.ip": "127.0.0.1",
        "net.peer.port": 48680,
        "http.user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "http.flavor": "1.1",
        "http.route": "/",
        "http.status_code": 200
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.27.0",
            "service.name": "todo",
            "telemetry.auto.version": "0.48b0"
        },
        "schema_url": ""
    }
}
{
    "name": "POST /add",
    "context": {
        "trace_id": "0x1225b9a518cf7ea836eefc4a9ee6d3c0",
        "span_id": "0xa124085da8f4ce10",
        "trace_state": "[]"
    },
    "kind": "SpanKind.SERVER",
    "parent_id": null,
    "start_time": "2024-10-28T14:20:37.643212Z",
    "end_time": "2024-10-28T14:20:37.648385Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "http.method": "POST",
        "http.server_name": "127.0.0.1",
        "http.scheme": "http",
        "net.host.name": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
        "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
        "net.host.port": 5000,
        "http.target": "/add",
        "net.peer.ip": "127.0.0.1",
        "net.peer.port": 42142,
        "http.user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "http.flavor": "1.1",
        "http.route": "/add",
        "http.status_code": 302
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.27.0",
            "service.name": "todo",
            "telemetry.auto.version": "0.48b0"
        },
        "schema_url": ""
    }
}
{
    "name": "GET /",
    "context": {
        "trace_id": "0xf78ac5fe73bea41b6ef6ec50996bd085",
        "span_id": "0x97c2270b6866fe65",
        "trace_state": "[]"
    },
    "kind": "SpanKind.SERVER",
    "parent_id": null,
    "start_time": "2024-10-28T14:20:37.666513Z",
    "end_time": "2024-10-28T14:20:37.669702Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "http.method": "GET",
        "http.server_name": "127.0.0.1",
        "http.scheme": "http",
        "net.host.name": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
        "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
        "net.host.port": 5000,
        "http.target": "/",
        "net.peer.ip": "127.0.0.1",
        "net.peer.port": 42158,
        "http.user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "http.flavor": "1.1",
        "http.route": "/",
        "http.status_code": 200
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.27.0",
            "service.name": "todo",
            "telemetry.auto.version": "0.48b0"
        },
        "schema_url": ""
    }
}
```

The OpenTelemetry (OTel) collector runs on port 4317, so any other error message than a timeout/connection error (e.g. ```Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.```), means that the application is running:

```
$ curl localhost:4317
curl: (1) Received HTTP/0.9 when not allowed
```

If the OTel Collector is not running you get:

```
$ curl localhost:4317
curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused
```

With this setup, in addition to the OTel Collector, we also get [Jaeger UI](https://github.com/jaegertracing/jaeger-ui) running under http://0.0.0.0:16686/ which will help in visualizing the calls. Alternative UIs that are supported are ```Prometheus``` and ```ZipKin```.

The client and server send data directly to the OTel Collector; The OTel Collector then sends the data to the appropriate backend, in this demo ```Jaeger```.

You can grep any urls from the text logfile:

```
$ cat output.log | grep http.host
```

You will see an output like:

```
"http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
"http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
"http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
...
```        

The collected telemetry is helpful to understand the amount and latency of the requests over time. 

Let’s filter in Jaeger UI (http://0.0.0.0:16686/) for one of the URLs using the tag ``` == url goes here == ```.

MORE

## 100 - Introduction

See [README.md](./100/README.md)

## 200 - Requirements

See [README.md](./200/README.md)

## 300 - Building Our Application

See [README.md](./300/README.md)

## 400 - Conclusion

See [README.md](./400/README.md)
