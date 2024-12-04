def mobiles(**kwargs):
    print(kwargs.get("name"))
    print(kwargs['price'])
    
mobiles(name="One plus",price=32000,display="amoled")