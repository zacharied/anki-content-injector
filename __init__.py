import os

from aqt import mw
from anki.hooks import addHook

config = mw.addonManager.getConfig(__name__)
isEnabled = config['startEnabled']

EXT_TO_TAG = {
    '.html': 'div',
    '.css': 'style',
    '.js': 'script'
}

def toggleEnabled(action):
    global isEnabled
    isEnabled = not isEnabled
    action.setChecked(isEnabled)

def injectGlobalContent(html, card, context):
    global isEnabled
    global config

    if not isEnabled:
        return html

    inject = ''
    for f in config['injectFiles']:
        injectFilePath = os.path.join(mw.col.media.dir(), f)
        _, ext = os.path.splitext(injectFilePath)
        if not os.path.isfile(injectFilePath):
            continue
        with open(injectFilePath, 'r', encoding='utf-8') as injectFile:
            if not ext in EXT_TO_TAG:
                continue
            inject += '<{0}>{1}</{0}>'.format(EXT_TO_TAG[ext], injectFile.read())

    if config['injectAtTail'] == True:
        return html + inject
    else:
        return inject + html
    
mw.form.menuTools.addSeparator()
action = mw.form.menuTools.addAction('Inject Global Content')
action.setCheckable(True)
action.setChecked(isEnabled)
action.triggered.connect(lambda: toggleEnabled(action))

addHook('prepareQA', injectGlobalContent)
