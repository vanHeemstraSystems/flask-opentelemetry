फ्लास्क-ओपनटेलीमेट्री

# फ्लास्क ओपनटेलीमेट्री

> ओपनटेलीमेट्री (ओटेल) एक ओपन-सोर्स, विक्रेता-तटस्थ अवलोकन ढांचा है जिसे किसी भी बैकएंड सिस्टम के साथ काम करने के लिए डिज़ाइन किया गया है। यह मेट्रिक्स, लॉग और ट्रेस जैसे टेलीमेट्री डेटा एकत्र करने के लिए मानकीकृत एपीआई, लाइब्रेरी और टूल प्रदान करता है। इस वार्ता का उद्देश्य फ्लास्क में ओपनटेलीमेट्री के साथ काम करने के लिए एक प्रारंभिक बिंदु प्रदान करना है।

[संदर्भ](./REFERENCES.md)

**कार्यकारी सारांश**

बाद[इंस्टालेशन](./300/100/README.md), इसे इसके साथ चलाएँ:

    $ cd flask_opentelemetry/src/example
    $ flask run

http&#x3A;//localhost:5000 पर एक वेब ब्राउज़र खोलें

आप एक देखेंगे`To-Do List`अनुप्रयोग। आप कार्य जोड़ या हटा सकते हैं.

सर्वर बंद करें (CTRL+C) और उसी टर्मिनल में चलाएँ:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

इसके बाद एजेंट के माध्यम से एप्लिकेशन शुरू करें (संदर्भ देखें) और एक टेक्स्ट लॉग फ़ाइल रखें:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000 | tee output.log

वैकल्पिक रूप से, आप एजेंट को कॉन्फ़िगर करने के लिए पर्यावरण चर का उपयोग कर सकते हैं:

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

http&#x3A;//localhost:5000 पर एक वेब ब्राउज़र खोलें

तुम्हें वैसा ही दिखेगा`To-Do List`अनुप्रयोग। आप कार्य जोड़ या हटा सकते हैं.

टर्मिनल में, आपको आउटपुट समान दिखाई देगा:

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

ओपनटेलीमेट्री (ओटेल) कलेक्टर पोर्ट 4317 पर चलता है, इसलिए टाइमआउट/कनेक्शन त्रुटि (जैसे) के अलावा कोई अन्य त्रुटि संदेश।`Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.`), इसका मतलब है कि एप्लिकेशन चल रहा है:

    $ curl localhost:4317
    curl: (1) Received HTTP/0.9 when not allowed

यदि ओटेल कलेक्टर नहीं चल रहा है तो आपको यह मिलेगा:

    $ curl localhost:4317
    curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused

इस सेटअप के साथ हमें ओटेल कलेक्टर के अलावा भी मिलता है[जैगर यूआई](https://github.com/jaegertracing/jaeger-ui)के अंतर्गत चल रहा है<http://0.0.0.0:16686/>जो कॉल को विज़ुअलाइज़ करने में मदद करेगा। वैकल्पिक यूआई जो समर्थित हैं वे हैं`Prometheus`और`ZipKin`.

क्लाइंट और सर्वर सीधे ओटेल कलेक्टर को डेटा भेजते हैं; ओटेल कलेक्टर इस डेमो में डेटा को उचित बैकएंड पर भेजता है`Jaeger`.

आप टेक्स्ट लॉगफ़ाइल से किसी भी यूआरएल को ग्रेप कर सकते हैं:

    $ cat output.log | grep http.host

आपको एक आउटपुट दिखाई देगा जैसे:

    "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
    "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
    "http.host": "5000-vanheemstra-flaskopente-6nzougkueau.ws-eu116.gitpod.io",
    ...

एकत्रित टेलीमेट्री समय के साथ अनुरोधों की मात्रा और विलंबता को समझने में सहायक है।

आइए जेगर यूआई में फ़िल्टर करें (<http://0.0.0.0:16686/>) टैग का उपयोग करने वाले यूआरएल में से एक के लिए`== url goes here ==`.

अधिक

## 100 - Introduction

देखना[README.md](./100/README.md)

## 200 - आवश्यकताएँ

देखना[README.md](./200/README.md)

## 300 - हमारे एप्लिकेशन का निर्माण

देखना[README.md](./300/README.md)

## 400 - निष्कर्ष

देखना[README.md](./400/README.md)
