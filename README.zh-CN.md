烧瓶开孔遥测

# Flask 开放遥测

> OpenTelemetry (OTel) is an open-source, vendor-neutral observability framework designed to work with any backend system. It provides standardized APIs, libraries, and tools to collect telemetry data, such as metrics, logs, and traces. This talk is intended to provide a starting point for working with OpenTelemetry in Flask.

[参考](./REFERENCES.md)

**执行摘要**

后[安装](./300/100/README.md)，运行它：

    $ cd flask_opentelemetry/src/example
    $ flask run

打开 Web 浏览器 http&#x3A;//localhost:5000

停止服务器 (CTRL+C) 并在同一终端中运行：

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

其次是：

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 8080

或者，您可以使用环境变量来配置代理：

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:8080
    opentelemetry-instrument \
        flask run

## 100 - 简介

看[README.md](./100/README.md)

## 200 - 要求

See [README.md](./200/README.md)

## 300 - 构建我们的应用程序

看[README.md](./300/README.md)

## 400 - 结论

看[README.md](./400/README.md)
