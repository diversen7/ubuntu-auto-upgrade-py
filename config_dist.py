CONFIG = {
    # SMTP
    "host": "smtp-relay.sendinblue.com",
    "port": 465,
    "username": "some.user@test.com",
    "password": "password",
    
    # App
    "default_to": "mail@test.com",
    "default_from": "System <mail@test.com>",
    "timezone": "Europe/Copenhagen",
    "restart": True,
    "send_mail": True,

    # Paths. These are the default paths for Ubuntu 20.04 and 22.04
    "apt_check_path": "/usr/lib/update-notifier/apt-check",
    "reboot_required_path": "/var/run/reboot-required",
}


def after_reboot():
    """
    The function to run after a reboot. This is useful for e.g. initializing
    a service that should run after a reboot.
    """
    pass
