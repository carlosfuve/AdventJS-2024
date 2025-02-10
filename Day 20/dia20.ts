function fixGiftList(received: string[], expected: string[]): { missing: Record<string, number>, extra: Record<string, number> } {
    const resMiss: Record<string, number> = {};
    const resExt: Record<string, number> = {};

    const agruparRegRecibidos: Record<string, number> = received.reduce((acc, reg) => {
        acc[reg] = (acc[reg] || 0) + 1;
        return acc;
    }, {} as Record<string, number>);

    const agruparRegEsperados: Record<string, number> = expected.reduce((acc, reg) => {
        acc[reg] = (acc[reg] || 0) + 1;
        return acc;
    }, {} as Record<string, number>);

    for (const [regalo, nReg] of Object.entries(agruparRegRecibidos)) {
        const nHay = expected.filter(reg => reg === regalo).length;
        const resta = nReg - nHay;

        if (resta > 0) {
            resExt[regalo] = resta;
        }

        if (resta >= 0) {
            delete agruparRegEsperados[regalo];
        } else {
            agruparRegEsperados[regalo] = Math.abs(resta);
        }
    }

    for (const [regaloE, nRegE] of Object.entries(agruparRegEsperados)) {
        resMiss[regaloE] = nRegE;
    }

    return {
        missing: resMiss,
        extra: resExt
    };
}
