from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile


OUTPUT_PATH = Path("StayAtlas_College_Presentation.pptx")

SLIDES = [
    {
        "title": "StayAtlas Hotel Listing Website",
        "subtitle": "College Project Presentation",
        "bullets": [
            "A modular hotel discovery and booking web application built for smooth browsing and faster reservations.",
            "Developed with Flask, SQLAlchemy, MySQL, HTML, CSS, and JavaScript.",
            "Focus area: searchable listings, secure login, bookings, guest reviews, and a polished travel interface.",
        ],
        "tag": "Slide 1 of 13",
    },
    {
        "title": "Problem Statement",
        "subtitle": "Why this project was built",
        "bullets": [
            "Travel websites often overload users with cluttered hotel cards and weak comparison tools.",
            "Users need one place to search by city, price, rating, and amenities before booking.",
            "Hotel detail, booking, and review steps should feel connected instead of fragmented.",
        ],
        "tag": "Slide 2 of 13",
    },
    {
        "title": "Project Overview",
        "subtitle": "What StayAtlas delivers",
        "bullets": [
            "A complete stay discovery flow from hotel search to reservation dashboard.",
            "Seeded with 24 hotels across 18 Indian destinations and 13 guest-focused amenities.",
            "Supports hotel exploration, detail pages, live suggestions, bookings, and review updates.",
        ],
        "tag": "Slide 3 of 13",
    },
    {
        "title": "Objectives",
        "subtitle": "Core goals of the system",
        "bullets": [
            "Build a practical full-stack project using modular Flask architecture.",
            "Improve hotel filtering, decision making, and booking convenience for users.",
            "Store hotel, user, booking, and review data in a structured relational database.",
        ],
        "tag": "Slide 4 of 13",
    },
    {
        "title": "Technology Stack",
        "subtitle": "Tools used in development",
        "bullets": [
            "Backend: Python, Flask, Flask-SQLAlchemy, blueprint-based structure.",
            "Database: MySQL with PyMySQL and environment-based configuration.",
            "Frontend: HTML templates, custom CSS, JavaScript for suggestions, totals, and reveal effects.",
        ],
        "tag": "Slide 5 of 13",
    },
    {
        "title": "System Architecture",
        "subtitle": "How the application is organized",
        "bullets": [
            "app/auth handles signup, login, and logout routes.",
            "app/main manages hotel listing, hotel detail, booking, reviews, and booking dashboard.",
            "app/models defines relational entities such as User, Hotel, Booking, Review, Amenity, and HotelImage.",
        ],
        "tag": "Slide 6 of 13",
    },
    {
        "title": "Hotel Discovery Module",
        "subtitle": "Browsing and shortlist features",
        "bullets": [
            "Search supports hotel name or city with query-based filtering.",
            "Filters include city, minimum and maximum price, rating, and selected amenities.",
            "Hotels are presented with images, location, price per night, and average rating.",
        ],
        "tag": "Slide 7 of 13",
    },
    {
        "title": "Hotel Detail and Booking",
        "subtitle": "From viewing to reservation",
        "bullets": [
            "Each hotel page includes gallery images, description, amenities, reviews, and map view.",
            "Booking form accepts check-in and check-out dates with client-side price calculation.",
            "Server-side validation blocks invalid dates and stores confirmed bookings with total price.",
        ],
        "tag": "Slide 8 of 13",
    },
    {
        "title": "Authentication and Reviews",
        "subtitle": "User-specific interactions",
        "bullets": [
            "Session-based login keeps protected actions available only to authenticated users.",
            "Users can create one review per hotel and update it later instead of duplicating entries.",
            "A personal dashboard shows all reservations with travel dates, hotel details, and booking status.",
        ],
        "tag": "Slide 9 of 13",
    },
    {
        "title": "Database Design",
        "subtitle": "Main entities in the schema",
        "bullets": [
            "User stores account information and password hash.",
            "Hotel connects to amenities, gallery images, bookings, and reviews through SQLAlchemy relationships.",
            "Booking tracks stay dates and total price, while Review stores rating, comment, and timestamps.",
        ],
        "tag": "Slide 10 of 13",
    },
    {
        "title": "Frontend Experience",
        "subtitle": "Usability improvements in the UI",
        "bullets": [
            "Hero section and richer hotel cards make browsing more visual and easier to scan.",
            "Live search suggestions are fetched through an API endpoint for faster discovery.",
            "Scroll-based reveal animations and dynamic booking totals make the interface feel modern.",
        ],
        "tag": "Slide 11 of 13",
    },
    {
        "title": "Benefits and Future Scope",
        "subtitle": "Why this project matters",
        "bullets": [
            "Demonstrates practical integration of frontend, backend, and database concepts in one project.",
            "Can be extended with payment gateway support, admin panel, cancellation flow, and wishlists.",
            "Further improvements could include room availability, recommendation engine, and deployment to cloud hosting.",
        ],
        "tag": "Slide 12 of 13",
    },
    {
        "title": "Conclusion",
        "subtitle": "Project outcome",
        "bullets": [
            "StayAtlas delivers a complete hotel listing and booking workflow with a clean user experience.",
            "The project shows strong understanding of full-stack web development and relational data design.",
            "It is suitable for demonstrating software architecture, CRUD operations, validation, and UI thinking in a college presentation.",
        ],
        "tag": "Slide 13 of 13",
    },
]


def emu(value: float) -> int:
    return int(value)


def content_types_xml(slide_count: int) -> str:
    slide_overrides = "\n".join(
        f'  <Override PartName="/ppt/slides/slide{i}.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1, slide_count + 1)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
{slide_overrides}
</Types>
"""


ROOT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""


def app_xml(slide_count: int) -> str:
    titles = "".join(f"<vt:lpstr>Slide {i}</vt:lpstr>" for i in range(1, slide_count + 1))
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
 xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office PowerPoint</Application>
  <PresentationFormat>Widescreen</PresentationFormat>
  <Slides>{slide_count}</Slides>
  <Notes>0</Notes>
  <HiddenSlides>0</HiddenSlides>
  <MMClips>0</MMClips>
  <ScaleCrop>false</ScaleCrop>
  <HeadingPairs>
    <vt:vector size="2" baseType="variant">
      <vt:variant><vt:lpstr>Slides</vt:lpstr></vt:variant>
      <vt:variant><vt:i4>{slide_count}</vt:i4></vt:variant>
    </vt:vector>
  </HeadingPairs>
  <TitlesOfParts>
    <vt:vector size="{slide_count}" baseType="lpstr">{titles}</vt:vector>
  </TitlesOfParts>
  <Company></Company>
  <LinksUpToDate>false</LinksUpToDate>
  <SharedDoc>false</SharedDoc>
  <HyperlinksChanged>false</HyperlinksChanged>
  <AppVersion>16.0000</AppVersion>
</Properties>
"""


def core_xml() -> str:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
 xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:dcterms="http://purl.org/dc/terms/"
 xmlns:dcmitype="http://purl.org/dc/dcmitype/"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>StayAtlas College Presentation</dc:title>
  <dc:subject>Hotel Listing Website Project Presentation</dc:subject>
  <dc:creator>OpenAI Codex</dc:creator>
  <cp:keywords>StayAtlas, Flask, Hotel Listing, College Presentation</cp:keywords>
  <dc:description>13-slide presentation for the StayAtlas hotel listing project.</dc:description>
  <cp:lastModifiedBy>OpenAI Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>
</cp:coreProperties>
"""


def presentation_xml(slide_count: int) -> str:
    slide_ids = "\n".join(
        f'    <p:sldId id="{255 + i}" r:id="rId{i + 1}"/>' for i in range(1, slide_count + 1)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
 xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldMasterIdLst>
    <p:sldMasterId id="2147483648" r:id="rId1"/>
  </p:sldMasterIdLst>
  <p:sldIdLst>
{slide_ids}
  </p:sldIdLst>
  <p:sldSz cx="12192000" cy="6858000"/>
  <p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>
"""


def presentation_rels_xml(slide_count: int) -> str:
    slide_rels = "\n".join(
        f'  <Relationship Id="rId{i + 1}" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" '
        f'Target="slides/slide{i}.xml"/>'
        for i in range(1, slide_count + 1)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>
{slide_rels}
</Relationships>
"""


SLIDE_MASTER_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
 xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld name="Simple Master">
    <p:bg>
      <p:bgPr>
        <a:solidFill><a:srgbClr val="F7F3EC"/></a:solidFill>
      </p:bgPr>
    </p:bg>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/>
          <a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMap accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" bg1="lt1" bg2="lt2" folHlink="folHlink" hlink="hlink" tx1="dk1" tx2="dk2"/>
  <p:sldLayoutIdLst>
    <p:sldLayoutId id="1" r:id="rId1"/>
  </p:sldLayoutIdLst>
</p:sldMaster>
"""


SLIDE_MASTER_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
</Relationships>
"""


SLIDE_LAYOUT_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
 xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1">
  <p:cSld name="Blank">
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/>
          <a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>
"""


SLIDE_LAYOUT_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>
"""


THEME_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="StayAtlas Theme">
  <a:themeElements>
    <a:clrScheme name="StayAtlas">
      <a:dk1><a:srgbClr val="1E2A39"/></a:dk1>
      <a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>
      <a:dk2><a:srgbClr val="36404D"/></a:dk2>
      <a:lt2><a:srgbClr val="F7F3EC"/></a:lt2>
      <a:accent1><a:srgbClr val="0E7490"/></a:accent1>
      <a:accent2><a:srgbClr val="C56E3D"/></a:accent2>
      <a:accent3><a:srgbClr val="B69A56"/></a:accent3>
      <a:accent4><a:srgbClr val="567189"/></a:accent4>
      <a:accent5><a:srgbClr val="5A7D5A"/></a:accent5>
      <a:accent6><a:srgbClr val="9F4C4C"/></a:accent6>
      <a:hlink><a:srgbClr val="0E7490"/></a:hlink>
      <a:folHlink><a:srgbClr val="7C3AED"/></a:folHlink>
    </a:clrScheme>
    <a:fontScheme name="StayAtlas Fonts">
      <a:majorFont>
        <a:latin typeface="Aptos Display"/>
        <a:ea typeface=""/>
        <a:cs typeface=""/>
      </a:majorFont>
      <a:minorFont>
        <a:latin typeface="Aptos"/>
        <a:ea typeface=""/>
        <a:cs typeface=""/>
      </a:minorFont>
    </a:fontScheme>
    <a:fmtScheme name="StayAtlas Format">
      <a:fillStyleLst>
        <a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
        <a:gradFill rotWithShape="1">
          <a:gsLst>
            <a:gs pos="0"><a:schemeClr val="accent1"/></a:gs>
            <a:gs pos="100000"><a:schemeClr val="accent2"/></a:gs>
          </a:gsLst>
          <a:lin ang="5400000" scaled="0"/>
        </a:gradFill>
      </a:fillStyleLst>
      <a:lnStyleLst>
        <a:ln w="12700"><a:solidFill><a:schemeClr val="accent1"/></a:solidFill></a:ln>
      </a:lnStyleLst>
      <a:effectStyleLst>
        <a:effectStyle><a:effectLst/></a:effectStyle>
      </a:effectStyleLst>
      <a:bgFillStyleLst>
        <a:solidFill><a:schemeClr val="lt2"/></a:solidFill>
      </a:bgFillStyleLst>
    </a:fmtScheme>
  </a:themeElements>
  <a:objectDefaults/>
  <a:extraClrSchemeLst/>
</a:theme>
"""


def paragraph_xml(text: str, size: int, color: str, bullet: bool = False, bold: bool = False) -> str:
    bullet_xml = '<a:buChar char="•"/>' if bullet else "<a:buNone/>"
    bold_val = "1" if bold else "0"
    return (
        f"<a:p><a:pPr>{bullet_xml}</a:pPr>"
        f'<a:r><a:rPr lang="en-US" sz="{size}" b="{bold_val}"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill></a:rPr>'
        f"<a:t>{escape(text)}</a:t></a:r><a:endParaRPr lang=\"en-US\" sz=\"{size}\"/></a:p>"
    )


def text_shape(shape_id: int, name: str, x: int, y: int, cx: int, cy: int, paragraphs: str) -> str:
    return f"""    <p:sp>
      <p:nvSpPr>
        <p:cNvPr id="{shape_id}" name="{escape(name)}"/>
        <p:cNvSpPr txBox="1"/>
        <p:nvPr/>
      </p:nvSpPr>
      <p:spPr>
        <a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>
        <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
        <a:noFill/>
        <a:ln><a:noFill/></a:ln>
      </p:spPr>
      <p:txBody>
        <a:bodyPr wrap="square"/>
        <a:lstStyle/>
{paragraphs}
      </p:txBody>
    </p:sp>
"""


def rect_shape(shape_id: int, name: str, x: int, y: int, cx: int, cy: int, fill: str) -> str:
    return f"""    <p:sp>
      <p:nvSpPr>
        <p:cNvPr id="{shape_id}" name="{escape(name)}"/>
        <p:cNvSpPr/>
        <p:nvPr/>
      </p:nvSpPr>
      <p:spPr>
        <a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>
        <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
        <a:solidFill><a:srgbClr val="{fill}"/></a:solidFill>
        <a:ln><a:noFill/></a:ln>
      </p:spPr>
    </p:sp>
"""


def slide_xml(slide: dict[str, object]) -> str:
    title_paragraphs = paragraph_xml(str(slide["title"]), 2600, "1E2A39", bullet=False, bold=True)
    subtitle_paragraphs = paragraph_xml(str(slide["subtitle"]), 1280, "0E7490", bullet=False, bold=True)
    bullet_paragraphs = "\n".join(
        paragraph_xml(text, 1800, "2F3A44", bullet=True, bold=False)
        for text in slide["bullets"]
    )
    footer_paragraphs = paragraph_xml(str(slide["tag"]), 1100, "F7F3EC", bullet=False, bold=True)

    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
 xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg>
      <p:bgPr>
        <a:solidFill><a:srgbClr val="F7F3EC"/></a:solidFill>
      </p:bgPr>
    </p:bg>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/>
          <a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
{rect_shape(2, "Top Bar", 0, 0, 12192000, 720000, "1E2A39")}
{rect_shape(3, "Accent Block", 0, 720000, 1450000, 6140000, "0E7490")}
{rect_shape(4, "Footer", 0, 6180000, 12192000, 678000, "1E2A39")}
{text_shape(5, "Title", 1850000, 1020000, 9300000, 900000, title_paragraphs)}
{text_shape(6, "Subtitle", 1850000, 1880000, 9000000, 400000, subtitle_paragraphs)}
{text_shape(7, "Body", 1850000, 2480000, 9300000, 3000000, bullet_paragraphs)}
{text_shape(8, "Footer Text", 9600000, 6320000, 1800000, 250000, footer_paragraphs)}
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>
"""


SLIDE_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>
"""


def build_pptx(output_path: Path) -> None:
    with ZipFile(output_path, "w", compression=ZIP_DEFLATED) as package:
        package.writestr("[Content_Types].xml", content_types_xml(len(SLIDES)))
        package.writestr("_rels/.rels", ROOT_RELS)
        package.writestr("docProps/app.xml", app_xml(len(SLIDES)))
        package.writestr("docProps/core.xml", core_xml())
        package.writestr("ppt/presentation.xml", presentation_xml(len(SLIDES)))
        package.writestr("ppt/_rels/presentation.xml.rels", presentation_rels_xml(len(SLIDES)))
        package.writestr("ppt/slideMasters/slideMaster1.xml", SLIDE_MASTER_XML)
        package.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", SLIDE_MASTER_RELS_XML)
        package.writestr("ppt/slideLayouts/slideLayout1.xml", SLIDE_LAYOUT_XML)
        package.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", SLIDE_LAYOUT_RELS_XML)
        package.writestr("ppt/theme/theme1.xml", THEME_XML)

        for index, slide in enumerate(SLIDES, start=1):
            package.writestr(f"ppt/slides/slide{index}.xml", slide_xml(slide))
            package.writestr(f"ppt/slides/_rels/slide{index}.xml.rels", SLIDE_RELS_XML)


if __name__ == "__main__":
    build_pptx(OUTPUT_PATH)
    print(f"Created {OUTPUT_PATH.resolve()}")
