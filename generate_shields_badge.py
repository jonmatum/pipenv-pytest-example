import xml.etree.ElementTree as ET
import urllib.parse

def get_coverage_percentage(xml_file="coverage.xml"):
    """
    Parse the coverage.xml file to get the coverage percentage.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    coverage = root.get("line-rate")
    return float(coverage) * 100

def create_shields_badge_url(coverage_percentage):
    """
    Generate a Shields.io badge URL based on the coverage percentage.
    """
    color = "red" if coverage_percentage < 50 else "yellow" if coverage_percentage < 80 else "brightgreen"
    label = "coverage"
    message = f"{coverage_percentage:.0f}%"
    url = f"https://img.shields.io/badge/{urllib.parse.quote(label)}-{urllib.parse.quote(message)}-{color}"
    return url

if __name__ == "__main__":
    coverage_percentage = get_coverage_percentage()
    badge_url = create_shields_badge_url(coverage_percentage)
    print(f"![Coverage Badge]({badge_url})")
