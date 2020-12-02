from file_system.file_system import FileSystem
from file_system.real_file_system import RealFileSystem
from utilities.data_generator import DataGenerator


def before_all(context):
    _load_configs_and_init_data(context)


def before_feature(context, feature):
    context.feature_tags = feature.tags


def before_scenario(context, scenario):
    context.logger.current_scenario = scenario.name
    context.scenario_tags = scenario.tags


def before_step(context, step):
    context.logger.current_step = step.name


def after_scenario(context, scenario):
    if 'file-system' in scenario.tags + context.feature_tags:
        _clear_the_file_system(context)


def after_step(context, step):
    pass


def after_all(context):
    pass


def _load_configs_and_init_data(context):
    context.data_generator = DataGenerator(context)
    context.file_system = FileSystem(context)
    context.real_file_system = RealFileSystem(context)


def _clear_the_file_system(context):
    context.real_file_system.clear_the_test_bucket()
