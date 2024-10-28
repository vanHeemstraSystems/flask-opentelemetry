kolf-opentelemetrie

# Kolf OpenTelemetrie

> OpenTelemetry (OTel) is an open-source, vendor-neutral observability framework designed to work with any backend system. It provides standardized APIs, libraries, and tools to collect telemetry data, such as metrics, logs, and traces. This talk is intended to provide a starting point for working with OpenTelemetry in Flask.

[Referenties](./REFERENCES.md)

**Samenvatting**

Na[installatie](./300/100/README.md), voer het uit met:

    $ cd flask_opentelemetry/src/example
    $ flask run

Open a web browser at http&#x3A;//localhost:5000

Je ziet een`To-Do List`app. U kunt taken toevoegen of verwijderen.

Stop de server (CTRL+C) en voer in dezelfde terminal uit:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

Gevolgd door:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000

Als alternatief kunt u omgevingsvariabelen gebruiken om de agent te configureren:

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317
    opentelemetry-instrument \
        flask run -p 5000

Open een webbrowser op http&#x3A;//localhost:5000

Je zult hetzelfde zien`To-Do List`app. U kunt taken toevoegen of verwijderen.

Maar op poort 4317 luistert de OpenTelemetry-server.

## 100 - Inleiding

Zien[README.md](./100/README.md)

## 200 - Vereisten

Zien[README.md](./200/README.md)

## 300 - Onze applicatie bouwen

Zien[README.md](./300/README.md)

## 400 - Conclusie

Zien[README.md](./400/README.md)
