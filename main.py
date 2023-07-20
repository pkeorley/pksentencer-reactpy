from reactpy import component, html, use_state
from reactpy.backend.flask import configure, Options

from client import FlaskApplication


app = FlaskApplication()


@component
def Main():

    textarea_text, set_textarea_text = use_state("()")
    textarea_cleared_text, set_textarea_cleared_text = use_state("")

    def on_change_textarea(event: dict):
        sentence = event["target"]["value"]
        set_textarea_cleared_text(app.parser.clear_text(sentence))
        set_textarea_text(app.parser.parse_sentence(sentence))

    return html.div(
        {"class_name": "Main-div"},
        html.div(
            {"class_name": "Main-div-div"},
            html.a(
                {
                    "target": "_blank",
                    "href": "https://pkeorley.xyz"
                },
                html.img({
                    "id": "avatar",
                    "src": "https://cdn.discordapp.com/avatars/762805351242268702/e0da3c183f47ee0393fdb4cd677602ee"
                           ".png?size=256",
                    "alt": "pkeorley",
                })
            ),
            html.textarea(
                {
                    "class_name": "Main-div-textarea",
                    "on_change": on_change_textarea,
                    "id": "textarea",
                    "value": textarea_cleared_text
                },
                textarea_text
            ),
            html.p(
                {"class_name": "Main-div-div-p"},
                textarea_text
            )
        )
    )


configure(app, Main, options=Options(
    head=(
        html.title("Sentence  -  convert phrase to python code..."),
        html.link({"rel": "stylesheet", "href": "static/index.css"})
    ),
    url_prefix="/"
))


app.run(
    debug=True,
    port=8080
)
