python generate.py

cd frontend
python main.py
cd ..
cp frontend/output/runs.py backend/generated/runs.py
 
pybricksdev run ble backend/main.py