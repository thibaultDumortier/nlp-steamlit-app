def count_sentences(txt:str) -> str:
    split_on_period = txt.split(". ")
    split_on_exclam = [x.split("! ") for x in split_on_period]
    final_split = [x.split("? ") for s in split_on_exclam for x in s]
    return len([x for s in final_split for x in s])