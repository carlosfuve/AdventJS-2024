function inBox(box: string[]): boolean {

    if (!(box[0].replace('#','') === '' && box[box.length-1].replace('#','') === '')) return false

    for (const line of box.slice(1,-1)){
        if (line.slice(1,-1).includes('*')) return true
    }
    
    return false
}