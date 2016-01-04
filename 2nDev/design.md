# MVP0.1

用Python 解析html 中的javascript

推荐工具：[Ghost.py](http://jeanphix.me/Ghost.py/)

+ installation
`pip install Ghost.py
`

+Quick Start

DEMO:The following test tries to center http://www.openstreetmap.org/ map to France:

    # Opens the web page
    ghost.open('http://www.openstreetmap.org/')
    # Waits for form search field
    ghost.wait_for_selector('input[name=query]')
    # Fills the form
    ghost.fill("#search_form", {'query': 'France'})
    # Submits the form
    ghost.call("#search_form", "submit")
    # Waits for results (an XHR has been called here)
    ghost.wait_for_selector(
        '#search_osm_nominatim .search_results_entry a')
    # Clicks first result link
    ghost.click(
        '#search_osm_nominatim .search_results_entry:first-child a')
    # Checks if map has moved to expected latitude
    lat, resources = ghost.evaluate("map.center.lat")
    assert float(lat.toString()) == 5860090.806537
