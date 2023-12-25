$path = "C:\Honours\Projects\Testing-Neural-Networks"

cd $path
python -m venv venv
venv\Scripts\activate.ps1

pip install pygame
pip install torch torchvision
pip install matplotlib 
pip install ipython

deactivate
Exit