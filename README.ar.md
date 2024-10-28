قارورة مفتوحة القياس

# قارورة القياس عن بعد المفتوحة

> OpenTelemetry (OTel) هو إطار عمل مفتوح المصدر وقابل للمراقبة محايد للبائع مصمم للعمل مع أي نظام خلفي. وهو يوفر واجهات برمجة التطبيقات والمكتبات والأدوات القياسية لجمع بيانات القياس عن بعد، مثل المقاييس والسجلات والتتبعات. تهدف هذه المحادثة إلى توفير نقطة بداية للعمل مع OpenTelemetry في Flask.

[مراجع](./REFERENCES.md)

**ملخص تنفيذي**

بعد[تثبيت](./300/100/README.md)، قم بتشغيله باستخدام:

    $ cd flask_opentelemetry/src/example
    $ flask run

افتح متصفح الويب على http&#x3A;//localhost:5000

سوف ترى أ`To-Do List`برنامج. يمكنك إضافة أو حذف المهام.

أوقف الخادم (CTRL+C) وفي نفس المحطة قم بتشغيل:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

تليها:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000

وبدلاً من ذلك، يمكنك استخدام متغيرات البيئة لتكوين الوكيل:

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317
    opentelemetry-instrument \
        flask run -p 5000

افتح متصفح الويب على http&#x3A;//localhost:5000

سوف ترى نفس الشيء`To-Do List`برنامج. يمكنك إضافة أو حذف المهام.

ولكن على المنفذ 4317، يستمع خادم OpenTelemetry.

## 100- مقدمة

يرى[README.md](./100/README.md)

## 200 - المتطلبات

يرى[README.md](./200/README.md)

## 300 – بناء تطبيقنا

يرى[README.md](./300/README.md)

## 400 - الخاتمة

يرى[README.md](./400/README.md)
