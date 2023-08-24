def burcarOrden(veterinaria,idOrden):
    for orden in veterinaria.ordenes:
        if orden.id == idOrden:
            return orden
    return False