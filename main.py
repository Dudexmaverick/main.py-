from fastapi import FastAPI, HTTPException

app = FastAPI()


Bandas = [
    {'id':1, 'nome': 'legião urbano', 'genero': 'MPB'},
    {'id':2, 'nome': 'mamonas assasinas', 'genero': 'Rock'},
    {'id':3, 'nome': 'cbrj', 'genero': 'Rock nacional '},
    {'id':4, 'nome': 'ira', 'genero': 'Rock nacional'},]
@app.get('/bandas')
async def bandas() -> list[dict]:
    return Bandas



@app.get('/bandas/{band_id}')
async def about(band_id: int)-> dict:
    band = next((b for b in Bandas if b['id'] == band_id),None)
    if band is None: 
        #status code 404
        raise HTTPException(status_code=404, detail='Bandas not found')
    return band

