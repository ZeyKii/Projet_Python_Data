# 🎵 Analyse de Données sur les Playlists Spotify 🎶

Ce projet vise à réaliser une analyse de données complète sur des playlists à partir du **Spotify Million Playlist Dataset** disponible sur [AIcrowd](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge).

## 🚀 But du Projet
L'objectif principal de ce projet est de comprendre les tendances musicales, les préférences des auditeurs et les schémas de création de playlists à partir d'un vaste ensemble de données de playlists Spotify. 🎧

## 📊 Données Disponibles
Le **Spotify Million Playlist Dataset** contient un million de playlists anonymisées créées par des utilisateurs de Spotify. Chaque playlist est représentée sous forme de fichier JSON contenant des informations sur les titres des chansons, les artistes, les genres, les caractéristiques musicales, etc. 📦

## 🔬 Méthodologie
Nous utiliserons principalement Python ainsi qu'une combinaison de techniques d'analyse exploratoire de données, de visualisation de données, de statistiques descriptives pour extraire des informations significatives des données de playlists Spotify. 🐍📊

## ℹ️ Informations sur le Dataset
Le **Spotify Million Playlist Dataset** contient des données essentielles pour l'analyse de playlists Spotify. Voici quelques détails supplémentaires sur le dataset :
Le MPD contient un million de playlists générées par les utilisateurs. Ces playlists ont été créées entre janvier 2010 et octobre 2017. Chaque playlist dans le MPD contient un titre de playlist, la liste des morceaux (incluant les métadonnées des morceaux), des informations d'édition (heure de la dernière édition, nombre d'éditions de playlist) et d'autres informations diverses sur la playlist.

## 🛠️ Comment le dataset a-t-il été construit
Le Million Playlist Dataset est créé en échantillonnant des playlists parmi les milliards de playlists que les utilisateurs de Spotify ont créées au fil des ans. Les playlists qui répondent aux critères suivants sont sélectionnées de manière aléatoire :

 * Créée par un utilisateur résidant aux États-Unis et âgé d'au moins 13 ans
 * Était une playlist publique au moment où le MPD a été généré
 * Contient au moins 5 morceaux
 * Ne contient pas plus de 250 morceaux
 * Contient au moins 3 artistes uniques
 * Contient au moins 2 albums uniques
 * N'a pas de morceaux locaux (les morceaux locaux sont des morceaux non-Spotify que l'utilisateur a sur son appareil local)
 * A au moins un follower (à l'exception du créateur)
 * A été créée après le 1er janvier 2010 et avant le 1er décembre 2017
 * N'a pas de titre offensant
 * N'a pas de titre orienté vers les adultes si la playlist a été créée par un utilisateur de moins de 18 ans

## 👥 Données démographiques générales des utilisateurs contribuant au MPD

### 🧑‍🤝‍🧑 Genre
 * Homme : 45%
 * Femme : 54%
 * Non spécifié : 0.5%
 * Non binaire : 0.5%

### 📅 Âge
 * 13-17 ans : 10%
 * 18-24 ans : 43%
 * 25-34 ans : 31%
 * 35-44 ans : 9%
 * 45-54 ans : 4%
 * 55 ans et plus : 3%

### 🌍 Pays
 * États-Unis : 100%

 ## 👥 Collaborateurs
- [Médé](https://github.com/MeydeyNc)
- [Telos](https://github.com/Telooss)
- [ZeyKii](https://github.com/ZeyKii)
- [maxime-boizot](https://github.com/maxime-boizot)

### Licence
L'utilisation du Million Playlist Dataset est soumise aux [conditions de licence](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge/challenge_rules).

### Citation
Veuillez citer le [papier](https://dl.acm.org/doi/abs/10.1145/3240323.3240342) suivant lorsque vous utilisez ce dataset :

*Ching-Wei Chen, Paul Lamere, Markus Schedl, and Hamed Zamani. Recsys Challenge 2018: Automatic Music Playlist Continuation. In Proceedings of the 12th ACM Conference on Recommender Systems (RecSys ’18), 2018.*
