télémétrie à ouverture de flacon

# Flacon OpenTelemetry

> OpenTelemetry (OTel) est un framework d'observabilité open source et indépendant du fournisseur, conçu pour fonctionner avec n'importe quel système backend. Il fournit des API, des bibliothèques et des outils standardisés pour collecter des données de télémétrie, telles que des métriques, des journaux et des traces. Cette présentation est destinée à fournir un point de départ pour travailler avec OpenTelemetry dans Flask.

[Références](./REFERENCES.md)

**Résumé exécutif**

Après[installation](./300/100/README.md), exécutez-le avec :

    $ cd flask_opentelemetry/src/example
    $ flask run

Ouvrez un navigateur Web sur http&#x3A;//localhost:5000

Vous verrez un`To-Do List`application. Vous pouvez ajouter ou supprimer des tâches.

Arrêtez le serveur (CTRL+C) et dans le même terminal exécutez :

    $ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

Suivi du démarrage de l'application via l'agent (voir référence) et de la conservation d'un fichier journal texte :

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000 | tee output.log

Vous pouvez également utiliser des variables d'environnement pour configurer l'agent :

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console \
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317 \
    OTEL_EXPORTER_OTLP_INSECURE=true \
    opentelemetry-instrument \
        flask run -p 5000 | tee output.log

Ouvrez un navigateur Web sur http&#x3A;//localhost:5000

Tu verras la même chose`To-Do List`application. Vous pouvez ajouter ou supprimer des tâches.

Mais sur le port 4317, le serveur OpenTelemetry écoute.

Le collecteur s'exécute sur le port 4317, donc tout autre message d'erreur qu'une erreur de délai d'attente/de connexion (par ex.`Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 2s.`), signifie que l'application est en cours d'exécution :

    $ curl localhost:4317
    curl: (1) Received HTTP/0.9 when not allowed

Si le collecteur ne fonctionne pas, vous obtenez :

    $ curl localhost:4317
    curl: (7) Failed to connect to localhost port 4317 after 0 ms: Connection refused

Avec cette configuration, en plus du collecteur de télémétrie ouvert, nous obtenons également[Interface utilisateur Jaeger](https://github.com/jaegertracing/jaeger-ui)courir sous<http://0.0.0.0:16686/>ce qui aidera à visualiser les appels.

Le client et le serveur envoient des données directement au collecteur OTel ;
Le collecteur OTel envoie ensuite les données au backend approprié, dans cette démo Jaeger.

Vous pouvez récupérer n'importe quelle URL du fichier journal texte :

    $ cat output.log | grep http.url

The collected telemetry is helpful to understand the amount and latency of the requests over time. Let’s filter in Jaeger UI (<http://0.0.0.0:16686/>) pour l'une des URL utilisant la balise`url goes here`.

## 100 - Introduction

Voir[README.md](./100/README.md)

## 200 - Exigences

Voir[README.md](./200/README.md)

## 300 - Construire notre application

Voir[README.md](./300/README.md)

## 400 - Conclusion

Voir[README.md](./400/README.md)
