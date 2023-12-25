from Empolyee_hour_directory.Models.Entry import Entry

class Worker:
    def __init__(self, name):
        self.id = None
        self.name = name
        self.entries = []
    
    def serialize_Worker(Obj):
        print("IsInstance", type(Obj))
        if isinstance(Obj, Worker):
            print("Yes")
            entries = []
            for entry in Obj.entries:
                print(entry)
                entries.append(Entry.serialize(entry))

            return {'worker_id': Obj.id, 'name': Obj.name, 'entries': entries}
    
    def serialize_all_workers(Obj):
        return {'worker_id': Obj.id, 'name': Obj.name}
