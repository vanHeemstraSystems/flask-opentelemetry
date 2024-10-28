matraz-opentelemetria

# Flask OpenTelemetría

> OpenTelemetry (OTel) es un marco de observabilidad de código abierto y de proveedor neutral diseñado para funcionar con cualquier sistema backend. Proporciona API, bibliotecas y herramientas estandarizadas para recopilar datos de telemetría, como métricas, registros y seguimientos. Esta charla pretende proporcionar un punto de partida para trabajar con OpenTelemetry en Flask.

[Referencias](./REFERENCES.md)

**Resumen ejecutivo**

Después[instalación](./300/100/README.md), ejecútelo con:

    $ cd flask_opentelemetry/src/example
    $ flask run

Abra un navegador web en http&#x3A;//localhost:5000

Verás un`To-Do List`aplicación. Puede agregar o eliminar tareas.

Detenga el servidor (CTRL+C) y en la misma terminal ejecute:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

Seguido por:

    opentelemetry-instrument \
      --traces_exporter console, otlp \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000

Alternativamente, puede utilizar variables de entorno para configurar el agente:

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console, otlp \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317
    opentelemetry-instrument \
        flask run -p 5000

Abra un navegador web en http&#x3A;//localhost:5000

Verás lo mismo`To-Do List`aplicación. Puede agregar o eliminar tareas.

Pero en el puerto 4317...

## 100 - Introducción

Ver[README.md](./100/README.md)

## 200 - Requisitos

See [README.md](./200/README.md)

## 300 - Construyendo nuestra aplicación

Ver[README.md](./300/README.md)

## 400 - Conclusión

Ver[README.md](./400/README.md)
