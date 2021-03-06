from pynwb.spec import NWBNamespaceBuilder
from export_spec import export_spec


def main():
    ns_builder = NWBNamespaceBuilder(doc='{{ cookiecutter.description }}',
                                     name='{{ cookiecutter.namespace }}',
                                     version='{{ cookiecutter.version }}',
                                     author='{{ cookiecutter.author }}',
                                     contact='{{ cookiecutter.email }}')

    # CHANGEME
    # define the new data types
    # compartment_series = NWBGroupSpec(
    #     neurodata_type_def='CompartmentSeries',
    #     neurodata_type_inc='TimeSeries',
    #     doc='Stores continuous data from cell compartments',
    #     links=[
    #         NWBLinkSpec(name='compartments',
    #                     target_type='Compartments',
    #                     doc='metadata about compartments in this CompartmentSeries',
    #                     quantity='?')
    #     ]
    # )

    # CHANGEME
    # add the new data types to this list
    # new_data_types = [compartment_series]
    new_data_types = []

    # CHANGEME
    # Must include types that are used and their namespaces (where to find them)
    # ns_builder.include_type('TimeSeries', namespace='core')

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
