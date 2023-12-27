from Empolyee_hour_directory.Models.Entry import Entry

class Worker:
    def __init__(self, name, position = "Analyst"):
        self.id = None
        self.name = name
        self.position = position
        self.entries = []
    
    def serialize_Worker_With_Entity(self):
        entries = []
        for entry in self.entries:
            entries.append(Entry.serialize(entry))
        return {'worker_id': self.id, 'name': self.name, 'position': self.position, 'entries': entries}
    
    def serialize_Worker_Without_Entity(self):
        return {'worker_id': self.id, 'name': self.name, 'position': self.position}
