import pyautogui
pyautogui.alert('This is a message box with OK button', 'Message')
result = pyautogui.confirm('Do you want to continue?', 'Confirmation', buttons=['OK', 'Cancel'])
if result == 'OK':
    print('User clicked OK')
else:
    print('User clicked Cancel')
