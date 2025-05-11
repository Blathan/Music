import service.serial_check as sc


def setup_connections(ui):
    for i, btn in enumerate(ui.buttons):
        # sc.send_fold_name(x + 1))
        btn.clicked.connect(lambda _, x=i: print(x+1))
