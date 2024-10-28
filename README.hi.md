फ्लास्क-ओपनटेलीमेट्री

# फ्लास्क ओपनटेलीमेट्री

> ओपन टेलीमेट्री (ओटेल) एक ओपन-सोर्स, विक्रेता-तटस्थ अवलोकन ढांचा है जिसे किसी भी बैकएंड सिस्टम के साथ काम करने के लिए डिज़ाइन किया गया है। यह मेट्रिक्स, लॉग और ट्रेस जैसे टेलीमेट्री डेटा एकत्र करने के लिए मानकीकृत एपीआई, लाइब्रेरी और टूल प्रदान करता है। इस वार्ता का उद्देश्य फ्लास्क में ओपनटेलीमेट्री के साथ काम करने के लिए एक प्रारंभिक बिंदु प्रदान करना है।

[संदर्भ](./REFERENCES.md)

**Executive Summary**

बाद[इंस्टालेशन](./300/100/README.md), इसे इसके साथ चलाएँ:

    $ cd flask_opentelemetry/src/example
    $ flask run

http&#x3A;//localhost: 5000 पर एक वेब ब्राउज़र खोलें

एक अलग टर्मिनल विंडो में चलाएँ:

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

के बाद:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 8080

## 100 - परिचय

देखना[README.md](./100/README.md)

## 200 - आवश्यकताएँ

देखना[README.md](./200/README.md)

## 300 - Building Our Application

देखना[README.md](./300/README.md)

## 400 - निष्कर्ष

देखना[README.md](./400/README.md)
