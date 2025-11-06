@echo off
echo =========================
echo  Auto Git Push Started
echo =========================

cd /d D:\AIML_Python_Learning

git add .
git commit -m "Auto update"
git push

echo.
echo ✅ All changes pushed to GitHub!
echo Press any key to exit...
pause > nul
