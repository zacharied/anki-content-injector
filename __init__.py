import codecs
import os

from aqt import mw
from anki.hooks import addHook

STYLESHEET_FILE = '_global.css'

isEnabled = True

def toggleEnabled(action):
    global isEnabled
    isEnabled = not isEnabled
    action.setChecked(isEnabled)

def injectGlobalCss(html, card, context):
    global isEnabled
    if not isEnabled:
        return html

    cssFilePath = os.path.join(mw.col.media.dir(), STYLESHEET_FILE)
    if not os.path.isfile(cssFilePath):
        return html
    
    with open(cssFilePath, 'r', encoding='utf-8') as cssFile:
        return html + '<style>' + cssFile.read() + '</style>'

mw.form.menuTools.addSeparator()
action = mw.form.menuTools.addAction('Use Global CSS')
action.setCheckable(True)
action.setChecked(isEnabled)
action.triggered.connect(lambda _, a=action: toggleEnabled(a))

addHook('prepareQA', injectGlobalCss)
