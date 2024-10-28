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

接下来通过代理启动应用程序（请参阅参考资料）并保留文本日志文件：

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
    OTEL_EXPORTER_OTLP_INSECURE=true \
    opentelemetry-instrument \
        flask run -p 5000 | tee output.log

打开 Web 浏览器 http&#x3A;//localhost:5000

你会看到同样的`To-Do List`应用程序。您可以添加或删除任务。

但在端口 4317 上，OpenTelemetry 服务器正在侦听。

收集器在端口 4317 上运行，因此除超时/连接错误之外的任何其他错误消息（例如`Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.`)，表示应用程序正在运行：

    $ curl localhost:4317
    curl: (1) Received HTTP/0.9 when not allowed

如果收集器没有运行，您会得到：

    $ curl localhost:4317
    curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused

通过此设置，除了开放遥测收集器之外，我们还获得[耶格用户界面](https://github.com/jaegertracing/jaeger-ui)运行在<http://0.0.0.0:16686/>这将有助于可视化通话。

您可以从文本日志文件中 grep 任何 url：

    $ cat output.log | grep http.url

收集的遥测数据有助于了解一段时间内请求的数量和延迟。让我们在 Jaeger UI 中进行过滤（<http://0.0.0.0:16686/>) 对于使用标签的 URL 之一`url goes here`.

## 100 - 简介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 构建我们的应用程序

看[README.md](./300/README.md)

## 400 - 结论

看[README.md](./400/README.md)
