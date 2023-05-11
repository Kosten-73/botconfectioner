from tgbot.database.db_api import OrdersUser, db


async def add_order_db(user_id: int, user_name: str, user_phone: str,
                       user_address: str, category: str, subcategory: str, filling: str, value: str, photo: str):
    order = OrdersUser(user_id=user_id, user_name=user_name, user_phone=user_phone,
                       user_address=user_address, category=category, subcategory=subcategory,
                       filling=filling, value=value, photo=photo)
    await order.create()


async def count_orders():
    total = await db.func.count(OrdersUser.order_id).gino.scalar()
    return total


async def select_all_orders():
    orders = await OrdersUser.query.gino.all()
    return [order.to_dict() for order in orders]


async def select_one_order(user_id):
    orders = await OrdersUser.query.where(OrdersUser.user_id == user_id).gino.all()
    return [order.to_dict() for order in orders]

async def delete_order(user_id):
    order = await OrdersUser.query.where(OrdersUser.user_id == user_id).gino.first()
    await order.delete()


async def update_state_order(user_id, accept):
    order = await OrdersUser.query.where(OrdersUser.user_id == user_id).gino.first()
    await order.update(accept=accept).apply()

