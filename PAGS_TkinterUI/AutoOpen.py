import win32api
import win32con
import sys
sys.setrecursionlimit(1000000)
 
name = 'smartRFS'
path = 'C:\Smart_RFS\Smart_RFS.exe'
 
KeyName = r'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
 
try:
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
    win32api.RegCloseKey(key)
except:
    print('error！')
print('success！')