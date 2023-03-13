from src import db
from src.models.tables import Group
from sqlalchemy import update, func


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
        print('test-->',self.group_id )
        stmt = update(Group).where(Group.id == self.group_id).values(
               create_date=  self.data.create_date, 
                group_name = self.data.group_name, 
               leader_name =  self.data.leader_name, 
               vice_leader_name =  self.data.vice_leader_name, 
               street_number = self.data.street_number,
                district = self.data.district,
                city = self.data.city,
                sectorId = self.data.sectorId, 
                host_name = self.data.host_name, 
                meeting_day = self.data.meeting_day, 
                meeting_time = self.data.meeting_time, 
                enabled =  self.data.enabled
         )
        
        
        




        
        db.session.execute(stmt)
        db.session.commit()
    

class FindGroup:
    def __init__(self) -> None:
        ...
    def count_groups(self):
        ...
    ## verificar e testar
    



