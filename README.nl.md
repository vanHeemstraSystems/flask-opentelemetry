kolf-opentelemetrie

# Kolf OpenTelemetrie

> OpenTelemetry (OTel) is een open-source, leveranciersneutraal observatieframework dat is ontworpen om met elk backend-systeem te werken. Het biedt gestandaardiseerde API's, bibliotheken en hulpmiddelen voor het verzamelen van telemetriegegevens, zoals statistieken, logboeken en sporen. Deze lezing is bedoeld om een ​​startpunt te bieden voor het werken met OpenTelemetry in Flask.

[Referenties](./REFERENCES.md)

**Samenvatting**

Na[installatie](./300/100/README.md), voer het uit met:

    $ cd flask_opentelemetry/src/example
    $ flask run

Open een webbrowser op http&#x3A;//localhost: 5000

Stop de server (CTRL+C) en voer in dezelfde terminal uit:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

Gevolgd door:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 8080

Als alternatief kunt u omgevingsvariabelen gebruiken om de agent te configureren:

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:8080
    opentelemetry-instrument \
        flask run

## 100 - Inleiding

Zien[README.md](./100/README.md)

## 200 - Vereisten

Zien[README.md](./200/README.md)

## 300 - Onze applicatie bouwen

See [README.md](./300/README.md)

## 400 - Conclusie

Zien[README.md](./400/README.md)
