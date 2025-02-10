import re

def find_in_agenda(agenda: str, phone: str) -> dict | None:
      agenda_split = agenda.split('\n')
      result_dict = {}
      for line in agenda_split:
        if phone in line:
            if not result_dict:
                inicio = line.find("<")
                fin = line.find(">")  
                result_dict['name'] = line[inicio+1:fin]

                new_line = line[:inicio] + line[fin+2:]
                result_dict['address'] = re.sub(r"\+\d+-\d+-\d+-\d+","",new_line).strip()
            else:
                return None

      return None if not result_dict else result_dict