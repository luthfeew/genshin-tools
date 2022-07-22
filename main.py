from pyodide import create_proxy

page_loading = Element("page_loading").element

view_feature = Element("view_feature").element
view_main = Element("view_main").element

x_uncensor = Element("x_uncensor").element
x_artifact = Element("x_artifact").element

goto_feature = Element("goto_feature").element
breadcrumb1 = Element("breadcrumb1").element
breadcrumb2 = Element("breadcrumb2").element
x_input = Element("x_input").element
x_output = Element("x_output").element


def loading_done():
    page_loading.classList.add("is-hidden")
    show_feature()


def goto_feature_click(event):
    show_feature()


def show_feature():
    view_feature.classList.remove("is-hidden")
    view_main.classList.add("is-hidden")
    x_input.value = ""
    x_output.value = ""


def show_main(id):
    view_main.classList.remove("is-hidden")
    view_feature.classList.add("is-hidden")
    breadcrumb1.innerHTML = id.closest(":not(button)").previousElementSibling.innerHTML
    breadcrumb2.innerHTML = id.innerHTML


def x_uncensor_click(event):
    show_main(x_uncensor)
    # view_x_uncensor.classList.remove("is-hidden")


def main():
    loading_done()
    goto_feature.addEventListener("click", create_proxy(goto_feature_click))
    x_uncensor.addEventListener("click", create_proxy(x_uncensor_click))


main()
