from sublime_plugin import WindowCommand, TextCommand
from sublime import cache_path, run_command, ENCODED_POSITION
from time import strftime
from os.path import isfile
from threading import Thread

scratchpadFile = cache_path()[:-5]+'scratchpad.txt'

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

class OpenscratchpadCommand(WindowCommand):
  def run(self):
    global scratchpadFile
    checkAndFillEmpty()
    self.window.open_file(scratchpadFile)

class ScratchpadCommand(WindowCommand):
  def run(self):
    global scratchpadFile, headerText
    checkAndFillEmpty()
    count = putTimeStamp()
    self.window.open_file(scratchpadFile+':'+str(count+1), ENCODED_POSITION)

def checkAndFillEmpty():
  global scratchpadFile, headerText
  if not isfile(scratchpadFile):
    with open(scratchpadFile, "a") as scratchFile:
      scratchFile.write(headerText)

def putTimeStamp():
  global scratchFile
  timeStamp = "\n" + strftime("%c") + " : " + "\n" +"========================" + "\n"
  with open(scratchpadFile, "a") as scratchFile:
      scratchFile.write(timeStamp)
  with open(scratchpadFile) as scratchFile:
    count = sum(1 for line in scratchFile)
  return count
