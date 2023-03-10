from src import db
from src.models.tables import Group
from sqlalchemy import update

class GroupType(Group):
    ...
    
class CreateGroup:
    def __init__(self, dto: GroupType) -> None:
        self.data = Group(
        dto.create_date, 
        dto.group_name, 
        dto.leader_name, 
        dto.vice_leader_name, 
        dto.street_number,
        dto.district,
        dto.city,
        dto.sectorId, 
        dto.host_name, 
        dto.meeting_day, 
        dto.meeting_time, 
        dto.enabled
          )

    def save(self):
        db.session.add(self.data)
        db.session.commit()


class UpdateGroup:
    def __init__(self, dto: GroupType, group_id: int ) -> None:
        self.data = Group(
        dto.create_date, 
        dto.group_name, 
        dto.leader_name, 
        dto.vice_leader_name, 
        dto.street_number,
        dto.district,
        dto.city,
        dto.sectorId, 
        dto.host_name, 
        dto.meeting_day, 
        dto.meeting_time, 
        dto.enabled
          )
        self.group_id = group_id
    def find_data(self):
        return Group.query.get(self.group_id)

    def update(self):
        stmt = update(Group).where(Group.id ==  self.group_id).values(
              self.data
         )
        db.session.execute(stmt)
        db.session.commit()
