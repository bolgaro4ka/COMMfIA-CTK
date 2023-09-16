import os

print("""На ваш компьютер будут установлены модули:
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
      
    Вы согласны? д/н """, end="")

quest=input()
if quest == "д" or quest == "y":
    os.system(
        "pip install ffmpeg-python imageio imageio-ffmpeg matplotlib numpy pandas python-dateutil pytz PyYAML scikit-image scikit-learn"
        " scipy torch torchvision tqdm customtkiner")
else: print("Установка была завершена пользователем!")