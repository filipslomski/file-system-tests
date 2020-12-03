from behave import *
from hamcrest import *

from file_system.file_system import FileSystem
from file_system.real_file_system import RealFileSystem

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
    real_file_system: RealFileSystem = context.real_file_system
    for count in range(int(no_of_files)):
        real_file_system.create_file('/')
    for count in range(int(no_of_dirs)):
        real_file_system.create_dir('/')


@then("I should see (?P<no_of_files>.*) file(?:s)? and (?P<no_of_dirs>.*) director(?:y|ies)?")
def assert_files_and_dirs(context, no_of_files, no_of_dirs):
    real_file_system: RealFileSystem = context.real_file_system
    assert_that(int(no_of_files), is_(equal_to(len(real_file_system.get_files('/')))))
    assert_that(int(no_of_dirs), is_(equal_to(len(real_file_system.get_directories('/')))))
