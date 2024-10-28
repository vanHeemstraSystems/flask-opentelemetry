matraz-opentelemetria

# Flask OpenTelemetría

> OpenTelemetry (OTel) es un marco de observabilidad de código abierto y de proveedor neutral diseñado para funcionar con cualquier sistema backend. Proporciona API, bibliotecas y herramientas estandarizadas para recopilar datos de telemetría, como métricas, registros y seguimientos. Esta charla pretende proporcionar un punto de partida para trabajar con OpenTelemetry en Flask.

[Referencias](./REFERENCES.md)

**Resumen ejecutivo**

Después[instalación](./300/100/README.md), ejecútelo con:

    $ cd flask_opentelemetry/src/example
    $ flask run

Abra un navegador web en http&#x3A;//localhost: 5000

En una ventana de terminal separada, ejecute:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

Seguido por:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 8080

## 100 - Introducción

Ver[README.md](./100/README.md)

## 200 - Requisitos

Ver[README.md](./200/README.md)

## 300 - Construyendo nuestra aplicación

Ver[README.md](./300/README.md)

## 400 - Conclusión

Ver[README.md](./400/README.md)
