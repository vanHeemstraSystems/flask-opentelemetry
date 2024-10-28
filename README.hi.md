फ्लास्क-ओपनटेलीमेट्री

# फ्लास्क ओपनटेलीमेट्री

> ओपन टेलीमेट्री (ओटेल) एक ओपन-सोर्स, विक्रेता-तटस्थ अवलोकन ढांचा है जिसे किसी भी बैकएंड सिस्टम के साथ काम करने के लिए डिज़ाइन किया गया है। यह मेट्रिक्स, लॉग और ट्रेस जैसे टेलीमेट्री डेटा एकत्र करने के लिए मानकीकृत एपीआई, लाइब्रेरी और टूल प्रदान करता है। इस वार्ता का उद्देश्य फ्लास्क में ओपनटेलीमेट्री के साथ काम करने के लिए एक प्रारंभिक बिंदु प्रदान करना है।

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
    OTEL_EXPORTER_OTLP_INSECURE=true \
    opentelemetry-instrument \
        flask run -p 5000 | tee output.log

http&#x3A;//localhost:5000 पर एक वेब ब्राउज़र खोलें

तुम्हें वैसा ही दिखेगा`To-Do List`अनुप्रयोग। आप कार्य जोड़ या हटा सकते हैं.

लेकिन पोर्ट 4317 पर, ओपनटेलीमेट्री सर्वर सुन रहा है।

कलेक्टर पोर्ट 4317 पर चलता है, इसलिए टाइमआउट/कनेक्शन त्रुटि (जैसे) के अलावा कोई अन्य त्रुटि संदेश।`Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.`), इसका मतलब है कि एप्लिकेशन चल रहा है:

    $ curl localhost:4317
    curl: (1) Received HTTP/0.9 when not allowed

यदि कलेक्टर नहीं चल रहा है तो आपको मिलेगा:

    $ curl localhost:4317
    curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused

इस सेटअप के साथ हमें ओपन टेलीमेट्री कलेक्टर के अलावा भी मिलता है[जैगर यूआई](https://github.com/jaegertracing/jaeger-ui)के अंतर्गत चल रहा है<http://0.0.0.0:16686/>जो कॉल को विज़ुअलाइज़ करने में मदद करेगा।

आप टेक्स्ट लॉगफ़ाइल से किसी भी यूआरएल को ग्रेप कर सकते हैं:

    $ cat output.log | grep http.url

एकत्रित टेलीमेट्री समय के साथ अनुरोधों की मात्रा और विलंबता को समझने में सहायक है। आइए जेगर यूआई में फ़िल्टर करें (<http://0.0.0.0:16686/>) टैग का उपयोग करने वाले यूआरएल में से एक के लिए`url goes here`.

## 100 - परिचय

देखना[README.md](./100/README.md)

## 200 - आवश्यकताएँ

देखना[README.md](./200/README.md)

## 300 - हमारे एप्लिकेशन का निर्माण

देखना[README.md](./300/README.md)

## 400 - निष्कर्ष

देखना[README.md](./400/README.md)
