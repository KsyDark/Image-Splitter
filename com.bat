color 2
::������� ����� �ணࠬ��
taskkill /f /im "Password generator.exe"
:: ����᪠�� �������� �஥�� � ������� pyinstaller
:: �।���⥫쭮 ��⠭���� ����஢�� - ��ਫ�� OEM 866
pyinstaller --onefile --noconsole --icon=ico.ico "Image Splitter.py"
:: ����᪠�� �ணࠬ�� ��᫥ �������樨
cd dist
start "Image Splitter" "Image Splitter.exe"