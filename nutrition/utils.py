def serialize_model(model):
    return {column.name: getattr(model, column.name) for column in model.__table__.columns}
