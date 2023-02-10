from add_on_repository import AddonRepository


class AddonAction:
  def __init__(self) -> None:
    self.add_on_repo = AddonRepository()


  def get_all_add_ons(self):
    try:
      
      add_on_list = self.add_on_repo.get_all_add_ons() 
      res = []
       
      for add_on in add_on_list:  
        res.append({
          # 'id': add_on["id"],
          'name': add_on["name"],
          'price' : add_on["price"]
        })
     
      return res
    except Exception as e:
      print(e)
      return {}


  

