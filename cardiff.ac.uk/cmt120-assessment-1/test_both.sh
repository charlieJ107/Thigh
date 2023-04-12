cd python
source venv/bin/Activate
python testingFramework_4.py template.py
deactivate
cd ../js
npm --solutionfile=template.js run test-js
cd ..
