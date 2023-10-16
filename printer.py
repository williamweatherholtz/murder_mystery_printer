import os

from plot import Character, Event

from dataclasses import dataclass

from pylatex import Document, Command, Section, Subsection
from pylatex.utils import italic, NoEscape, bold

@dataclass
class TextPrintable:
    text: str
    xpos: int
    ypos: int
    private: bool = False
    logo_fn: str = ''
    just_name: bool = False
    character_name: str = ''
    act: int = 0





class Printer:
    def __init__(self, fn, characters= list[Character]):
        self.fn = fn
        self.characters = characters
        
        self.margin = 72
        self.text_margin = 150
        
    def fill_document(self, doc):
        """Add a section, a subsection and some text to the document.

        :param doc: the document
        :type doc: :class:`pylatex.document.Document` instance
        """
        with doc.create(Section('A section')):
            doc.append('Some regular text and some ')
            doc.append(italic('italic text. '))

            with doc.create(Subsection('A subsection')):
                doc.append('Also some crazy characters: $&#{}')
        
    def make_document(self, year=None):

        # initializing variables with values
        if year is not None:
            documentTitle = f'Murder Mystery Characters {year}'
            
        
        # maybe somebody's murder mystery has different # of acts
        actnums = sorted(set(e.act for character in self.characters for e in character.events))
        

        # Document with `\maketitle` command activated
        doc = Document('latex_' + self.fn)

        doc.preamble.append(Command('title', 'Awesome Title'))
        doc.preamble.append(Command('author', 'Anonymous author'))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.append(NoEscape(r'\maketitle'))

        self.fill_document(doc)

        doc.generate_pdf(clean=True, clean_tex=False)
        
        return

        # Add stuff to the document
        with doc.create(Section('A second section')):
            doc.append('Some text.')

        doc.generate_pdf('basic_maketitle2', clean_tex=False)
        tex = doc.dumps()  # The document as string in LaTeX syntax
    
        return
        
        with open(fn, 'w') as latek_writer:        
            # populates page from the bottom up, remember that. i.e. (0, 0) is bottom left corner of the page
            for act in actnums:
                for c in sorted(self.characters, key = lambda c: c.name):
                    # if this character has nothing to do this act, there's nothing to print
                    if len(c.events) == 0:
                        continue
                                        
                    length_left = PAGE_LENGTH - y_position
                    estimated_height = len(c.events)*30
                    if estimated_height > length_left:
                        pdf.showPage()
                        y_position = y_initial_position
                    
                    # draw logo, & name on left-hand side
                    pdf.drawImage(c.logo_fn, LOGO_X-100, y_position+30, height=50, preserveAspectRatio=True,  mask='auto')#, anchor='l')
                    pdf.drawString(LOGO_X, y_position, f'{c.name} - Act {act}')
                    
                    max_evts = len([e for e in c.events if e.act == act])
                    
                    
                    
                    for i, e in enumerate(e for e in c.events if e.act == act):
                        if e.private:
                            pdf.drawImage('symbols/private.png', x=x_position-40, y=y_position-10, width=30, height=30, mask='auto', preserveAspectRatio=True)                        
                        
                        pdf.drawString(x_position, y_position, text = f'{max_evts-i}. {e.desc}')
                        y_position += Y_INCREMENT
                    latek_writer.write('}\n')
                    pdf.line(30, y_position+20, 550, y_position+20)
                    
                    # each act and character gets a name heading
                    y_position += Y_INCREMENT
        
        '''
        with open(fn, 'w') as latek_writer:        
            # populates page from the bottom up, remember that. i.e. (0, 0) is bottom left corner of the page
            for act in actnums:
                for c in sorted(self.characters, key = lambda c: c.name):
                    if len(c.events) == 0:
                        continue
                    
                    # custom command + opening brace for events
                    write_string = '\charact{' + c.name + '}{' + str(act) + '}{' + c.logo_fn + '}{'
                    latek_writer.write(write_string)#f'\charact\{{c.name}/}/{{act}/}/{{c.logo_fn}/}')
                    
                    length_left = PAGE_LENGTH - y_position
                    estimated_height = len(c.events)*30
                    if estimated_height > length_left:
                        pdf.showPage()
                        y_position = y_initial_position
                    
                    # draw logo, & name on left-hand side
                    pdf.drawImage(c.logo_fn, LOGO_X-100, y_position+30, height=50, preserveAspectRatio=True,  mask='auto')#, anchor='l')
                    pdf.drawString(LOGO_X, y_position, f'{c.name} - Act {act}')
                    
                    max_evts = len([e for e in c.events if e.act == act])
                    
                    
                    
                    for i, e in enumerate(e for e in c.events if e.act == act):
                        if e.private:
                            latek_writer.write('\privateitem{')
                            #pdf.drawImage('symbols/private.png', x=x_position-40, y=y_position-10, width=30, height=30, mask='auto', preserveAspectRatio=True)
                        else:
                            latek_writer.write('\publicitem{')
                        
                        latek_writer.write(e.desc + '}\n\n')
                        
                        #print (max_evts, i)
                        pdf.drawString(x_position, y_position, text = f'{max_evts-i}. {e.desc}')
                        y_position += Y_INCREMENT
                    latek_writer.write('}\n')
                    pdf.line(30, y_position+20, 550, y_position+20)
                    
                    # each act and character gets a name heading
                    y_position += Y_INCREMENT
            '''
        pdf.showPage()
        pdf.save()



if __name__ == '__main__':
    
    c1 = Character(name='Snow White', logo_fn='logos/char1.png', events=[Event('Private last thing', act=3, private=True), Event('first thing', act=1, private=False),Event('Private thing also in 1st act', act=1, private=True), Event('Private middle thing', act=2, private=True)])
    c2 = Character(name='Ursela', logo_fn='logos/char2.png', events=[Event('last thing', act=3, private=True), Event('first thing', act=1, private=False), Event('Middle thing', act=2, private=True)])
    p = Printer(characters=[c1, c2], fn='test')
    
    #print (p.characters)
    p.make_document()