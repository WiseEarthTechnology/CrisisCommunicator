from models import Supply

def update_supply(_quantity, _measurement):
    
    """
    Method to store details into the supply table.
    
    Parameters: quantity, Measurement
    
    rtype: int
    
    """
    
    supply_update = Supply(quantity=_quantity, measurement=_measurement)
    supply_update.save()
    return supply_update.pk
