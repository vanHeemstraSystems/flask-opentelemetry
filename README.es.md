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

Seguido por iniciar la aplicación a través del agente (ver referencia) y mantener un archivo de registro de texto:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000 | tee output.log

Alternativamente, puede utilizar variables de entorno para configurar el agente:

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console \
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317 \
    OTEL_EXPORTER_OTLP_INSECURE=true \
    opentelemetry-instrument \
        flask run -p 5000 | tee output.log

Abra un navegador web en http&#x3A;//localhost:5000

Verás lo mismo`To-Do List`aplicación. Puede agregar o eliminar tareas.

Pero en el puerto 4317, el servidor OpenTelemetry está escuchando.

El recopilador se ejecuta en el puerto 4317, por lo que cualquier otro mensaje de error que no sea un error de tiempo de espera/conexión (p. ej.`Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.`), significa que la aplicación se está ejecutando:

    $ curl localhost:4317
    curl: (1) Received HTTP/0.9 when not allowed

Si el recopilador no se está ejecutando, obtienes:

    $ curl localhost:4317
    curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused

Con esta configuración, además del recopilador de telemetría abierto, también obtenemos[Interfaz de usuario de Jaeger](https://github.com/jaegertracing/jaeger-ui)corriendo bajo<http://0.0.0.0:16686/>lo que ayudará a visualizar las llamadas.

Puede recuperar cualquier URL del archivo de registro de texto:

    $ cat output.log | grep http.url

La telemetría recopilada es útil para comprender la cantidad y la latencia de las solicitudes a lo largo del tiempo. Filtremos en Jaeger UI (<http://0.0.0.0:16686/>) para una de las URL que utilizan la etiqueta`url goes here`.

## 100 - Introducción

Ver[README.md](./100/README.md)

## 200 - Requisitos

Ver[README.md](./200/README.md)

## 300 - Construyendo nuestra aplicación

Ver[README.md](./300/README.md)

## 400 - Conclusión

Ver[README.md](./400/README.md)
