from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Club Rabbit Volley")


# =====================================================
# ARCHIVOS ESTÁTICOS
# =====================================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# =====================================================
# TEMPLATES
# =====================================================

templates = Jinja2Templates(directory="templates")


# =====================================================
# INICIO
# =====================================================

@app.get("/")
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="inicio.html",
        context={
            "active_page": "inicio"
        }
    )


# =====================================================
# NOSOTROS
# =====================================================

@app.get("/nosotros")
async def nosotros(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="nosotros.html",
        context={
            "active_page": "nosotros"
        }
    )


# =====================================================
# PROGRAMAS
# =====================================================

@app.get("/categorias")
async def programas(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="categorias.html",
        context={
            "active_page": "categorias"
        }
    )


# =====================================================
# EVENTOS
# =====================================================

@app.get("/eventos")
async def eventos(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="eventos.html",
        context={
            "active_page": "eventos"
        }
    )


# =====================================================
# GALERÍA
# =====================================================

@app.get("/galeria")
async def galeria(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="galeria.html",
        context={
            "active_page": "galeria"
        }
    )


# =====================================================
# CONTACTO
# =====================================================

@app.get("/contacto")
async def contacto(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contacto.html",
        context={
            "active_page": "contacto"
        }
    )