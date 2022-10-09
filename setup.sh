VIRTUAL_ENVIRONMENT_DIRECTORY='./.venv'

[ -d "/path/to/dir" ]  && python3 -m venv $VIRTUAL_ENVIRONMENT_DIRECTORY
source $VIRTUAL_ENVIRONMENT_DIRECTORY/bin/activate
pip3 install --upgrade pip
pip3 install --requirement requirements.txt