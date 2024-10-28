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

Suivi de:

    opentelemetry-instrument \
      --traces_exporter console \
      --metrics_exporter console \
      --logs_exporter console \
      --service_name todo \
      flask run -p 5000

Vous pouvez également utiliser des variables d'environnement pour configurer l'agent :

    OTEL_SERVICE_NAME=todo \
    OTEL_TRACES_EXPORTER=console \
    OTEL_METRICS_EXPORTER=console \
    OTEL_LOG_EXPORTER=console
    OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317
    opentelemetry-instrument \
        flask run -p 5000

Ouvrez un navigateur Web sur http&#x3A;//localhost:5000

Tu verras la même chose`To-Do List`application. Vous pouvez ajouter ou supprimer des tâches.

Mais sur le port 4317, le serveur OpenTelemetry écoute.

## 100 - Introduction

Voir[README.md](./100/README.md)

## 200 - Exigences

Voir[README.md](./200/README.md)

## 300 - Construire notre application

Voir[README.md](./300/README.md)

## 400 - Conclusion

Voir[README.md](./400/README.md)
