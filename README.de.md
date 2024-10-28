Kolben-Open-Telemetrie

# Flasche OpenTelemetry

> OpenTelemetry (OTel) ist ein herstellerneutrales Open-Source-Observability-Framework, das für die Zusammenarbeit mit jedem Backend-System entwickelt wurde. Es bietet standardisierte APIs, Bibliotheken und Tools zum Sammeln von Telemetriedaten wie Metriken, Protokollen und Traces. Dieser Vortrag soll einen Ausgangspunkt für die Arbeit mit OpenTelemetry in Flask bieten.

[Referenzen](./REFERENCES.md)

**Zusammenfassung**

Nach[Installation](./300/100/README.md), führe es aus mit:

    $ cd flask_opentelemetry/src/example
    $ flask run

Öffnen Sie einen Webbrowser unter http&#x3A;//localhost:5000

Sie werden ein sehen`To-Do List`App. Sie können Aufgaben hinzufügen oder löschen.

Stoppen Sie den Server (STRG+C) und führen Sie im selben Terminal Folgendes aus:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

Anschließend starten Sie die Anwendung über den Agenten (siehe Referenz) und führen eine Textprotokolldatei:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000 | tee output.log

Alternatively, you can use environment variables to configure the agent:

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console \
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317 \
    OTEL_EXPORTER_OTLP_INSECURE=true \
    opentelemetry-instrument \
        flask run -p 5000 | tee output.log

Öffnen Sie einen Webbrowser unter http&#x3A;//localhost:5000

Sie werden dasselbe sehen`To-Do List`App. Sie können Aufgaben hinzufügen oder löschen.

Aber auf Port 4317 lauscht der OpenTelemetry-Server.

Der Collector läuft auf Port 4317, sodass jede andere Fehlermeldung als ein Timeout/Verbindungsfehler (z. B.`Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.`), bedeutet, dass die Anwendung ausgeführt wird:

    $ curl localhost:4317
    curl: (1) Received HTTP/0.9 when not allowed

Wenn der Collector nicht läuft, erhalten Sie Folgendes:

    $ curl localhost:4317
    curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused

Mit diesem Setup erhalten wir zusätzlich zum offenen Telemetriekollektor auch[Jaeger UI](https://github.com/jaegertracing/jaeger-ui)unterlaufen<http://0.0.0.0:16686/>Dies hilft bei der Visualisierung der Anrufe.

Client und Server senden Daten direkt an den OTel Collector;
Der OTel Collector sendet die Daten dann an das entsprechende Backend, in dieser Demo Jaeger.

Sie können alle URLs aus der Textprotokolldatei abrufen:

    $ cat output.log | grep http.url

Die gesammelten Telemetriedaten sind hilfreich, um die Menge und Latenz der Anfragen im Zeitverlauf zu verstehen. Lassen Sie uns in der Jaeger-Benutzeroberfläche filtern (<http://0.0.0.0:16686/>) für eine der URLs, die das Tag verwenden`url goes here`.

## 100 - Einführung

See [README.md](./100/README.md)

## 200 – Anforderungen

Sehen[README.md](./200/README.md)

## 300 – Erstellen unserer Anwendung

Sehen[README.md](./300/README.md)

## 400 – Fazit

Sehen[README.md](./400/README.md)
