from pyodide import create_proxy
from js import document

page_loading = Element("page_loading").element

view_feature = Element("view_feature").element
view_main = Element("view_main").element

x_uncensor = Element("x_uncensor").element
x_artifact = Element("x_artifact").element

view_x_uncensor = Element("view_x_uncensor").element
x_uncensor_ext = Element("x_uncensor_ext").element

goto_feature = Element("goto_feature").element
breadcrumb1 = Element("breadcrumb1").element
breadcrumb2 = Element("breadcrumb2").element
x_input = Element("x_input").element
# x_output = Element("x_output").element
proc_copy = Element("proc_copy").element

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
    # "r": "г",
    "b": "Ь",
    "V": "Ѵ",
    "v": "ѵ",
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
    # x_output.value = ""
    view_x_uncensor.classList.add("is-hidden")


def show_main(id):
    view_main.classList.remove("is-hidden")
    view_feature.classList.add("is-hidden")
    breadcrumb1.innerHTML = id.closest(":not(button)").previousElementSibling.innerHTML
    breadcrumb2.innerHTML = id.innerHTML


def x_uncensor_click(event):
    show_main(x_uncensor)
    view_x_uncensor.classList.remove("is-hidden")


def proc_copy_click(event):
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
    loading_done()
    goto_feature.addEventListener("click", create_proxy(goto_feature_click))
    x_uncensor.addEventListener("click", create_proxy(x_uncensor_click))
    proc_copy.addEventListener("click", create_proxy(proc_copy_click))


main()
