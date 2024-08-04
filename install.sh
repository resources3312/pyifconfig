pyinstaller --onefile pyifconfig.py 
rm /usr/bin/pyifconfig
cp ./dist/pyifconfig /usr/bin/
rm -rf build dist *.spec
echo "[+] Pyifconfig was installed"
