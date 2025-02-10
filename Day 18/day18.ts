function findInAgenda(agenda: string, phone:string): Record<string,string> | null {
    const agendaSplit = agenda.split("\n");
    const resultDict: Record<string, string> = {}
    const phoneRegex = /\+\d+-\d+-\d+-\d+/;

    for (const line of agendaSplit){
        if (line.includes(phone)){
            if (Object.keys(resultDict).length === 0){
                const inicio = line.indexOf("<");
                const fin = line.indexOf(">");

                if (inicio !== -1 && fin !== -1){
                    resultDict["name"] = line.slice(inicio + 1, fin);
                    const newLine = line.slice(0, inicio) + line.slice(fin + 2);
                    resultDict["address"] = newLine.replace(phoneRegex, "").trim();
                }
            }
            else {
                return null;
            }
        }
    }

    return Object.keys(resultDict).length === 0 ? null : resultDict;
}