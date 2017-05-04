from urllib2 import HTTPError, URLError
from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QMessageBox

from osma_web_services_dialog import MapcloudAuthDialog
from layers import BASE_API_URL, make_mapcloud_request

__author__ = 'matthew.walsh'


class MapCloudAuthentication:

    username = None
    password = None

    def __init__(self, iface):

        # Local ref to plugin iface
        self.iface = iface

        # Create instance of mc_auth dlg
        self.mc_auth_dlg = MapcloudAuthDialog()
        self.mc_auth_dlg.ui.loginPushButton.clicked.connect(self.check_auth_credentials)
        self.mc_auth_dlg.ui.cancelPushButton.clicked.connect(self.cancel_login)

        # Windows registry access
        self.registry = QSettings()

    def cancel_login(self):
        self.mc_auth_dlg.close()

    def validate_auth_credentials(self, username=None, password=None):
        """
        Test the auth credentials by hitting the GetCapabilities.
        First tries the provided details then uses the registry.
        :param username: MC username
        :param password: MC password
        """
        try:
            if not username or not password:
                username = self.registry.value("TheMapCloudWebServices/username")
                password = self.registry.value("TheMapCloudWebServices/password")

            get_cap_url = '{}/maps/wms?REQUEST=GetCapabilities'.format(BASE_API_URL)
            _, status_code = make_mapcloud_request(get_cap_url, username, password)

            if status_code == 200:
                self.username = str(username)
                self.password = str(password)
                return True
            else:
                return False

        except TypeError:
            # Raise TypeError for no mc_auth present and http for 404
            print "No auth credentials found in registry"
            return False

        except HTTPError, err:
            if err.code == 401:
                print "Authentication failed - invalid auth credentials"
            else:
                print "HTTP error code: " + str(err.code)
            return False

        except URLError, err:
            print err

    def prompt_login(self):
        """
        Show the login dialog.
        """
        self.mc_auth_dlg.exec_()

    def check_auth_credentials(self):
        """
        Save the auth credentials from the dialog if they
        are valid.
        """
        username_text = str(self.mc_auth_dlg.ui.usernameLineEdit.text())
        password_text = str(self.mc_auth_dlg.ui.passwordLineEdit.text())
        valid = self.validate_auth_credentials(username_text, password_text)
        if valid:
            self.username = username_text
            self.password = password_text
            self.store_auth_credentials()
            self.mc_auth_dlg.close()
        else:
            QMessageBox.warning(self.iface.mainWindow(),
                                "Invalid MapCloud Authentication",
                                "The credentials provided are not valid")

    def store_auth_credentials(self):
        """
        Store the auth credentials in the registry.
        """
        username_entry = "TheMapCloudWebServices/username"
        password_entry = "TheMapCloudWebServices/password"
        self.registry.setValue(username_entry, self.username)
        self.registry.setValue(password_entry, self.password)

    def clear_auth_credentials(self):
        """
        Remove any registry entries and clear class
        variables.
        """
        self.username = None
        self.password = None

        username_entry = "TheMapCloudWebServices/username"
        password_entry = "TheMapCloudWebServices/username"
        self.registry.remove(username_entry)
        self.registry.remove(password_entry)
