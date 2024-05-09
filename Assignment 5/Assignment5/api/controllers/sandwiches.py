from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, sandwiches):
    # Create a new instance of the Order model with the provided data
    db_sandwiches = models.Osandwiches(
        customer_name=sandwiches.customer_name,
        sandwich_id=sandwiches.sandwich_id,
        description=sandwiches.description
    )
    # Add the newly created Order object to the database session
    db.add(db_sandwiches)
    # Commit the changes to the database
    db.commit()

    db.refresh(db_sandwiches)

    return db_sandwiches


def read_all(db: Session):
    return db.query(models.sandwiches).all()


def read_one(db: Session, sandwiches_id):
    return db.query(models.sandwiches).filter(models.sandwiches.id == sandwiches_id).first()


def update(db: Session, sandwiches_id, sandwiches):
    # Query the database for the specific order to update
    db_sandwiches = db.query(models.sandwiches).filter(models.sandwiches.id == sandwiches_id)
    # Extract the update data from the provided 'order' object
    update_data = sandwiches.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_sandwiches.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated order record
    return db_sandwiches.first()


def delete(db: Session, sandwiches_id):
    # Query the database for the specific order to delete
    db_sandwiches = db.query(models.sandwiches).filter(models.sandwiches.id == sandwiches_id)
    # Delete the database record without synchronizing the session
    db_sandwiches.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
