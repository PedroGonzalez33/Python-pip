import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def get_list():
    return '''
    <h1> Hola soy peter33 </h1>
    <p> Hi i'm peter33 </p>
    '''

@app.get('/contact')
def get_list():
    return {'name':'peter33 :)'}
    
def run():
    store.get_product

if __name__ == '__main__':
    run()
