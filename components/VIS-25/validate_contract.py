#!/usr/bin/env python3
"""VIS-25 read-only contract scan for a supplied Roll20 HTML/CSS snapshot.

Run: python validate_contract.py --html sheet.html --css sheet.css
Does not edit input files, attributes, actions, or worker code.
"""
import argparse
import re
from pathlib import Path
from html.parser import HTMLParser

class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.elements = []

    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        self.elements.append((tag, props, set(props.get("class", "").split())))

    handle_startendtag = handle_starttag

def validate(html_path, css_path):
    html = Path(html_path).read_text(encoding="utf-8")
    css = Path(css_path).read_text(encoding="utf-8")
    parser = Scan()
    parser.feed(html)
    elems = parser.elements
    classes = {c for _, _, cc in elems for c in cc}
    names = {p.get("name") for _, p, _ in elems if p.get("name")}
    errors, warnings = [], []

    for cls in (
        "sheet-vn-wrapper", "sheet-vn-header", "sheet-vn-panel",
        "sheet-vn-tabbar", "sheet-vn-tabbtn", "sheet-vn-tabstate",
        "sheet-vn-pagestate", "sheet-vn-page", "sheet-vn-input",
        "sheet-vn-btn", "sheet-vn-stat", "sheet-vn-skillsummary",
        "sheet-vn-spellsummary", "sheet-vn-typepill", "sheet-vn-actionpill",
        "sheet-vn-familypill", "sheet-vn-summarytone", "sheet-vn-familytone",
        "sheet-vn-focusopen", "sheet-vn-clubrail", "sheet-vn-clublogo",
        "repeating_skills", "repeating_knownspells", "repeating_sponsors"
    ):
        if cls not in classes:
            errors.append(f"Missing structural class: {cls}")

    expected = [4, 1, 3, 2, 5, 6, 7]
    actual = [
        int(p["name"].removeprefix("act_vn_tab_"))
        for tag, p, _ in elems
        if tag == "button" and re.fullmatch(r"act_vn_tab_\d+", p.get("name", ""))
    ]
    if actual != expected:
        errors.append(f"Tab action order changed: {actual} (expected {expected})")
    for i in expected:
        for name in (f"attr_vn_tabbtn_{i}", f"attr_vn_tabpage_{i}"):
            if name not in names:
                errors.append(f"Missing navigation state field: {name}")
    for name in (
        "attr_vn_entity_mode", "attr_vn_focus_open", "attr_vn_crawler_identity",
        "attr_vn_race_display_name", "attr_vn_class_display_name",
        "attr_lvl", "attr_floor_current"
    ):
        if name not in names:
            errors.append(f"Missing source field: {name}")

    for cls, expected_count in (("sheet-vn-stat", 5), ("sheet-vn-clublogo", 6)):
        count = sum(cls in cc for _, _, cc in elems)
        if count != expected_count:
            warnings.append(f"{cls}: expected {expected_count} in R42, found {count}")

    for signature in (
        '.sheet-vn-summarytone[value="ATTACK"]',
        '.sheet-vn-familytone[value="ANIMAL"]',
        '.sheet-vn-tabstate[value="1"]+.sheet-vn-tabbtn'
    ):
        if signature not in css:
            warnings.append(f"CSS gate rule changed: {signature}")

    print("VIS-25 R42 component compatibility scan")
    print(f"Elements: {len(elems)} | Tab order: {actual}")
    for msg in warnings: print("WARN:", msg)
    for msg in errors: print("FAIL:", msg)
    print(f"RESULT: {'FAIL' if errors else 'PASS'} ({len(errors)} errors, {len(warnings)} warnings)")
    return int(bool(errors))

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--html", required=True)
    p.add_argument("--css", required=True)
    a = p.parse_args()
    raise SystemExit(validate(a.html, a.css))
