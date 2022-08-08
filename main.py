import math
import numpy as np
from pyodide import create_proxy
from js import document, console
from collections import Counter
from pyodide.http import pyfetch

page_loading = Element("page_loading").element

view_feature = Element("view_feature").element
view_main = Element("view_main").element

x_uncensor = Element("x_uncensor").element
x_stats = Element("x_stats").element
x_artifact = Element("x_artifact").element

view_x_uncensor = Element("view_x_uncensor").element
x_uncensor_ext = Element("x_uncensor_ext").element
x_uncensor_process = Element("x_uncensor_process").element

view_x_stats = Element("view_x_stats").element
x_stat_uid = Element("x_stat_uid").element
x_stat_process = Element("x_stat_process").element
x_stat_info = Element("x_stat_info").element
x_stat_stats = Element("x_stat_stats").element
x_stat_exploration_name = Element("x_stat_exploration_name").element
x_stat_exploration_info = Element("x_stat_exploration_info").element
x_stat_teapot = Element("x_stat_teapot").element
x_stat_abyss = Element("x_stat_abyss").element
x_stat_abyss_ranks = Element("x_stat_abyss_ranks").element
x_stat_abyss_ranks_mp = Element("x_stat_abyss_ranks_mp").element
x_stat_abyss_ranks_mk = Element("x_stat_abyss_ranks_mk").element
x_stat_abyss_ranks_ss = Element("x_stat_abyss_ranks_ss").element
x_stat_abyss_ranks_mdt = Element("x_stat_abyss_ranks_mdt").element
x_stat_abyss_ranks_mbu = Element("x_stat_abyss_ranks_mbu").element
x_stat_abyss_ranks_msu = Element("x_stat_abyss_ranks_msu").element
x_stat_abyss_floors = Element("x_stat_abyss_floors").element
x_stat_characters = Element("x_stat_characters").element
x_stat_result = Element("x_stat_result").element
x_stat_error = Element("x_stat_error").element

view_x_artifact = Element("view_x_artifact").element
x_art_newgc = Element("x_art_newgc").element
x_art_name = Element("x_art_name").element
x_art_part = Element("x_art_part").element
x_art_main = Element("x_art_main").element
x_art_level = Element("x_art_level").element
x_art_star = Element("x_art_star").element
x_art_cr = Element("x_art_cr").element
x_art_cd = Element("x_art_cd").element
x_art_er = Element("x_art_er").element
x_art_em = Element("x_art_em").element
x_art_atk = Element("x_art_atk").element
x_art_atkf = Element("x_art_atkf").element
x_art_hp = Element("x_art_hp").element
x_art_hpf = Element("x_art_hpf").element
x_art_def = Element("x_art_def").element
x_art_deff = Element("x_art_deff").element
x_art_clear_sub = Element("x_art_clear_sub").element
x_art_clear_all = Element("x_art_clear_all").element
x_art_generate = Element("x_art_generate").element
x_art_command = Element("x_art_command").element
x_art_error = Element("x_art_error").element
x_art_error_info = Element("x_art_error_info").element

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
    "V": "Ѵ",
    "v": "ѵ",
    "u": "υ",
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
    view_x_stats.classList.add("is-hidden")


def show_main(id):
    view_main.classList.remove("is-hidden")
    view_feature.classList.add("is-hidden")
    breadcrumb1.innerHTML = id.closest(":not(button)").previousElementSibling.innerHTML
    breadcrumb2.innerHTML = id.innerHTML


def x_uncensor_click(event):
    show_main(x_uncensor)
    view_x_uncensor.classList.remove("is-hidden")


def x_stats_click(event):
    show_main(x_stats)
    view_x_stats.classList.remove("is-hidden")


def x_artifact_click(event):
    show_main(x_artifact)
    view_x_artifact.classList.remove("is-hidden")

    x_art_name.innerHTML = f"<option value='0' disabled selected>-</option>"
    x_art_part.innerHTML = f"<option value='0' disabled selected>-</option>"
    x_art_main.innerHTML = f"<option value='0' disabled selected>-</option>"

    for x, y in ARTIFACT_SET.items():
        x_art_name.innerHTML += f"<option value='{x}'>{y}</option>"
    for x, y in ARTIFACT_PART.items():
        x_art_part.innerHTML += f"<option value='{x}'>{y}</option>"

    x_art_name.parentElement.classList.remove("is-loading")
    x_art_part.parentElement.classList.remove("is-loading")
    x_art_main.parentElement.classList.remove("is-loading")


def x_art_part_change(event):
    clear_artifact_substat()
    x_art_main.innerHTML = ""

    match int(x_art_part.value):
        case 40:
            key = [10001]
        case 20:
            key = [10003]
        case 50:
            key = [10002, 10004, 10006, 10007, 10008]
        case 10:
            key = [
                10002,
                10004,
                10006,
                10008,
                15008,
                15009,
                15010,
                15011,
                15012,
                15013,
                15014,
                15015,
            ]
        case 30:
            key = [10002, 10004, 10006, 10008, 13007, 13008, 12009]
        case _:
            return

    if len(key) > 1:
        x_art_main.innerHTML = "<option value='0'>-</option>"
    for x, y in MAIN_STAT.items():
        if x in key:
            x_art_main.innerHTML += f"<option value='{x}'>{y}</option>"


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


def x_stat_invalid():
    x_stat_result.classList.add("is-hidden")
    x_stat_error.classList.remove("is-hidden")
    x_stat_process.classList.remove("is-loading")


async def x_stat_process_click(event):
    x_stat_process.classList.add("is-loading")

    if x_stat_uid.value == "":
        x_stat_invalid()
        return

    try:
        res = await pyfetch(
            url="https://matrix0123.herokuapp.com/full/" + x_stat_uid.value.strip(),
            method="GET",
        )

        raw = await res.json()
        if not raw["data"]:
            x_stat_invalid()
            return

        x_stat_result.classList.remove("is-hidden")
        x_stat_error.classList.add("is-hidden")

        info = raw["data"]["info"]
        stats = raw["data"]["stats"]
        explorations = raw["data"]["explorations"]
        teapot = raw["data"]["teapot"]
        abyss = (
            raw["data"]["abyss"]["current"]
            if raw["data"]["abyss"]["current"]["floors"]
            else raw["data"]["abyss"]["previous"]
        )
        characters = raw["data"]["characters"]

        x_stat_info.innerHTML = f"""
        <h1 class="title has-text-centered">{info["nickname"]}</h1>
        <h2 class="subtitle has-text-centered is-capitalized">
            <p>{raw["uid"]}<br>AR {info["level"]} ~ {info['server'][3:]}</p>
        </h2>
        """

        x_stat_stats.innerHTML = ""
        for x in stats:
            x_stat_stats.innerHTML += f"""
            <tr>
                <td>{x.replace("_", " ")}</td>
                <td>{stats[x]}</td>
            </tr>
            """

        x_stat_exploration_name.innerHTML = ""
        x_stat_exploration_info.innerHTML = ""
        for x in explorations:
            x_stat_exploration_name.innerHTML += f"""
            <td>{x["name"]}</td>
            """
            x_stat_exploration_info.innerHTML += f"""
            <td>
                <table>
                    <tr>
                        <td>Explored</td>
                        <td>{x["explored"]}%</td>
                    </tr>
                    <tr>
                        <td>{x["type"]}</td>
                        <td>{x["level"]}</td>
                    </tr>
                </table>
            </td>
            """

        x_stat_teapot.innerHTML = ""
        for x in teapot:
            if x != "realms" and x != "comfort_icon":
                x_stat_teapot.innerHTML += f"""
                <tr>
                    <td>{x.replace("_", " ")}</td>
                    <td>{teapot[x]}</td>
                </tr>
                """

        x_stat_abyss.innerHTML = ""
        for x in abyss:
            if x != "ranks" and x != "floors":
                x_stat_abyss.innerHTML += f"""
                <tr>
                    <td>{x.replace("_", " ")}</td>
                    <td>{abyss[x]}</td>
                </tr>
                """

        x_stat_abyss_ranks.innerHTML = ""
        for x in abyss["ranks"]:
            x_stat_abyss_ranks.innerHTML += f"""
            <td>{x.replace("_", " ")}</td>
            """

        x_stat_abyss_ranks_mp.innerHTML = ""
        for x in abyss["ranks"]["most_played"]:
            x_stat_abyss_ranks_mp.innerHTML += f"""
            <tr>
                <td>{x["name"]}</td>
                <td>{x["value"]}</td>
            </tr>
            """

        x_stat_abyss_ranks_mk.innerHTML = ""
        for x in abyss["ranks"]["most_kills"]:
            x_stat_abyss_ranks_mk.innerHTML += f"""
            <tr>
                <td>{x["name"]}</td>
                <td>{x["value"]}</td>
            </tr>
            """

        x_stat_abyss_ranks_ss.innerHTML = ""
        for x in abyss["ranks"]["strongest_strike"]:
            x_stat_abyss_ranks_ss.innerHTML += f"""
            <tr>
                <td>{x["name"]}</td>
                <td>{x["value"]}</td>
            </tr>
            """

        x_stat_abyss_ranks_mdt.innerHTML = ""
        for x in abyss["ranks"]["most_damage_taken"]:
            x_stat_abyss_ranks_mdt.innerHTML += f"""
            <tr>
                <td>{x["name"]}</td>
                <td>{x["value"]}</td>
            </tr>
            """

        x_stat_abyss_ranks_mbu.innerHTML = ""
        for x in abyss["ranks"]["most_bursts_used"]:
            x_stat_abyss_ranks_mbu.innerHTML += f"""
            <tr>
                <td>{x["name"]}</td>
                <td>{x["value"]}</td>
            </tr>
            """

        x_stat_abyss_ranks_msu.innerHTML = ""
        for x in abyss["ranks"]["most_skills_used"]:
            x_stat_abyss_ranks_msu.innerHTML += f"""
            <tr>
                <td>{x["name"]}</td>
                <td>{x["value"]}</td>
            </tr>
            """

        x_stat_abyss_floors.innerHTML = ""
        for x in abyss["floors"]:
            x_stat_abyss_floors.innerHTML += f"""
            <td>{x["stars"]} <i class="fa-solid fa-star"></i></td>
            """
        for x in range(4 - len(abyss["floors"])):
            x_stat_abyss_floors.innerHTML += f"""
            <td>0 <i class="fa-solid fa-star"></i></td>
            """

        x_stat_characters.innerHTML = ""
        for x in characters:

            temp_artifact = []
            for artifacts in x["artifacts"]:
                temp_artifact.append(artifacts["set"]["name"])
            count = Counter(temp_artifact)
            artifact_set = ""
            for key, value in count.items():
                artifact_set += f"{key} x{value}<br>"

            if x["outfits"]:
                for outfit in x["outfits"]:
                    outfit_name = outfit["name"]
            else:
                outfit_name = "-"

            x_stat_characters.innerHTML += f"""
            <tr><td class="pt-3" colspan="2"><strong>{x["name"]}</strong></td></tr>
            <tr>
                <td>
                    <table>
                        <tr>
                            <td>Rarity</td>
                            <td>{x["rarity"]}</td>
                        </tr>
                        <tr>
                            <td>Element</td>
                            <td>{x["element"]}</td>
                        </tr>
                        <tr>
                            <td>Level</td>
                            <td>{x["level"]}</td>
                        </tr>
                        <tr>
                            <td>Friendship</td>
                            <td>{x["friendship"]}</td>
                        </tr>
                        <tr>
                            <td>Constellation</td>
                            <td>{x["constellation"]}</td>
                        </tr>
                        <tr>
                            <td>Artifacts</td>
                            <td>{artifact_set}</td>
                        </tr>
                        <tr>
                            <td>Outfits</td>
                            <td>{outfit_name}</td>
                        </tr>
                    </table>
                </td>
                <td>
                    <table>
                        <tr>
                            <td>Weapon</td>
                            <td>{x["weapon"]["name"]}</td>
                        </tr>
                        <tr>
                            <td>Rarity</td>
                            <td>{x["weapon"]["rarity"]}</td>
                        </tr>
                        <tr>
                            <td>Level</td>
                            <td>{x["weapon"]["level"]}</td>
                        </tr>
                        <tr>
                            <td>Refinement</td>
                            <td>{x["weapon"]["refinement"]}</td>
                        </tr>
                    </table>
                </td>
            </tr>
            """

    except Exception as e:
        console.log(e)
        x_stat_process.classList.remove("is-loading")

    x_stat_process.classList.remove("is-loading")


def find_nearest(array, value, command):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return [array[idx], command[idx]]


def generate_artifact(value, stat, command):
    output = []

    if value:
        raw = float(value)
        div = raw / max(stat)

        x = str(div).split(".")[1][:2]
        if int(x) < 8:
            med = raw / round(div)
        else:
            med = raw / int(math.ceil(div))

        while div > 1:
            f = find_nearest(stat, med, command)
            output.append(f[1])
            raw = raw - f[0]
            div = div - 1
        while raw >= (min(stat) - 1):
            f = find_nearest(stat, raw, command)
            output.append(f[1])
            raw = raw - f[0]

    output.sort(reverse=True)
    return output


def x_art_generate_click(event):
    x_art_error.classList.add("is-hidden")

    if (
        int(x_art_name.value) == 0
        or int(x_art_part.value) == 0
        or int(x_art_main.value) == 0
    ):
        x_art_error.classList.remove("is-hidden")
        x_art_command.value = ""
        return

    raw_cmd = []
    raw_cmd.append(generate_artifact(x_art_cr.value, CR, CR_CMD))
    raw_cmd.append(generate_artifact(x_art_cd.value, CD, CD_CMD))
    raw_cmd.append(generate_artifact(x_art_er.value, ER, ER_CMD))
    raw_cmd.append(generate_artifact(x_art_em.value, EM, EM_CMD))
    raw_cmd.append(generate_artifact(x_art_atk.value, ATK, ATK_CMD))
    raw_cmd.append(generate_artifact(x_art_atkf.value, FLAT_ATK, FLAT_ATK_CMD))
    raw_cmd.append(generate_artifact(x_art_hp.value, HP, HP_CMD))
    raw_cmd.append(generate_artifact(x_art_hpf.value, FLAT_HP, FLAT_HP_CMD))
    raw_cmd.append(generate_artifact(x_art_def.value, DEF, DEF_CMD))
    raw_cmd.append(generate_artifact(x_art_deff.value, FLAT_DEF, FLAT_DEF_CMD))

    raw_cmd = [x for x in raw_cmd if x]

    if len(raw_cmd) > 4:
        x_art_error.classList.remove("is-hidden")
        x_art_command.value = ""
        return

    flat_list = []
    for sublist in raw_cmd:
        for item in sublist:
            flat_list.append(item)

    cmd = "/gart "
    cmd += (
        str(
            int(x_art_name.value)
            + int(x_art_part.value)
            + (int(x_art_star.value) * 100)
        )
        + " "
        + str(x_art_main.value)
    )

    count = dict(Counter(flat_list))
    for key, value in count.items():
        if value > 1:
            cmd += " " + str(key) + "," + str(value)
        else:
            cmd += " " + str(key)

    if x_art_newgc.checked:
        cmd = cmd[:11] + " lv" + str(int(x_art_level.value)) + cmd[11:]
    else:
        cmd += " " + str(int(x_art_level.value) + 1)

    x_art_command.value = cmd
    x_art_command.select()
    document.execCommand("copy")


def x_art_clear_sub_click(event):
    clear_artifact_substat()


def x_art_clear_all_click(event):
    x_art_main.innerHTML = "<option value='0'>-</option>"
    x_art_name.selectedIndex = 0
    x_art_part.selectedIndex = 0
    x_art_main.selectedIndex = 0
    x_art_star.value = 5
    x_art_level.value = 20
    clear_artifact_substat()


def clear_artifact_substat():
    x_art_cr.value = ""
    x_art_cd.value = ""
    x_art_er.value = ""
    x_art_em.value = ""
    x_art_atk.value = ""
    x_art_atkf.value = ""
    x_art_hp.value = ""
    x_art_hpf.value = ""
    x_art_def.value = ""
    x_art_deff.value = ""
    x_art_error.classList.add("is-hidden")
    x_art_command.value = ""


def main():
    goto_feature.addEventListener("click", create_proxy(goto_feature_click))

    x_uncensor.addEventListener("click", create_proxy(x_uncensor_click))
    x_uncensor_process.addEventListener("click", create_proxy(x_uncensor_process_click))

    x_stats.addEventListener("click", create_proxy(x_stats_click))
    x_stat_process.addEventListener("click", create_proxy(x_stat_process_click))

    x_artifact.addEventListener("click", create_proxy(x_artifact_click))
    x_art_generate.addEventListener("click", create_proxy(x_art_generate_click))
    x_art_clear_sub.addEventListener("click", create_proxy(x_art_clear_sub_click))
    x_art_clear_all.addEventListener("click", create_proxy(x_art_clear_all_click))
    x_art_part.addEventListener("change", create_proxy(x_art_part_change))

    loading_done()


main()
