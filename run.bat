@echo off
cls
python generate.py

cd frontend
python main.py
cd ..
copy frontend\output\runs.py backend\runs.py

cd backend
pybricksdev run ble main.py
