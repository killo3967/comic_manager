import os

def cleanFrame(fmcode):    
    cleancode = fmcode.replace('\t', '    ')
    cleancode = cleancode.replace('m_', '')
    cleancode = cleancode.replace('    # Virtual event handlers, overide them in your derived class', '')
    return cleancode   


def fixFrame(prjDir, filename):
    fmcode = ""
    srcFile = os.path.join(prjDir, filename + '.py')

    with open(srcFile, 'r') as f:
        for line in f:
            if line.startswith(('# -*- coding: utf-8 -*- ')):
                fmcode += "# %s.py" % filename
            elif 'true' in line:
                line = line.replace('true', 'True')
                fmcode += line           
            elif line.startswith(('import wx.xrc')):
                pass
            elif line.startswith(('##')):
                pass
            elif line.startswith(('class')):
                lineSp = line.split(' ')
                frameName = lineSp[1]
                fmcode += line
            elif line.startswith(('    def __init__( self, parent ):')):
                fmcode += '    def __init__( self ):\n'
            elif line.startswith(('        wx.Frame.__init__')):
                line = line.replace('parent', 'None')
                fmcode += line
            elif line.startswith(('    def __del__( self ):')):
                pass
            elif line.startswith(('        pass')):
                fmcode += '        # ------------ Add widget program settings\n\n'
                fmcode += '        # ------------ Call Populates\n\n'
                fmcode += '        self.Show()\n\n'
                fmcode += '        # ------------ Event handlers'
            else:
                fmcode += line

    # ----- add main loop
    # fmcode += 'if __name__ == "__main__":\n'
    # fmcode += '    app = wx.App(False)\n'
    # fmcode += '    frame = %s()\n' % frameName
    # fmcode += '    app.MainLoop()\n'

    cleancode = cleanFrame(fmcode)   
    outFile = os.path.join(prjDir, filename + 'BK.py')

    with open(outFile, 'w') as f:
        f.write(cleancode)

    return cleancode

prjDir = r"D:\SCRIPTS\PYTHON\comic_manager\OC"
filename = "comic_manager"

print('Cleaning descode file: %s' % (filename + 'BK.py'))
outStat = fixFrame(prjDir, filename)
print('Clean descode file and save in src folder %s.' % filename)
