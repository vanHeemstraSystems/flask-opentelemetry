Kolben-Open-Telemetrie

# Flasche OpenTelemetry

> OpenTelemetry (OTel) ist ein herstellerneutrales Open-Source-Observability-Framework, das für die Zusammenarbeit mit jedem Backend-System entwickelt wurde. Es bietet standardisierte APIs, Bibliotheken und Tools zum Sammeln von Telemetriedaten wie Metriken, Protokollen und Traces. Dieser Vortrag soll einen Ausgangspunkt für die Arbeit mit OpenTelemetry in Flask bieten.

[Referenzen](./REFERENCES.md)

**Zusammenfassung**

Nach[Installation](./300/100/README.md), führe es aus mit:

    $ cd flask_opentelemetry/src/example
    $ flask run

Öffnen Sie einen Webbrowser unter http&#x3A;//localhost:5000

Stoppen Sie den Server (STRG+C) und führen Sie im selben Terminal Folgendes aus:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

Gefolgt von:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 8080

Alternativ können Sie Umgebungsvariablen verwenden, um den Agenten zu konfigurieren:

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:8080
    opentelemetry-instrument \
        flask run

## 100 - Einführung

Sehen[README.md](./100/README.md)

## 200 – Anforderungen

Sehen[README.md](./200/README.md)

## 300 – Erstellen unserer Anwendung

Sehen[README.md](./300/README.md)

## 400 – Fazit

Sehen[README.md](./400/README.md)
