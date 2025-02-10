function drawTable(data: Array<Record<string, string | number>>): string{
    const nameCols = Object.keys(data[0]);
    const maxLenCols = nameCols.map(col =>
        Math.max(...data.map(row => String(row[col]).length), col.length)
    )

    const separator = "+" + maxLenCols.map(width => "-".repeat(width+2)).join("+") + "+";

    const boxHeader = "| " + nameCols.map((header, i) =>
        header.charAt(0).toUpperCase() + header.slice(1).padEnd(maxLenCols[i])
    ).join(" | ") + " |";

    const rows = data.map(row => 
        "| " + nameCols.map((key, i) => String(row[key]).padEnd(maxLenCols[i])).join(" | ") + " |"
    );

    return [separator, boxHeader, separator, ...rows, separator].join("\n");
}