# Slum Mapping
### Slums mapping from pretrained CNN network on VHR and MR imagery 

This repository is aimed to provide step by step methodology from creation of dataset to classifying slums through transfer learning.
Slums detection in cities of major developing nations has been experimented with different methods and techniques. Majority of which are difficult to reiterate and follow to implement in different cities. While Very High Resolution datasets have primarily been used for such tasks, some studies have also worked with Medium Resolution datasets in Slum detection and mapping. This study utilised both VHR and MR datasets and compared the results. We demonstrate a simple step by step approach to map slums. Similar procedure can be followed for slum or any landform detection in any city.

#### The Methodology consists of primarily four subtasks. 
> - ##### Creation of Training dataset using Google Earth Platform.
The training dataset is manually created with the help of Google Earth Pro. GE provides interface to quickly zoom and locate the various classes. In this study, the samples for four classes such as (a) Slums (b) Non-Slums/Other Built (c) Green, and (d) Water are created with the help of the *path* tool. The paths created by the path tool is saved as a lat/long pair as a csv file. Two satellite imageries are used in this study (a) Pleiades: 0.5m resolution and (b) Sentinel: 10m resolution. Natural color (RGB) bands are used from Pleiades while False Color (8,4,3) are used from Sentinel product. The lat/long pair are treated as centre pixel of the varying-size image patches such as 10x10 pixel (Sentinel) and 200x200 pixel (Pleiades) created as a part of the final dataset. 

> - ##### Generation of transfer Values from Inception Network.
The image patches created for each satellite dataset are rescaled to 128x128 pixels and fed into the Inception Network to collect 1024-D transfer values. These values can be plotted in 2-D representation with the help of t-SNE and PCA to visualize the samples of classes or formation of clusters.

> - ##### Creation of Simple Neural Network to classify the inputs.
For each satellite dataset, corresponding transfer values are then fed into the Neural Network for further train the clssifier to detect 4 classes.

> - ##### Mapping the outputs and evaluation of the Model.
To map the prediction results in entire area of the city, each satellite map is sequentially clipped and fed into the Inception Net to collect transfer values which are further fed into the Neural Network to obtain model results. These results are then mapped over the corresponding satellite patches.

