
from qtpylib.blotter import Blotter


class MainBlotter(Blotter):
    pass  # we just need the name


# ===========================================
if __name__ == "__main__":
    blotter = MainBlotter(
        dbhost    = "localhost", # MySQL server
        dbname    = "qtpy",      # MySQL database
        dbuser    = "root",    # MySQL username
        dbpass    = "password",   # MySQL password
        ibport    = 4000,        # IB port (7496/7497 = TWS, 4001 = IBGateway)
        orderbook = True         # fetch and stream order book data
    )
    blotter.run()
