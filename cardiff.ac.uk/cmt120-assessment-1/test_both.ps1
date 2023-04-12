Set-Location python\
venv/Scripts/Activate.ps1
python testingFramework_4.py template.py
deactivate
Set-Location ..\js\
npm --solutionfile=template.js run test-js
Set-Location ..\