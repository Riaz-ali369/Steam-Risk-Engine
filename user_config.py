import logging
import os
import sys
import yaml

log = logging.getLogger("UserConfig")


def create_default_config() -> None:
    default_config = {"api_key": "SETME", # The user has to set their own steam API key.
                      "steam_user_ids_to_investigate": ["YOUR_STEAMID64_HERE"], # 17-digit SteamID64
                      "dark_mode": True,}
    with open("Config.yaml", "w") as f:
        yaml.safe_dump(default_config, f, sort_keys=False, default_flow_style=False)

if os.path.exists("Config.yaml"):
    with open("Config.yaml", "r") as f:
        config = yaml.safe_load(f)
    try:
        globals().update(config)
    except:
        log.error("Config.yaml has invalid data. A new one will be generated for you. Please reconfigure and try again.")
        os.remove("Config.yaml")
        create_default_config()
        sys.exit(1)

else:
    log.error("Config.yaml is missing. A new one will be generated for you. Please reconfigure and try again.")
    create_default_config()
    sys.exit(1)