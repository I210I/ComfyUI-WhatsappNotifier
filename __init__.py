from .WhatsappNotify import WhatsappNotify

NODE_CLASS_MAPPINGS = {
    "whatsappNotify": WhatsappNotify 
}

NODE_DISPLAY_NAMES_MAPPINGS = {
    "whatsappNotify": "Whatsapp Notify Node" 
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAMES_MAPPINGS']