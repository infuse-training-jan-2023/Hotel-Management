from service.add_on_services import AddonService
class AddonController:
    @staticmethod
    def create_response(add_on_list):
      resp=[]
      for add_on in add_on_list:  
            resp.append({
          'name': add_on["name"],
          'price' : add_on["price"]
        })
      return resp

    @staticmethod
    def get_all_add_ons():
      try:  
        return AddonController.create_response(AddonService.get_all_add_ons())
      except Exception as e:
        return str(e)

    
