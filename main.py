from pyodide import create_proxy
from js import document

page_loading = Element("page_loading").element

view_feature = Element("view_feature").element
view_main = Element("view_main").element

x_uncensor = Element("x_uncensor").element
x_artifact = Element("x_artifact").element

view_x_uncensor = Element("view_x_uncensor").element
x_uncensor_ext = Element("x_uncensor_ext").element
x_uncensor_process = Element("x_uncensor_process").element

view_x_artifact = Element("view_x_artifact").element

goto_feature = Element("goto_feature").element
breadcrumb1 = Element("breadcrumb1").element
breadcrumb2 = Element("breadcrumb2").element
x_input = Element("x_input").element

uncensor_dict = {
    "A": "А",
    "a": "а",
    "E": "Е",
    "e": "е",
    "O": "О",
    "o": "о",
    "I": "І",
    "i": "і",
}
uncensor_dict_ext = {
    "B": "В",
    "K": "К",
    "M": "М",
    "H": "Н",
    "P": "Р",
    "p": "р",
    "C": "С",
    "c": "с",
    "T": "Т",
    "y": "у",
    "X": "Х",
    "x": "х",
    "b": "Ь",
    "V": "Ѵ",
    "v": "ѵ",
}

CR = [3.9, 3.5, 3.1, 2.7]
CD = [7.8, 7.0, 6.2, 5.4]
ATK = [5.8, 5.2, 4.7, 4.1]
EM = [23, 21, 19, 16]
ER = [6.5, 5.8, 5.2, 4.5]
HP = [5.8, 5.2, 4.7, 4.1]
DEF = [7.3, 6.6, 5.8, 5.1]
FLAT_ATK = [19.45, 17.51, 15.56, 13.62]
FLAT_HP = [299, 269, 239, 209]
FLAT_DEF = [23, 21, 19, 16]
CD_CMD = [501224, 501223, 501222, 501221]
CR_CMD = [501204, 501203, 501202, 501201]
ATK_CMD = [501064, 501063, 501062, 501061]
EM_CMD = [501244, 501243, 501242, 501241]
ER_CMD = [501234, 501233, 501232, 501231]
HP_CMD = [501034, 501033, 501032, 501031]
DEF_CMD = [501094, 501093, 501092, 501091]
FLAT_ATK_CMD = [501054, 501053, 501052, 501051]
FLAT_HP_CMD = [501024, 501023, 501022, 501021]
FLAT_DEF_CMD = [501084, 501083, 501082, 501081]
ARTIFACT_SET = {
    75004: "Gladiator's Finale",
    77004: "Wanderer's Troupe",
    81004: "Noblesse Oblige",
    82004: "Bloodstained Chivalry",
    88004: "Archaic Petra",
    89004: "Retracing Bolide",
    73004: "Lavawalker",
    80004: "Crimson Witch of Flames",
    72004: "Thundersoother",
    79004: "Thundering Fury",
    93004: "Shimenawa's Reminiscence",
    94004: "Emblem of Severed Fate",
    71004: "Blizzard Strayer",
    90004: "Heart of Depth",
    91004: "Tenacity of the Millelith",
    92004: "Pale Flame",
    95004: "Husk of Opulent Dreams",
    96004: "Ocean-Hued Clam",
    97004: "Vermillion Hereafter",
    98004: "Echoes of an Offering",
    74004: "Maiden Beloved",
    76004: "Viridescent Venerer",
    55004: "Berserker",
    57004: "Instructor",
    59004: "The Exile",
    83004: "Prayers for Illumination",
    84004: "Prayers for Destiny",
    85004: "Prayers for Wisdom",
    86004: "Prayers to Springtime",
    58004: "Gambler",
    62004: "Scholar",
    53004: "Defender's Will",
    51004: "Resolution of Sojourner",
    52004: "Brave Heart",
    56004: "Martial Artist",
    54004: "Tiny Miracle",
    61004: "Lucky Dog",
    60004: "Adventurer",
    63004: "Traveling Doctor",
}
ARTIFACT_PART = {
    40: "Flower of Life",
    20: "Plume of Death",
    50: "Sands of Eon",
    10: "Goblet of Eonothem",
    30: "Circlet of Logos",
}
MAIN_STAT = {
    10001: "HP",
    10002: "HP Percentage",
    10003: "ATK",
    10004: "ATK Percentage",
    10005: "DEF",
    10006: "DEF Percentage",
    10007: "Energy Recharge",
    10008: "Elemental Mastery",
    13007: "Crit Rate",
    13008: "Crit Damage",
    12009: "Healing Bonus",
    15008: "Pyro DMG Bonus",
    15009: "Electro DMG Bonus",
    15010: "Cryo DMG Bonus",
    15011: "Hydro DMG Bonus",
    15012: "Anemo DMG Bonus",
    15013: "Geo DMG Bonus",
    15014: "Dendro DMG Bonus",
    15015: "Physical DMG Bonus",
}


def loading_done():
    page_loading.classList.add("is-hidden")
    show_feature()


def goto_feature_click(event):
    show_feature()


def show_feature():
    view_feature.classList.remove("is-hidden")
    view_main.classList.add("is-hidden")
    x_input.value = ""
    view_x_uncensor.classList.add("is-hidden")
    view_x_artifact.classList.add("is-hidden")


def show_main(id):
    view_main.classList.remove("is-hidden")
    view_feature.classList.add("is-hidden")
    breadcrumb1.innerHTML = id.closest(":not(button)").previousElementSibling.innerHTML
    breadcrumb2.innerHTML = id.innerHTML


def x_uncensor_click(event):
    show_main(x_uncensor)
    view_x_uncensor.classList.remove("is-hidden")


def x_artifact_click(event):
    show_main(x_artifact)
    view_x_artifact.classList.remove("is-hidden")


def x_uncensor_process_click(event):
    if x_uncensor_ext.checked:
        ext = dict(uncensor_dict)
        ext.update(uncensor_dict_ext)
        for key in ext:
            x_input.value = x_input.value.replace(key, ext[key])
    else:
        for key in uncensor_dict:
            x_input.value = x_input.value.replace(key, uncensor_dict[key])
    x_input.select()
    document.execCommand("copy")


def main():
    goto_feature.addEventListener("click", create_proxy(goto_feature_click))
    x_uncensor.addEventListener("click", create_proxy(x_uncensor_click))
    x_uncensor_process.addEventListener("click", create_proxy(x_uncensor_process_click))
    x_artifact.addEventListener("click", create_proxy(x_artifact_click))
    loading_done()


main()
