def prepare_gifts(gifts: list[str]) -> list[str]:
  gifts = list(set(gifts))
  return sorted(gifts)