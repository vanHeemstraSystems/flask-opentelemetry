燒瓶開孔遙測

# Flask 開放遙測

> OpenTelemetry (OTel) 是一個開源、供應商中立的可觀測性框架，旨在與任何後端系統配合使用。它提供標準化的 API、庫和工具來收集遙測數據，例如指標、日誌和追蹤。本演講旨在為在 Flask 中使用 OpenTelemetry 提供一個起點。

[參考](./REFERENCES.md)

**執行摘要**

後[安裝](./300/100/README.md)，運行它：

    $ cd flask_opentelemetry/src/example
    $ flask run

開啟 Web 瀏覽器 http&#x3A;//localhost:5000

你會看到一個`To-Do List`應用程式.您可以新增或刪除任務。

停止伺服器 (CTRL+C) 並在同一終端機中運作：

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

接下來透過代理程式啟動應用程式（請參閱參考資料）並保留文字日誌檔案：

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000 | tee output.log

或者，您可以使用環境變數來配置代理：

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console \
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317 \
    OTEL_EXPORTER_OTLP_INSECURE=true \
    opentelemetry-instrument \
        flask run -p 5000 | tee output.log

開啟 Web 瀏覽器 http&#x3A;//localhost:5000

你會看到同樣的`To-Do List`應用程式.您可以新增或刪除任務。

但在連接埠 4317 上，OpenTelemetry 伺服器正在偵聽。

收集器在連接埠 4317 上運行，因此除逾時/連接錯誤之外的任何其他錯誤訊息（例如`Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.`)，表示應用程式正在運行：

    $ curl localhost:4317
    curl: (1) Received HTTP/0.9 when not allowed

如果收集器沒有運行，您會得到：

    $ curl localhost:4317
    curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused

透過此設置，除了開放遙測收集器之外，我們還獲得[耶格使用者介面](https://github.com/jaegertracing/jaeger-ui)運行在<http://0.0.0.0:16686/>這將有助於可視化通話。

客戶端和伺服器直接向OTel Collector發送資料；
然後，OTel Collector 將資料傳送到適當的後端，在此示範中為 Jaeger。

您可以從文字日誌檔案中 grep 任何 url：

    $ cat output.log | grep http.url

收集的遙測資料有助於了解一段時間內請求的數量和延遲。讓我們在 Jaeger UI 中進行過濾（<http://0.0.0.0:16686/>) 對於使用標籤的 URL 之一`url goes here`.

## 100 - 簡介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 建立我們的應用程式

看[README.md](./300/README.md)

## 400 - 結論

看[README.md](./400/README.md)
