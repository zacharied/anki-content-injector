import os

from aqt import mw, qt
from aqt.clayout import CardLayout
from anki.hooks import addHook, wrap

EXT_TO_TAG = {
    '.html': 'div',
    '.css': 'style',
    '.js': 'script'
}

class ContentInjector():
    def __init__(self):
        self.config = mw.addonManager.getConfig(__name__)
        self.isEnabledGlobal = self.config['startEnabled']
        self.isEnabledPreview = self.isEnabledGlobal

        # Add toggle to menu.
        mw.form.menuTools.addSeparator()
        action = mw.form.menuTools.addAction('Inject Global Content')
        action.setCheckable(True)
        action.setChecked(self.isEnabledGlobal)
        action.triggered.connect(lambda: self.onEnabledGlobalChecked(action))

        # Main hook for inserting content.
        addHook('prepareQA', self.injectContent)

        # Add toggle to clayout editor UI.
        CardLayout.setupMainArea = wrap(CardLayout.setupMainArea, self.myClayoutMainArea, "around")

    # Get files in the injectFiles config that exist.
    def availableInjectFiles(self):
        files = []
        for f in self.config['injectFiles']:
            if os.path.isfile(os.path.join(mw.col.media.dir(), f)):
                files.append(f)
        return files

    # Called when the toggle in the main menu is changed.
    def onEnabledGlobalChecked(self, action):
        self.isEnabledGlobal = action.isChecked()
    
    # Called when the toggle in the clayout editor is changed.
    def onEnabledPreviewChecked(self, action, editor):
        self.isEnabledPreview = action.isChecked()
        editor.redraw()

    # Given the main card HTML, inject the global content into it.
    def injectContent(self, html, card, context):
        if context == 'clayoutQuestion' or context == 'clayoutAnswer':
            if not self.isEnabledPreview:
                return html
        elif not self.isEnabledGlobal:
            return html

        inject = ''
        for f in self.availableInjectFiles():
            with open(f, 'r', encoding='utf-8') as injectFile:
                _, ext = os.path.splitext(f)
                if not ext in EXT_TO_TAG:
                    continue
                inject += '<{0}>{1}</{0}>'.format(EXT_TO_TAG[ext], injectFile.read())

        if self.config['injectAtTail'] == True:
            return html + inject
        else:
            return inject + html

    # Monkey patch to modify the clayout editor UI.
    def myClayoutMainArea(self, editor, _old):
        self.isEnabledPreview = self.isEnabledGlobal

        _ret = _old(editor)

        checkbox = qt.QCheckBox("Inject global content in preview")
        checkbox.setChecked(self.isEnabledPreview)
        checkbox.stateChanged.connect(lambda: self.onEnabledPreviewChecked(checkbox, editor))
        editor.pform.verticalLayout_3.addWidget(checkbox)

        return _ret

ContentInjector()
