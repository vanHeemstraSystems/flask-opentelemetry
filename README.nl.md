kolf-opentelemetrie

# Kolf OpenTelemetrie

> OpenTelemetry (OTel) is een open-source, leveranciersneutraal observatieframework dat is ontworpen om met elk backend-systeem te werken. Het biedt gestandaardiseerde API's, bibliotheken en hulpmiddelen voor het verzamelen van telemetriegegevens, zoals statistieken, logboeken en sporen. Deze lezing is bedoeld om een ​​startpunt te bieden voor het werken met OpenTelemetry in Flask.

[Referenties](./REFERENCES.md)

**Samenvatting**

Na[installatie](./300/100/README.md), voer het uit met:

    $ cd flask_opentelemetry/src/example
    $ flask run

Open een webbrowser op http&#x3A;//localhost:5000

Je ziet een`To-Do List`app. U kunt taken toevoegen of verwijderen.

Stop de server (CTRL+C) en voer in dezelfde terminal uit:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

Gevolgd door het starten van de applicatie via de agent (zie referentie) en het bijhouden van een tekstlogbestand:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000 | tee output.log

Als alternatief kunt u omgevingsvariabelen gebruiken om de agent te configureren:

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console \
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317 \
    OTEL_EXPORTER_OTLP_INSECURE=true \
    opentelemetry-instrument \
        flask run -p 5000 | tee output.log

Open een webbrowser op http&#x3A;//localhost:5000

Je zult hetzelfde zien`To-Do List`app. U kunt taken toevoegen of verwijderen.

Maar op poort 4317 luistert de OpenTelemetry-server.

De collector draait op poort 4317, dus elke andere foutmelding dan een time-out/verbindingsfout (bijv.`Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.`), betekent dat de applicatie actief is:

    $ curl localhost:4317
    curl: (1) Received HTTP/0.9 when not allowed

Als de collector niet actief is, krijgt u:

    $ curl localhost:4317
    curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused

Met deze opstelling krijgen we, naast de open telemetriecollector, ook[Jaeger-gebruikersinterface](https://github.com/jaegertracing/jaeger-ui)onder lopen<http://0.0.0.0:16686/>wat zal helpen bij het visualiseren van de oproepen.

De client en server sturen gegevens rechtstreeks naar de OTel Collector;
De OTel Collector stuurt de gegevens vervolgens naar de juiste backend, in deze demo van Jaeger.

U kunt elke URL uit het tekstlogbestand grep:

    $ cat output.log | grep http.url

De verzamelde telemetrie is nuttig om inzicht te krijgen in de hoeveelheid en latentie van de aanvragen in de loop van de tijd. Laten we filteren in de Jaeger UI (<http://0.0.0.0:16686/>) voor een van de URL's die de tag gebruiken`url goes here`.

## 100 - Inleiding

Zien[README.md](./100/README.md)

## 200 - Vereisten

Zien[README.md](./200/README.md)

## 300 - Onze applicatie bouwen

Zien[README.md](./300/README.md)

## 400 - Conclusie

Zien[README.md](./400/README.md)
