import json
import csv
import glob
import xml.etree.ElementTree as etree

from translate.storage import pypo


def main():
    root = etree.Element("TranslationData")

    for file_path in glob.glob("translation/ko/*.po"):
        with open(file_path, "rb") as fp:
            po = pypo.pofile(fp)
        
        unit: pypo.pounit
        for unit in po.units:
            if unit.isheader():
                continue

            key = unit.getcontext()
            target = unit.target

            if target:
                etree.SubElement(root, "Term", key=key, value=target)
    
    doc = etree.ElementTree(root)
    etree.indent(doc)
    doc.write("translation.xml", encoding="utf-8")


if __name__ == "__main__":
    main()
