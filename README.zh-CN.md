烧瓶开孔遥测

# Flask 开放遥测

> OpenTelemetry (OTel) 是一个开源、供应商中立的可观测性框架，旨在与任何后端系统配合使用。它提供标准化的 API、库和工具来收集遥测数据，例如指标、日志和跟踪。本演讲旨在为在 Flask 中使用 OpenTelemetry 提供一个起点。

[参考](./REFERENCES.md)

**执行摘要**

后[安装](./300/100/README.md)，运行它：

    $ cd flask_opentelemetry/src/example
    $ flask run

打开 Web 浏览器 http&#x3A;//localhost:5000

你会看到一个`To-Do List`应用程序。您可以添加或删除任务。

停止服务器 (CTRL+C) 并在同一终端中运行：

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

Followed by starting the application via the agent (see reference) and keep a text log file:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000 | tee output.log

或者，您可以使用环境变量来配置代理：

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

打开 Web 浏览器 http&#x3A;//localhost:5000

你会看到同样的`To-Do List`应用程序。您可以添加或删除任务。

在终端中，您将看到类似的输出：

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

OpenTelemetry (OTel) 收集器在端口 4317 上运行，因此除超时/连接错误之外的任何其他错误消息（例如`Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.`)，表示应用程序正在运行：

    $ curl localhost:4317
    curl: (1) Received HTTP/0.9 when not allowed

如果收集器没有运行，您会得到：

    $ curl localhost:4317
    curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused

通过此设置，除了开放遥测收集器之外，我们还获得[耶格用户界面](https://github.com/jaegertracing/jaeger-ui)运行在<http://0.0.0.0:16686/>这将有助于可视化通话。

客户端和服务器直接向OTel Collector发送数据；然后，OTel Collector 将数据发送到适当的后端，在此演示中为 Jaeger。

您可以从文本日志文件中 grep 任何 url：

    $ cat output.log | grep http.host

您将看到如下输出：

    "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
    "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
    "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
    ...

The collected telemetry is helpful to understand the amount and latency of the requests over time. 

让我们在 Jaeger UI 中进行过滤（<http://0.0.0.0:16686/>) 对于使用标签的 URL 之一`== url goes here ==`.

更多的

## 100 - 简介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - Building Our Application

看[README.md](./300/README.md)

## 400 - 结论

看[README.md](./400/README.md)
