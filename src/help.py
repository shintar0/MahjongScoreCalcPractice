import data
import pprint

def ls():
    pprint.pprint(data.DATA)

def calc_point():
    print("●平和が絡むツモあがりは必ず20符 \n"+
        "●平和が絡むロンあがりは必ず30符 \n"+
        "●七対子が絡むあがりは必ず25符(50符) \n"+
        "●平和も七対子も絡まないツモあがりは30符であることが多い \n"+
        "●平和も七対子も絡まないロンあがりは40符であることが多い \n")
