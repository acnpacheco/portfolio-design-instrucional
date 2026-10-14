"""Empacota o curso demonstrativo e verifica estrutura local, sem certificar conformidade."""
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / 'dist' / 'course'
OUT = ROOT / 'dist' / 'assets' / 'scorm'
OUT.mkdir(parents=True, exist_ok=True)

def manifest(version):
    is2004 = version == '2004'
    namespace = 'http://www.imsglobal.org/xsd/imscp_v1p1' if is2004 else 'http://www.imsproject.org/xsd/imscp_rootv1p1p2'
    adl = 'http://www.adlnet.org/xsd/adlcp_v1p3' if is2004 else 'http://www.adlnet.org/xsd/adlcp_rootv1p2'
    scormtype = 'scormType' if is2004 else 'scormtype'
    version_label = '2004 4th Edition' if is2004 else '1.2'
    mastery = '' if is2004 else '<adlcp:masteryscore>75</adlcp:masteryscore>'
    sequence = '<imsss:sequencing><imsss:objectives><imsss:primaryObjective objectiveID="atendimento" satisfiedByMeasure="true"><imsss:minNormalizedMeasure>0.75</imsss:minNormalizedMeasure></imsss:primaryObjective></imsss:objectives></imsss:sequencing>' if is2004 else ''
    files = ''.join(f'<file href="{f}"/>' for f in ['index.html', 'course.css', 'course.js', 'navigation.js', 'scorm.js', 'config.js'])
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="FORMA_ATENDIMENTO_{version}" version="1.0" xmlns="{namespace}" xmlns:adlcp="{adl}" xmlns:imsss="http://www.imsglobal.org/xsd/imsss">
<metadata><schema>ADL SCORM</schema><schemaversion>{version_label}</schemaversion></metadata>
<organizations default="ORG"><organization identifier="ORG"><title>Atendimento com propósito</title><item identifier="ITEM" identifierref="SCO"><title>Quatro decisões de atendimento</title>{mastery}{sequence}</item></organization></organizations>
<resources><resource identifier="SCO" type="webcontent" adlcp:{scormtype}="sco" href="index.html">{files}</resource></resources></manifest>'''

for version, filename in [('1.2', 'atendimento-scorm12.zip'), ('2004', 'atendimento-scorm2004.zip')]:
    xml = manifest(version)
    ET.fromstring(xml)
    target = OUT / filename
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('imsmanifest.xml', xml)
        archive.writestr('config.js', f"window.FORMA_SCORM_VERSION='{version}';\n")
        for file in ['index.html', 'course.css', 'course.js', 'navigation.js', 'scorm.js']:
            archive.write(COURSE / file, file)
    with zipfile.ZipFile(target) as archive:
        names = set(archive.namelist())
        root = ET.fromstring(archive.read('imsmanifest.xml'))
        for node in root.iter():
            if node.tag.endswith('}file') or node.tag.endswith('}resource'):
                assert node.attrib['href'] in names
        assert archive.testzip() is None
    print(f'{filename}: XML legível, referências locais e integridade ZIP conferidas.')

