import os
import glob
import shutil

def make_dir(tomake):
    root_dir = os.path.abspath('.')
    tomake_dir = os.path.join(root_dir, tomake)
    if not os.path.exists(tomake_dir):
        os.makedirs(tomake_dir)

tomakes = ['code/', 'raw_data/', 'temp_data/', 'model/', 'result/']
for tomake in tomakes:
    make_dir(tomake)

for data in glob.glob('*csv'):
    mv = shutil.move(data, 'raw_data/')

#shutil.move(os.path.abspath(__file__), 'code/')
