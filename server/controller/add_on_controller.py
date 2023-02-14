from service.add_on_services import AddonService
class AddonController:
    def get_all_add_ons(self):
      try:
        add_on_list=AddonService.get_all_add_ons()
        resp=[]
        for add_on in add_on_list:  
            resp.append({
          # 'id': add_on["id"],
          'name': add_on["name"],
          'price' : add_on["price"]
        })
        return resp
      except Exception as e:
        return str(e)
