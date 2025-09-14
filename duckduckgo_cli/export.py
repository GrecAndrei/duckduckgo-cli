"""
Export module for the enhanced ddgs tool
"""

import json
import csv
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def export_results(results, format_type, output_file):
    """Export results to a file in the specified format."""
    if format_type == "json":
        with open(output_file, "w") as f:
            json.dump(results, f, indent=2)
    elif format_type == "csv":
        if not results:
            return
        with open(output_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(results[0].keys())
            for result in results:
                writer.writerow(result.values())
    elif format_type == "xml":
        root = Element("results")
        for result in results:
            item = SubElement(root, "result")
            for key, value in result.items():
                child = SubElement(item, key)
                child.text = str(value)
        rough_string = tostring(root, "utf-8")
        reparsed = minidom.parseString(rough_string)
        with open(output_file, "w") as f:
            f.write(reparsed.toprettyxml(indent="  "))
    elif format_type == "markdown":
        if not results:
            return
        with open(output_file, "w") as f:
            f.write("| Title | URL | Snippet |\n")
            f.write("|-------|-----|---------|\n")
            for result in results:
                title = result["title"].replace("|", "\\|")
                href = result["href"].replace("|", "\\|")
                body = result["body"].replace("|", "\\|")
                f.write(f"| {title} | {href} | {body} |\n")
