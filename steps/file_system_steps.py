from behave import *
from hamcrest import *

from file_system.file_system import FileSystem

use_step_matcher("re")


@step(u'I call the (?P<function>.*) function')
def call_function(context, function):
    file_system: FileSystem = context.file_system
    functions = {
        'AddFile': file_system.add_file,
        'AddDir': file_system.add_dir,
        'ChangeDir': file_system.change_dir,
        'DirUp': file_system.dir_up,
        'Pwd': file_system.pwd
    }
    functions[function]()


@given("I have (?P<no_of_dirs>.*) directories and (?P<no_of_files>.*) files in my root directory")
def prepare_files_and_dirs(context, no_of_dirs, no_of_files):
    raise NotImplementedError(u'STEP: Given I have no directories and no files in my root directory')