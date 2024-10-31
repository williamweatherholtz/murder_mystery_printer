import os

from dataclasses import dataclass, field

import pandas as pd

from pylatex import Document, Command, UnsafeCommand
from pylatex.basic import NewPage
from pylatex.package import Package
from pylatex.base_classes import CommandBase, Arguments
from pylatex.utils import italic, NoEscape, bold
   

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

# these classes form an interface to call custom commands via pylatex.  
# their implementations are found in the latex murdermystery.cls file
class PublicItem(CommandBase):
    _latex_name = 'publicitem'

class PrivateItem(CommandBase):
    _latex_name = 'privateitem'

class CharacterEntry(CommandBase):
    _latex_name = 'charentry'

class Printer:
    def __init__(self, fn, characters:list[Character], doc_class='murdermystery'):
        self.fn = fn
        self.characters = characters
        self.doc_class = doc_class
    
    def analyze(self, fn='analysis.html', clues=True) -> pd.DataFrame:
        acts = set()
        for c in self.characters:
            for e in c.events:
                acts.add(e.act)
        
        data = {}
        index = []
        for act in acts:
            data[f'Act {act}'] = []
            #data['Name'] = []
            for c in self.characters:
                #data['Name'].append(c.name)
                if c.name not in index:
                    index.append(c.name)
                
                # maybe the amount of characters per clue is most meaningful, or maybe it's the # of clues
                if clues:
                    data[f'Act {act}'].append(len([e for e in c.events if e.act == act]))
                else:
                    data[f'Act {act}'].append(sum([len(e.desc) for e in c.events if e.act == act]))
                    
                
        df = pd.DataFrame(data, index=index)
        #if 
        df = df.style.background_gradient(cmap="RdYlGn", vmin=0)#, vmax=4)
        
        df.to_html(fn)
        
        return df
    
    def _add_entry(self, c:Character, events:list[Event], act:int):
        pubs = [e for e in events if not e.private]
        pvts = [e for e in events if e.private]
        
        items = ''
        for e in pubs:
            items += PublicItem(arguments=(e.desc)).dumps()
        for e in pvts:
            items += PrivateItem(arguments=(e.desc)).dumps()
        
        self.doc.append(CharacterEntry( arguments=(c.name.capitalize(), act, c.logo_fn, NoEscape(items))))
                
    def make_document(self, act_new_page=False):
        self.doc = Document(self.fn, documentclass=self.doc_class)
            
        
        # maybe somebody's murder mystery has different # of acts
        actnums = sorted(set(e.act for character in self.characters for e in character.events))
                
        for act in actnums:
            for c in sorted(self.characters, key = lambda c: c.name):
                # if this character has nothing to do this act, there's nothing to print
                if len(c.events) == 0:
                    continue
                
                # wasteful, but concise & quick enough
                act_events = [e for e in c.events if e.act == act]
                
                self._add_entry(c, act_events, act)
            if act_new_page:
                self.doc.append(NewPage())            
        self.doc.generate_pdf(clean=True, clean_tex=True)
        #self.doc.generate_tex()
        

if __name__ == '__main__':
    
    c1 = Character(name='Primary Character', logo_fn='logos/char1.png', events=[Event('Private last thing', act=3, private=True), Event('first thing', act=1, private=False),Event('Private thing also in 1st act', act=1, private=True), Event('Private middle thing', act=2, private=True)])
    
    c2 = Character(name='Ursela', logo_fn='logos/char2.png', events=[Event('last thing', act=3, private=True), Event('first thing', act=1, private=False), Event('Middle thing', act=2, private=True)])
    
    p = Printer(characters=[c1, c2], fn='test')
    
    #print (p.characters)
    p.make_document()