"""System module."""
from fastapi.responses import JSONResponse
from Tickets.config.logs_config import APP_LOGGER as log
from Tickets.tools.paggination import paggination

def log_error(error_description, status):
    """A dummy docstring."""
    log.error(error_description)
    return JSONResponse(status_code=status, content=error_description)

def log_debug(debug_description, status):
    """A dummy docstring."""
    log.debug(debug_description)
    return JSONResponse(status_code=status, content=debug_description)

def respuesta_info(info_description, status):
    """A dummy docstring."""
    log.info(info_description)
    return JSONResponse(status_code=status, content=info_description)

async def pagg(collection,filter):
    query_res, metadata = await paggination(
            collection,
            0,
            1000,
            filter,
            return_id=True,
            sort_key="created_at",
            sort_direction=-1)
    return query_res