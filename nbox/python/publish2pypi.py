import os

package = "twine"

try:
    __import__(package)
except:
    os.system("pip install " + package)

os.system('if [ -d "dist" ]; then rm -Rf dist; fi')

# Remember change version number for upload new version
os.system('python setup.py sdist bdist_wheel')
os.system('twine upload dist/*')