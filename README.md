# COMMfIA-CTK
Application for creating animated photos (can be used for deep fakes) based on COMMfIA and the CustomTkinter graphics library

## Setup
To install the application you will need Python >3.8. To install missing modules run setup.py and confirm download
```
На ваш компьютер будут установлены модули:
    - ffmpeg-python 
    - imageio 
    - imageio-ffmpeg 
    - matplotlib 
    - numpy 
    - pandas 
    - python-dateutil 
    - pytz 
    - PyYAML 
    - scikit-image 
    - scikit-learn
    - scipy 
    - torch 
    - torchvision 
    - tqdm
    - customtkiner
      
    Вы согласны? д/н
```

The libraries are installed with the command:
```os.system("pip install ffmpeg-python imageio imageio-ffmpeg matplotlib numpy pandas python-dateutil pytz PyYAML scikit-image scikit-learn scipy torch torchvision tqdm customtkiner")```,
so it may not work on other systems other than Windows

## Usage 
For the application to work, you need to install checkpoint (https://drive.google.com/drive/folders/1PyQJmkdCsAkOYwUyaj_l-l0as-iLDgeH) or click on the download button in the program window.

There are the following models to choose from:
 - bair-256 
 - fashion-256 
 - mgif-256 
 - nemo-256 
 - taichi-256 
 - taichi-adv-256 
 - vox-256 
 - vox-adv-256


For faces the model vox-256/vox-adv-256 is used

**The Checkpoint name must match the model name!**

### Preservation
If you save a file to the same directory several times, the file will be overwritten!

## Image
![image](https://github.com/bolgaro4ka/COMMfIA-CTK/assets/123888141/131ce3b1-1b3b-4724-8010-3bb825fdb3a8)

## Examples
### Taichi Dataset
![image](https://github.com/AliaksandrSiarohin/first-order-model/blob/master/sup-mat/face-swap.gif?raw=true)
### Fashion Dataset
![image](https://github.com/AliaksandrSiarohin/first-order-model/blob/master/sup-mat/fashion-teaser.gif?raw=true)
### MGIF Dataset
![image](https://github.com/AliaksandrSiarohin/first-order-model/blob/master/sup-mat/mgif-teaser.gif?raw=true)
### VoxCeleb Dataset
![image](https://github.com/AliaksandrSiarohin/first-order-model/blob/master/sup-mat/vox-teaser.gif?raw=true)
## Links
 - COMMfIA - https://github.com/AliaksandrSiarohin/first-order-model

### Created by Bolgaro4ka (Nikita Fedosov)
