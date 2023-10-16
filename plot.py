
from dataclasses import dataclass, field
    

@dataclass
class Event:
    desc: str
    act: int = None
    private: bool = False


@dataclass
class Character:
    name: str
    logo_fn: str
    events: list[Event] = field(default_factory=list)
    player: str = None
    
    def __add__(self, e: Event):
        self.events.append(e)
        return self
    

if __name__ == '__main__':
    
    c = Character(name='Guy Dude', logo_fn='mylogo.png')
    
    e1 = Event('He kills that girl', act=3, private=True)
    e2 = Event('He puts his shoes on', act=1)
    
    c += e1
    c += e1
    c += e2
    
    print (c)