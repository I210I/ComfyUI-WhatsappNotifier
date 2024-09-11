import pywhatkit

class WhatsappNotify:
    @classmethod
    def INPUT_TYPES(cls):
        inputs = {
            "required": {
                "Index": ("INT", {}),
                "Number": ("STRING", {}),  
                "Message": ("STRING", {})
            }
        }
        return inputs

    RETURN_TYPES = ("INT",) 
    RETURN_NAMES = ("RETURN VALUE",)
    FUNCTION = "sendMessage"
    CATEGORY = "Whatsapp/Notify"

    def sendMessage(self, Index ,Number, Message):
        if not Number.startswith("+"):
            raise ValueError("The phone number needs start with '+'.")
        pywhatkit.sendwhatmsg_instantly(Number, Message + " Index at {}".format(Index))
        return Index
