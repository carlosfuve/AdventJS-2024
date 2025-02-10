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






agenda = "+34-600-123-456 Calle Gran Via 12 <Juan Perez>\nPlaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654\n<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York"

print(find_in_agenda(agenda,'34-600-123-456'))

print(find_in_agenda(agenda,'600-987'))

print(find_in_agenda(agenda,'111'))
print(find_in_agenda(agenda,'1'))