烧瓶开孔遥测

# Flask 开放遥测

> OpenTelemetry (OTel) 是一个开源、供应商中立的可观测性框架，旨在与任何后端系统配合使用。它提供标准化的 API、库和工具来收集遥测数据，例如指标、日志和跟踪。本演讲旨在为在 Flask 中使用 OpenTelemetry 提供一个起点。

[参考](./REFERENCES.md)

**执行摘要**

后[安装](./300/100/README.md)，运行它：

    $ cd flask_opentelemetry/src/example
    $ flask run

打开 Web 浏览器 http&#x3A;//localhost:5000

You will see a `To-Do List`应用程序。您可以添加或删除任务。

停止服务器 (CTRL+C) 并在同一终端中运行：

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

其次是：

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000

或者，您可以使用环境变量来配置代理：

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317
    opentelemetry-instrument \
        flask run -p 5000

打开 Web 浏览器 http&#x3A;//localhost:5000

你会看到同样的`To-Do List`应用程序。您可以添加或删除任务。

但在端口 4317 上，OpenTelemetry 服务器正在侦听。

## 100 - 简介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 构建我们的应用程序

看[README.md](./300/README.md)

## 400 - 结论

看[README.md](./400/README.md)
