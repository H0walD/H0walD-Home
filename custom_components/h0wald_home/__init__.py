"""H0walD Home: Dashboard-Editor als Seitenleisten-Panel für Home Assistant."""
from __future__ import annotations

from pathlib import Path

from homeassistant.components import frontend, panel_custom
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, PANEL_ICON, PANEL_TITLE, PANEL_URL, STATIC_URL, VERSION

ELEMENT = "h0wald-home-panel"


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Panel und Dateien registrieren."""
    data = hass.data.setdefault(DOMAIN, {})
    if not data.get("static"):
        await hass.http.async_register_static_paths(
            [StaticPathConfig(STATIC_URL, str(Path(__file__).parent / "frontend"), False)]
        )
        data["static"] = True

    await panel_custom.async_register_panel(
        hass,
        frontend_url_path=PANEL_URL,
        webcomponent_name=ELEMENT,
        sidebar_title=PANEL_TITLE,
        sidebar_icon=PANEL_ICON,
        module_url=f"{STATIC_URL}/{ELEMENT}.js?v={VERSION}",
        require_admin=True,
        config={},
    )
    # Lädt die Datei auch in Dashboards, damit die Karte custom:h0wald-home-card verfügbar ist
    frontend.add_extra_js_url(hass, f"{STATIC_URL}/{ELEMENT}.js?v={VERSION}")
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Panel entfernen."""
    frontend.async_remove_panel(hass, PANEL_URL)
    frontend.remove_extra_js_url(hass, f"{STATIC_URL}/{ELEMENT}.js?v={VERSION}")
    return True
