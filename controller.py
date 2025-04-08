def setup_connections(ui):
    for i, btn in enumerate(ui.buttons):
        btn.clicked.connect(lambda _, x=i: print(f"Button {x + 1} clicked!"))
