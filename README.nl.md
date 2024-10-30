kolf-opentelemetrie

# Kolf OpenTelemetrie

> OpenTelemetry (OTel) is een open-source, leveranciersneutraal observatieframework dat is ontworpen om met elk backend-systeem te werken. Het biedt gestandaardiseerde API's, bibliotheken en hulpmiddelen voor het verzamelen van telemetriegegevens, zoals statistieken, logboeken en sporen. Deze lezing is bedoeld om een ​​startpunt te bieden voor het werken met OpenTelemetry in Flask.

-   [Glossarium](./GLOSSARY.md)
-   [Referenties](./REFERENCES.md)

**Samenvatting**

Na[installatie](./300/100/README.md), voer het uit met:

    $ cd flask_opentelemetry/src/example
    $ flask run

Open een webbrowser op http&#x3A;//localhost:5000

Je ziet een`To-Do List`app. U kunt taken toevoegen of verwijderen.

Stop de server (CTRL+C) en voer in dezelfde terminal uit:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

Gevolgd door het starten van de applicatie via de agent (zie[referentie](https://opentelemetry.io/docs/instrumentation/python/automatic/#configuring-the-agent)) en houd een tekstlogbestand bij:

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
    ELASTIC_APM_SERVER_ENDPOINT=0.0.0.0:4317 \
    ELASTIC_APM_SECRET_TOKEN=secret \
    OTEL_EXPORTER_OTLP_INSECURE=true \
    opentelemetry-instrument \
        flask run -p 5000 | tee output.log

Open een webbrowser op http&#x3A;//localhost:5000

Je zult hetzelfde zien`To-Do List`app. U kunt taken toevoegen of verwijderen.

In de terminal ziet u dezelfde uitvoer:

     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    127.0.0.1 - - [28/Oct/2024 14:20:33] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [28/Oct/2024 14:20:37] "POST /add HTTP/1.1" 302 -
    127.0.0.1 - - [28/Oct/2024 14:20:37] "GET / HTTP/1.1" 200 -
    {
        "name": "GET /",
        "context": {
            "trace_id": "0xf70da0284034c5ea91a354e82ea3358f",
            "span_id": "0x791d76168f2219ef",
            "trace_state": "[]"
        },
        "kind": "SpanKind.SERVER",
        "parent_id": null,
        "start_time": "2024-10-28T14:20:33.591136Z",
        "end_time": "2024-10-28T14:20:33.598630Z",
        "status": {
            "status_code": "UNSET"
        },
        "attributes": {
            "http.method": "GET",
            "http.server_name": "127.0.0.1",
            "http.scheme": "http",
            "net.host.name": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
            "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
            "net.host.port": 5000,
            "http.target": "/",
            "net.peer.ip": "127.0.0.1",
            "net.peer.port": 48680,
            "http.user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "http.flavor": "1.1",
            "http.route": "/",
            "http.status_code": 200
        },
        "events": [],
        "links": [],
        "resource": {
            "attributes": {
                "telemetry.sdk.language": "python",
                "telemetry.sdk.name": "opentelemetry",
                "telemetry.sdk.version": "1.27.0",
                "service.name": "todo",
                "telemetry.auto.version": "0.48b0"
            },
            "schema_url": ""
        }
    }
    {
        "name": "POST /add",
        "context": {
            "trace_id": "0x1225b9a518cf7ea836eefc4a9ee6d3c0",
            "span_id": "0xa124085da8f4ce10",
            "trace_state": "[]"
        },
        "kind": "SpanKind.SERVER",
        "parent_id": null,
        "start_time": "2024-10-28T14:20:37.643212Z",
        "end_time": "2024-10-28T14:20:37.648385Z",
        "status": {
            "status_code": "UNSET"
        },
        "attributes": {
            "http.method": "POST",
            "http.server_name": "127.0.0.1",
            "http.scheme": "http",
            "net.host.name": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
            "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
            "net.host.port": 5000,
            "http.target": "/add",
            "net.peer.ip": "127.0.0.1",
            "net.peer.port": 42142,
            "http.user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "http.flavor": "1.1",
            "http.route": "/add",
            "http.status_code": 302
        },
        "events": [],
        "links": [],
        "resource": {
            "attributes": {
                "telemetry.sdk.language": "python",
                "telemetry.sdk.name": "opentelemetry",
                "telemetry.sdk.version": "1.27.0",
                "service.name": "todo",
                "telemetry.auto.version": "0.48b0"
            },
            "schema_url": ""
        }
    }
    {
        "name": "GET /",
        "context": {
            "trace_id": "0xf78ac5fe73bea41b6ef6ec50996bd085",
            "span_id": "0x97c2270b6866fe65",
            "trace_state": "[]"
        },
        "kind": "SpanKind.SERVER",
        "parent_id": null,
        "start_time": "2024-10-28T14:20:37.666513Z",
        "end_time": "2024-10-28T14:20:37.669702Z",
        "status": {
            "status_code": "UNSET"
        },
        "attributes": {
            "http.method": "GET",
            "http.server_name": "127.0.0.1",
            "http.scheme": "http",
            "net.host.name": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
            "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
            "net.host.port": 5000,
            "http.target": "/",
            "net.peer.ip": "127.0.0.1",
            "net.peer.port": 42158,
            "http.user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "http.flavor": "1.1",
            "http.route": "/",
            "http.status_code": 200
        },
        "events": [],
        "links": [],
        "resource": {
            "attributes": {
                "telemetry.sdk.language": "python",
                "telemetry.sdk.name": "opentelemetry",
                "telemetry.sdk.version": "1.27.0",
                "service.name": "todo",
                "telemetry.auto.version": "0.48b0"
            },
            "schema_url": ""
        }
    }

De OpenTelemetry (OTel)-collector draait op poort 4317, dus elke andere foutmelding dan een time-out/verbindingsfout (bijv.`Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.`), betekent dat de applicatie actief is:

    $ curl localhost:4317
    curl: (1) Received HTTP/0.9 when not allowed

Als de OTel Collector niet actief is, krijgt u:

    $ curl localhost:4317
    curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused

Met deze opstelling krijgen we, naast de OTel Collector, ook[Jaeger-gebruikersinterface](https://github.com/jaegertracing/jaeger-ui)onderdoor rennen<http://0.0.0.0:16686/>wat zal helpen bij het visualiseren van de oproepen. Alternatieve gebruikersinterfaces die worden ondersteund, zijn dat wel`Prometheus`En`ZipKin`.

De client en server sturen gegevens rechtstreeks naar de OTel Collector; De OTel Collector stuurt de gegevens vervolgens in deze demo naar de juiste backend`Jaeger`.

U kunt elke URL uit het tekstlogbestand grep:

    $ cat output.log | grep http.host

Je zult een uitvoer zien zoals:

    "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
    "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
    "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
    ...

De verzamelde telemetrie is nuttig om inzicht te krijgen in de hoeveelheid en latentie van de aanvragen in de loop van de tijd.

Laten we filteren in de Jaeger UI (<http://0.0.0.0:16686/>) voor een van de URL's die de tag gebruiken`== url goes here ==`.

MEER

## 100 - Inleiding

Zien[README.md](./100/README.md)

## 200 - Vereisten

Zien[README.md](./200/README.md)

## 300 - Onze applicatie bouwen

Zien[README.md](./300/README.md)

## 400 - Conclusie

Zien[README.md](./400/README.md)
