import paho.mqtt.publish as mqtt_publish
from fastapi import FastAPI, Request, HTTPException, Form
from Personas.routes.routes import persona
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title="Personas",
    version="1.0.0.0",
    docs_url = "/api/docs",
    redoc_url= "/api/docs"
)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

app.include_router(persona, prefix="/api/personas")


@app.post("/enviar-mqtt/")
async def enviar_mqtt(topic: str = Form(), message: str = Form()):
    print(message)
    print(topic)
    # Configurar opciones de autenticación
    mqtt_username = 'mjproyect'
    mqtt_password = 'gA11lEO1'
    auth = {'username': mqtt_username, 'password': mqtt_password}
    
    # Enviar mensaje al servidor MQTT
    mqtt_broker = '192.168.0.49'
    mqtt_port = 1883
    mqtt_publish.single(topic, payload=message, hostname=mqtt_broker, port=mqtt_port, auth=auth)
    
    return {"message": "Mensaje enviado al servidor MQTT"}