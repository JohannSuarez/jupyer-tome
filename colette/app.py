import holoviews as hv
import panel as pn

pn.extension()

header_color = "#44f1a6"


primary_view = pn.Column (

    pn.pane.PNG(
        "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"
    )

)



my_template = pn.template.FastListTemplate(
    site="Sample Site",
    title="Memories",
    favicon="assets/ammo_box.png",
    header_background=header_color,
    main=[
        primary_view
    ]
)





my_template.servable()
