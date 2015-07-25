from urllib2 import urlopen, HTTPError, URLError

from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QMessageBox
from osma_web_services_dialog import TokenDialog

__author__ = 'matthew.walsh'


class Token:
    # Main variable for a VALID token
    token = None

    def __init__(self, iface):

        # Local ref to plugin iface
        self.iface = iface

        # Create instance of token dlg
        self.token_dlg = TokenDialog()
        self.token_dlg.ui.goTokenButton.clicked.connect(self.check_token_from_dlg)

        # Windows registry access
        self.registry = QSettings()

    def check_token(self, token=None):
        # Check Windows registry for a valid token
        try:
            if not token:
                token = self.registry.value("OsmaWebServices/Token")
            get_cap_url = "http://wms.locationcentre.co.uk/services/" + token + "/service?&request=GetCapabilities"
            request = urlopen(get_cap_url)
            response = request.getcode()
            if response == 200:
                self.token = str(token)
                return True
            else:
                return False
        except TypeError:
            # Raise TypeError for no token present and http for 404
            print "No token in reg"
            return False
        except HTTPError, err:
            if err.code == 403:
                print "Invalid token in reg"
            else:
                print "HTTP error code: " + str(err.code)
            return False
        except URLError, err:
            print err

    def prompt_token(self):
        self.token_dlg.exec_()

    def check_token_from_dlg(self):
        token_dlg_text = str(self.token_dlg.ui.tokenLineEdit.text())
        valid = self.check_token(token_dlg_text)
        if valid:
            self.token = token_dlg_text
            self.store_token()
            self.token_dlg.close()
        else:
            QMessageBox.warning(self.iface.mainWindow(), "Invalid Token", "The token provided is not valid")

    def store_token(self):
        # Store token in registry
        name = "OsmaWebServices/Token"
        self.registry.setValue(name, self.token)

    def clear_token(self):
        self.token = None
        name = "OsmaWebServices/Token"
        self.registry.remove(name)
