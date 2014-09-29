from sublime_plugin import WindowCommand, TextCommand
from sublime import packages_path, run_command, ENCODED_POSITION
from time import strftime
from os.path import isfile

headerText = """
    _____                _       _                     _
   /  ___|              | |     | |                   | |
   \ `--.  ___ _ __ __ _| |_ ___| |__  _ __   __ _  __| |
    `--. \/ __| '__/ _` | __/ __| '_ \| '_ \ / _` |/ _` |
   /\__/ / (__| | | (_| | || (__| | | | |_) | (_| | (_| |
   \____/ \___|_|  \__,_|\__\___|_| |_| .__/ \__,_|\__,_|
                                      | |
                                      |_|

"""

class OpenScratchpadCommand(WindowCommand):
  def run(self):
    scratchpadFile = packages_path()[:-8]+'scratchpad.txt'
    checkAndFillEmpty(scratchpadFile)
    self.window.open_file(scratchpadFile)

class ScratchpadCommand(WindowCommand):
  def run(self):
    scratchpadFile = packages_path()[:-8]+'scratchpad.txt'
    global headerText
    checkAndFillEmpty(scratchpadFile)
    count = putTimeStamp(scratchpadFile)
    self.window.open_file(scratchpadFile+':'+str(count+1), ENCODED_POSITION)

def checkAndFillEmpty(scratchpadFile):
  global headerText
  if not isfile(scratchpadFile):
    with open(scratchpadFile, "a") as scratchFile:
      scratchFile.write(headerText)

def putTimeStamp(scratchpadFile):
  timeStamp = "\n" + strftime("%c") + " : " + "\n" +"========================" + "\n"
  with open(scratchpadFile, "a") as scratchFile:
      scratchFile.write(timeStamp)
  with open(scratchpadFile) as scratchFile:
    count = sum(1 for line in scratchFile)
  return count
