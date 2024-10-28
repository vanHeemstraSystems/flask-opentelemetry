قارورة مفتوحة القياس

# قارورة القياس عن بعد المفتوحة

> OpenTelemetry (OTel) is an open-source, vendor-neutral observability framework designed to work with any backend system. It provides standardized APIs, libraries, and tools to collect telemetry data, such as metrics, logs, and traces. This talk is intended to provide a starting point for working with OpenTelemetry in Flask.

[مراجع](./REFERENCES.md)

**ملخص تنفيذي**

بعد[تثبيت](./300/100/README.md)، قم بتشغيله باستخدام:

    $ cd flask_opentelemetry/src/example
    $ flask run

افتح متصفح الويب على http&#x3A;//localhost: 5000

في نافذة طرفية منفصلة قم بتشغيل:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

تليها:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 8080

## 100- مقدمة

يرى[README.md](./100/README.md)

## 200 - المتطلبات

يرى[README.md](./200/README.md)

## 300 – بناء تطبيقنا

يرى[README.md](./300/README.md)

## 400 - الخاتمة

يرى[README.md](./400/README.md)
