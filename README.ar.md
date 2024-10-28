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

يلي ذلك بدء التطبيق عبر الوكيل (انظر المرجع) والاحتفاظ بملف سجل نصي:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000 | tee output.log

وبدلاً من ذلك، يمكنك استخدام متغيرات البيئة لتكوين الوكيل:

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console \
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317 \
    OTEL_EXPORTER_OTLP_INSECURE=true \
    opentelemetry-instrument \
        flask run -p 5000 | tee output.log

افتح متصفح الويب على http&#x3A;//localhost:5000

سوف ترى نفس الشيء`To-Do List`برنامج. يمكنك إضافة أو حذف المهام.

ولكن على المنفذ 4317، يستمع خادم OpenTelemetry.

يعمل المجمع على المنفذ 4317، لذا فإن أي رسالة خطأ أخرى غير خطأ المهلة/الاتصال (على سبيل المثال.`Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.`)، يعني أن التطبيق قيد التشغيل:

    $ curl localhost:4317
    curl: (1) Received HTTP/0.9 when not allowed

إذا لم يكن المجمع قيد التشغيل، فستحصل على:

    $ curl localhost:4317
    curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused

مع هذا الإعداد، بالإضافة إلى جامع القياس عن بعد المفتوح، نحصل أيضًا على[واجهة المستخدم جايجر](https://github.com/jaegertracing/jaeger-ui)يركض تحت<http://0.0.0.0:16686/>والتي سوف تساعد في تصور المكالمات.

يرسل العميل والخادم البيانات مباشرة إلى OTel Collector؛
يقوم جامع OTel بعد ذلك بإرسال البيانات إلى الواجهة الخلفية المناسبة، في هذا العرض التوضيحي لـ Jaeger.

يمكنك الحصول على أي عناوين URL من ملف السجل النصي:

    $ cat output.log | grep http.url

يعد القياس عن بعد الذي تم جمعه مفيدًا لفهم مقدار الطلبات ووقت الاستجابة لها بمرور الوقت. دعونا نقوم بالتصفية في Jaeger UI (<http://0.0.0.0:16686/>) لأحد عناوين URL التي تستخدم العلامة`url goes here`.

## 100- مقدمة

يرى[README.md](./100/README.md)

## 200 - المتطلبات

يرى[README.md](./200/README.md)

## 300 – بناء تطبيقنا

يرى[README.md](./300/README.md)

## 400 - الخاتمة

يرى[README.md](./400/README.md)
