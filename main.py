import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom decorator to print name and version dynamically
def sl(func):
    def wrapper(*args, **kwargs):
        name = kwargs.get('name', 'default_name')
        version = kwargs.get('version', 'default_version')
        logging.info(f"name: {name} and version: {version}")
        return func(*args, **kwargs)
    return wrapper

# This function uses custom decorator
@sl
def my_function(name=None, version=None):
    return f"This function is used to call custom decorator with name: {name} and version: {version}"

# Map API call to use custom decorator based on given header
def api_call_function(header):
    if header == "application.json":
        return my_function(name="application.json", version="2.0")
    elif header == "application.xml":
        return my_function(name="application.xml", version="3.0")
    else:
        return my_function()

def main():
    # This can be used to call the function
    api_call_function("application.json")
    api_call_function("application.xml")
    api_call_function("")

if __name__ == '__main__':
    main()