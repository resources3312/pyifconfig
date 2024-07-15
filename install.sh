pyinstaller --onefile pyifconfig.py 
cp ./dist/pyifconfig /usr/bin/
rm -rf build dist *.spec
echo "[+] Pyifconfig was installed"
