قارورة مفتوحة القياس

# قارورة القياس عن بعد المفتوحة

> OpenTelemetry (OTel) هو إطار عمل مفتوح المصدر وقابل للمراقبة محايد للبائع مصمم للعمل مع أي نظام خلفي. وهو يوفر واجهات برمجة التطبيقات والمكتبات والأدوات القياسية لجمع بيانات القياس عن بعد، مثل المقاييس والسجلات والتتبعات. تهدف هذه المحادثة إلى توفير نقطة بداية للعمل مع OpenTelemetry في Flask.

-   [مسرد](./GLOSSARY.md)
-   [مراجع](./REFERENCES.md)

**ملخص تنفيذي**

بعد[تثبيت](./300/100/README.md)، قم بتشغيله باستخدام:

    $ cd flask_opentelemetry/src/example
    $ flask run

افتح متصفح الويب على http&#x3A;//localhost:5000

سوف ترى أ`To-Do List`برنامج. يمكنك إضافة أو حذف المهام.

أوقف الخادم (CTRL+C) وفي نفس المحطة قم بتشغيل:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

يليه بدء التطبيق عبر الوكيل (انظر[مرجع](https://opentelemetry.io/docs/instrumentation/python/automatic/#configuring-the-agent)) واحتفظ بملف سجل نصي:

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
    ELASTIC_APM_SERVER_ENDPOINT=0.0.0.0:4317 \
    ELASTIC_APM_SECRET_TOKEN=secret \
    OTEL_EXPORTER_OTLP_INSECURE=true \
    opentelemetry-instrument \
        flask run -p 5000 | tee output.log

افتح متصفح الويب على http&#x3A;//localhost:5000

سوف ترى نفس الشيء`To-Do List`برنامج. يمكنك إضافة أو حذف المهام.

في المحطة، سترى الإخراج على حد سواء:

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

يعمل مُجمع OpenTelemetry (OTel) على المنفذ 4317، لذا فإن أي رسالة خطأ أخرى غير خطأ المهلة/الاتصال (على سبيل المثال.`Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.`)، يعني أن التطبيق قيد التشغيل:

    $ curl localhost:4317
    curl: (1) Received HTTP/0.9 when not allowed

إذا لم يكن مجمع OTel قيد التشغيل، فستحصل على:

    $ curl localhost:4317
    curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused

مع هذا الإعداد، بالإضافة إلى OTel Collector، نحصل أيضًا على[واجهة المستخدم جايجر](https://github.com/jaegertracing/jaeger-ui)يركض تحت<http://0.0.0.0:16686/> which will help in visualizing the calls. Alternative UIs that are supported are `Prometheus`و`ZipKin`.

يرسل العميل والخادم البيانات مباشرة إلى OTel Collector؛ يقوم جامع OTel بعد ذلك بإرسال البيانات إلى الواجهة الخلفية المناسبة، في هذا العرض التوضيحي`Jaeger`.

يمكنك الحصول على أي عناوين URL من ملف السجل النصي:

    $ cat output.log | grep http.host

سترى إخراجًا مثل:

    "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
    "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
    "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
    ...

يعد القياس عن بعد الذي تم جمعه مفيدًا لفهم مقدار الطلبات ووقت الاستجابة لها بمرور الوقت.

دعونا نقوم بالتصفية في Jaeger UI (<http://0.0.0.0:16686/>) لأحد عناوين URL التي تستخدم العلامة`== url goes here ==`.

أكثر

## 100- مقدمة

يرى[README.md](./100/README.md)

## 200 - المتطلبات

يرى[README.md](./200/README.md)

## 300 – بناء تطبيقنا

يرى[README.md](./300/README.md)

## 400 - الخاتمة

يرى[README.md](./400/README.md)
