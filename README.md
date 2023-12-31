# SYOCART - Projet IoT

SYOCART est un système conçu pour étudier et optimiser en temps réel les conditions de température afin d'améliorer la conservation des aliments. Le nom "SYOCART" est un acronyme :
- **SY**stem of **O**ptimizing and **C**onserving **A**liment in **R**eal **T**ime.

## Aperçu

SYOCART vise à fournir une solution complète pour surveiller et optimiser les conditions de température cruciales pour la conservation des aliments. Le système combine l'apprentissage automatique, la collecte de données IoT et la surveillance en temps réel pour garantir que les aliments restent dans des conditions optimales en termes de qualité et de sécurité.

## Table des matières

- [Service AI (Classificateur d'images TensorFlow avec une application web Flask)](#service-ai-classificateur-dimages-tensorflow-avec-une-application-web-flask)
- [Service REST avec Django (Tableau de bord de données ESP32 DHT)](#service-rest-avec-django-tableau-de-bord-de-donnees-esp32-dht)
- [Service série (Surveillance des données USB dans GCP)](#service-serie-surveillance-des-donnees-usb-dans-gcp)
- [Structure du répertoire](#structure-du-repertoire)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contributeurs](#contributeurs)
- [Licence](#licence)

...

## Objectifs du système

Les objectifs principaux de SYOCART comprennent :

- **Optimisation de la température en temps réel :** Utiliser l'apprentissage automatique et l'IA pour analyser et optimiser les conditions de température pour le stockage des aliments.

- **Prise de décision basée sur les données :** Collecter des données à partir des capteurs ESP32 DHT et des sources USB pour prendre des décisions éclairées sur la conservation des aliments.

- **Tableau de bord convivial :** Présenter des données pertinentes via un tableau de bord convivial construit avec Django, permettant aux utilisateurs de surveiller et de gérer le système efficacement.

## Dépendances

- Nécessite Python 3.10 et 3.8
- Arduino IDE et certaines bibliothèques associées
- VS Code ou tout autre éditeur de code ou IDE
- Redistribuables Visual Studio 2015-2019
- Docker (Non nécessaire)
- ESP32
- DHT11
- Caméra

## Utilisation

- Consultez les fichiers source pour le code.

## Contributeurs

- Ibrahim Lahlou
- Hicham Ghouch

## Pipeline Architecture

![image](https://github.com/IbLahlou/syocart_app/assets/105231126/8f9426e0-0ead-4a52-9dba-4cabdf21e711)
