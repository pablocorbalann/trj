# This file contains all the configurations and functions that are
# needed to load and parse the files. For example the configuration 
# file.
import yaml
import os
import decorators

def load_configuration():
    """
    This function is used to load the configuration (~/configuration.yaml)
    using the YAML Python module.

    Returns
    -------
    configuration: structure
        The Yaml file setted up as a structure.
    """
    route = os.path.abspath("configuration.yaml")
    try:
        with open(route, "r") as f:
            yaml_file = yaml.load(f, Loader=yaml.FullLoader)
            return yaml_file
    except FileNotFoundError as e:
        print(f"""
Can't run the app. The configuration couldn't be loaded
        
{e}
        
Remember to run the app as:
        
    python server/server.py

Instead of 
        
    python sevrer.py
""")
        decorators.exit(1)

if __name__ == "__main__":
    print(load_configuration())
