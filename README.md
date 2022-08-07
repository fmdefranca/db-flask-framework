# flask-bootstrap-template

makre sure to install the pip packages in the pipfile

Powershell
``` powershell
> $env:FLASK_APP = "hello"
> flask run
 * Running on http://127.0.0.1:5000/
 ```

BASH
```bash
$ export FLASK_RUN_PORT=8000
$ flask run
 * Running on http://127.0.0.1:8000/
 ```

Then run ```pipenv sync``` to sync the virtual environment, then ```pipenv shell```.

Then navigate to the /static/assets/ folder and run ```npm i``` (make sure you have node and npm installed)

Finally ```flask run```
