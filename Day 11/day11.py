def decode_filename(filename: str) -> str:
  idx_guion = filename.index('_') + 1
  idx_punto = filename.rindex('.')
  return filename[idx_guion:idx_punto]