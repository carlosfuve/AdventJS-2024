function decodeFilename(filename: string): string{
    const idxGuion = filename.indexOf('_') + 1;
    const idxPunto = filename.lastIndexOf('.');
    return filename.substring(idxGuion, idxPunto);
}
