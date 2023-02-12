from pymongo import MongoClient# define the schema

booking_schema = {
  "customer_id": object,
  "room_id": str,
  "add_ons": list,
  "room_price": float,
  "total_amount": float,
  "cancel_status": bool
}
