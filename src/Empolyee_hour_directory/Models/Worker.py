from Empolyee_hour_directory.Models.Entry import Entry

class Worker:
    def __init__(self, name):
        self.id = None
        self.name = name
        self.entries = []
    
    def serialize_Worker_With_Entity(Obj):
        print("IsInstance", type(Obj))
        if isinstance(Obj, Worker):
            entries = []
            for entry in Obj.entries:
                entries.append(Entry.serialize(entry))
            return {'worker_id': Obj.id, 'name': Obj.name, 'entries': entries}
    
    def serialize_Worker_Without_Entity(Obj):
        return {'worker_id': Obj.id, 'name': Obj.name}
