# Computer-Vision-Yolo8

Un repository qui contient une application streamlit et un model yolov8 entrainé sur des images de feu de foret pour détecter la fume sur une image.


Le model a était entrainé sur le dataset Wildfire Smoke Dataset bris sur Roboflow.

Le score du model sur le set de validation est de 92.5

Le model peut étre utilisé en tant que détécteur de fumé implementé dans un systeme de video-surveillance qui offrira une détéction rapide d'un eventuel feu naissant.

Il presente pour le moment quelque limites et necessite un entrainement plus approfondie sur une DB plus diversifié et une implementation d'une reconaissance via video.


Pour lancer executez streamlit run app.py ou construisez l'image avec docker.


