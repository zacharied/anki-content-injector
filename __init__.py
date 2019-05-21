import os

from aqt import mw, qt
from aqt.clayout import CardLayout
from anki.hooks import addHook, wrap
from aqt.utils import showInfo
import PyQt5

EXT_TO_TAG = {
    '.html': 'div',
    '.css': 'style',
    '.js': 'script'
}

config = mw.addonManager.getConfig(__name__)

isEnabled = config['startEnabled']
isEnabledPreview = isEnabled

def toggleEnabled(action):
    global isEnabled
    isEnabled = not isEnabled
    action.setChecked(isEnabled)

def setPreviewEnabled(check, editor):
    global isEnabledPreview
    isEnabledPreview = check.isChecked()
    editor.redraw()

def availableInjectFiles():
    global config
    files = []
    for f in config['injectFiles']:
        if os.path.isfile(os.path.join(mw.col.media.dir(), f)):
            files.append(f)
    return files

def injectGlobalContent(html, card, context):
    global isEnabled
    global config

    if not isEnabled:
        return html
    
    if not isEnabledPreview and (context == 'clayoutQuestion' or context == 'clayoutAnswer'):
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

def clayoutEditorTopArea(editor, _old):
    global isEnabled, isEnabledPreview
    isEnabledPreview = isEnabled

    _ret = _old(editor)

    checkbox = qt.QCheckBox("Inject global content in preview")
    checkbox.setChecked(isEnabled)
    checkbox.stateChanged.connect(lambda: setPreviewEnabled(checkbox, editor))
    editor.topAreaForm.verticalLayout.addWidget(checkbox)

    return _ret

mw.form.menuTools.addSeparator()
action = mw.form.menuTools.addAction('Inject Global Content')
action.setCheckable(True)
action.setChecked(isEnabled)
action.triggered.connect(lambda: toggleEnabled(action))

addHook('prepareQA', injectGlobalContent)

CardLayout.setupTopArea = wrap(CardLayout.setupTopArea, clayoutEditorTopArea, "around")
