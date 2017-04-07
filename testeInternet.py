import webbrowser


url = 'http://workflow02-evt:8000/EnterpriseConsole/BPMUITemplates/Default/Repository/Site/Login.aspx?_repo=BPM%20Repository%2002&_instanceName=EVERTICAL2&_provtext=Galaxy%20Users[EVERTICAL2]&_prov=galaxyuserprovider'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
##webbrowser.open(chrome_path).open(url)

webbrowser.open('http://workflow02-evt:8000/EnterpriseConsole/BPMUITemplates/Default/Repository/Site/Login.aspx?_repo=BPM%20Repository%2002&_instanceName=EVERTICAL2&_provtext=Galaxy%20Users[EVERTICAL2]&_prov=galaxyuserprovider')

##import webbrowser
##webbrowser.open('http://google.co.kr', new=2)
