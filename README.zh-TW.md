燒瓶開孔遙測

# Flask 開放遙測

> OpenTelemetry (OTel) 是一個開源、供應商中立的可觀測性框架，旨在與任何後端系統配合使用。它提供標準化的 API、庫和工具來收集遙測數據，例如指標、日誌和追蹤。本演講旨在為在 Flask 中使用 OpenTelemetry 提供一個起點。

[參考](./REFERENCES.md)

**執行摘要**

後[安裝](./300/100/README.md)，運行它：

    $ cd flask_opentelemetry/src/example
    $ flask run

開啟 Web 瀏覽器 http&#x3A;//localhost:5000

Stop the server (CTRL+C) and in the same terminal run:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

其次是：

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 8080

或者，您可以使用環境變數來配置代理：

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:8080
    opentelemetry-instrument \
        flask run

## 100 - 簡介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 建立我們的應用程式

看[README.md](./300/README.md)

## 400 - 結論

看[README.md](./400/README.md)
