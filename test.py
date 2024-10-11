from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from learn import *

def App():
    put_html('<h1>learn python3</h1>')
    popup('hello')
    data = input_group(
        'LODIN',
        [
            input('username',name='name'),
            input('password',name='pass')
        ]
    )

start_server(App, port=1234, debug=True)