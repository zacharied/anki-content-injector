import os

from aqt import mw
from anki.hooks import addHook

config = mw.addonManager.getConfig(__name__)
isEnabled = config['startEnabled']

def toggleEnabled(action):
    global isEnabled
    isEnabled = not isEnabled
    action.setChecked(isEnabled)

def injectGlobalCss(html, card, context):
    global isEnabled
    global config

    if not isEnabled:
        return html

    style = ''
    for f in config['cssFiles']:
        cssFilePath = os.path.join(mw.col.media.dir(), f)
        if not os.path.isfile(cssFilePath):
            continue
        with open(cssFilePath, 'r', encoding='utf-8') as cssFile:
            style += '<style>' + cssFile.read() + '</style>'

    if config['loadAtHead'] == True:
        return style + html
    else:
        return html + style
    
mw.form.menuTools.addSeparator()
action = mw.form.menuTools.addAction('Use Global CSS')
action.setCheckable(True)
action.setChecked(isEnabled)
action.triggered.connect(lambda: toggleEnabled(action))

addHook('prepareQA', injectGlobalCss)
