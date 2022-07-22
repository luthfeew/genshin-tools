page_loading = Element("page_loading").element

view_feature = Element("view_feature").element
view_main = Element("view_main").element

x_uncensor = Element("x_uncensor").element
x_artifact = Element("x_artifact").element

x_input = Element("x_input").element
x_output = Element("x_output").element


def loading_done():
    page_loading.classList.add("is-hidden")
    show_feature()


def show_feature():
    view_feature.classList.remove("is-hidden")
    view_main.classList.add("is-hidden")
    x_input.value = ""
    x_output.value = ""


def main():
    loading_done()


main()
