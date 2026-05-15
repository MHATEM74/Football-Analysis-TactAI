import subprocess
import sys

def install_all_requirements():
    packages = [
        'ultralytics',
        'opencv-python',
        'supervision',
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'pyyaml',
        'pickle-mixin'
    ]

    print("--- يا محمد.. جاري التثبيت الآن (والمرة دي صح!) ---")
    
    for package in packages:
        print(f"جاري تثبيت: {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except Exception as e:
            print(f"❌ مشكلة في {package}: {e}")

    print("\n" + "="*50)
    print("كله تمام يا بطل! المكتبات جاهزة.. شغل main.py وتوكل على الله")
    print("="*50)

if _name_ == "_main_":
    install_all_requirements()