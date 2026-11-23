# Pure Python PDF Generator without any external dependencies
import sys

class SimplePDF:
    def __init__(self, filename):
        self.filename = filename
        self.objects = []
        self.pages = []
        
    def add_object(self, content):
        self.objects.append(content)
        return len(self.objects)
        
    def create_page(self, stream_content):
        # sanitize unicode characters to ASCII/latin-1
        replacements = {
            '\u2014': '--',
            '\u2013': '-',
            '\u2018': "'",
            '\u2019': "'",
            '\u201c': '"',
            '\u201d': '"',
            '\u2022': '*',
            '\u2192': '->'
        }
        for k, v in replacements.items():
            stream_content = stream_content.replace(k, v)
        stream_bytes = stream_content.encode('latin1')
        stream_len = len(stream_bytes)
        stream_obj = f"<< /Length {stream_len} >>\nstream\n{stream_content}\nendstream"
        stream_id = self.add_object(stream_obj)
        
        page_obj = f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595.28 841.89] /Contents {stream_id} 0 R /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> >>"
        page_id = self.add_object(page_obj)
        self.pages.append(page_id)
        
    def save(self):
        # 1: Catalog, 2: Pages, 3: F1 (Helvetica), 4: F2 (Helvetica-Bold)
        # We will insert Catalog, Pages, F1, F2 at the beginning
        font_helv = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"
        font_bold = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>"
        
        # Shift all existing objects
        shifted_pages = [p + 4 for p in self.pages]
        pages_ref = " ".join([f"{p} 0 R" for p in shifted_pages])
        pages_obj = f"<< /Type /Pages /Kids [ {pages_ref} ] /Count {len(shifted_pages)} >>"
        catalog_obj = "<< /Type /Catalog /Pages 2 0 R >>"
        
        final_objects = [catalog_obj, pages_obj, font_helv, font_bold]
        for obj in self.objects:
            # Update any references inside objects
            # stream_id in page was stream_id (which is 1-based, now shifted)
            if "/Parent 2 0 R" in obj:
                # it's a page obj
                import re
                def repl(m):
                    old_id = int(m.group(1))
                    return f"/Contents {old_id + 4} 0 R"
                obj = re.sub(r'/Contents (\d+) 0 R', repl, obj)
            final_objects.append(obj)
            
        with open(self.filename, 'wb') as f:
            f.write(b"%PDF-1.4\n")
            xref_offsets = []
            offset = len(b"%PDF-1.4\n")
            
            for i, obj in enumerate(final_objects, 1):
                xref_offsets.append(offset)
                obj_data = f"{i} 0 obj\n{obj}\nendobj\n".encode('latin1')
                f.write(obj_data)
                offset += len(obj_data)
                
            xref_pos = offset
            f.write(b"xref\n")
            f.write(f"0 {len(final_objects) + 1}\n".encode('latin1'))
            f.write(b"0000000000 65535 f \n")
            for off in xref_offsets:
                f.write(f"{off:010d} 00000 n \n".encode('latin1'))
                
            trailer = f"trailer\n<< /Size {len(final_objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n"
            f.write(trailer.encode('latin1'))

pdf = SimplePDF(r"C:\Users\chith\.gemini\antigravity\scratch\importnow-replica\ImportNow_Assignment_Explanation_Premsai.pdf")

# Page 1 content
c1 = """
0.89 0.14 0.11 rg 40 800 515 3 re f
0.04 0.04 0.04 rg
BT /F2 22 Tf 40 765 Td (IMPORTNOW) Tj ET
0.89 0.14 0.11 rg
BT /F2 22 Tf 175 765 Td ( -- AI Executive Assignment) Tj ET

0.2 0.2 0.2 rg
BT /F1 10 Tf 40 740 Td (Candidate: Premsai | Email: maheshmannef4@gmail.com | Role: AI Executive | Date: Nov 2026) Tj ET

0.95 0.95 0.95 rg 40 655 515 70 re f
0.8 0.8 0.8 RG 40 655 515 70 re S
0.04 0.04 0.04 rg
BT /F2 12 Tf 52 705 Td (PROJECT DELIVERABLES & VERIFIED LINKS:) Tj ET
BT /F2 10 Tf 52 685 Td (Live Website:) Tj /F1 10 Tf 140 685 Td (https://premsai19.github.io/importnow-replica/) Tj ET
BT /F2 10 Tf 52 668 Td (GitHub Repo:) Tj /F1 10 Tf 140 668 Td (https://github.com/Premsai19/importnow-replica) Tj ET

0.89 0.14 0.11 rg 40 635 4 14 re f
0.04 0.04 0.04 rg
BT /F2 14 Tf 50 637 Td (1. Executive Summary & Challenge Overview) Tj ET

0.2 0.2 0.2 rg
BT /F1 9.5 Tf 40 618 Td (This report outlines the technical workflow and AI architecture used to build a 100% faithful,) Tj ET
BT /F1 9.5 Tf 40 605 Td (production-ready replication of the ImportNow concept platform (importnow-concept.vercel.app).) Tj ET
BT /F1 9.5 Tf 40 592 Td (The objective was to reproduce the visual design, interactive 3D WebGL scenes, knowledge hub,) Tj ET
BT /F1 9.5 Tf 40 579 Td (and responsive behavior from scratch using modern AI tools and web standards.) Tj ET

0.89 0.14 0.11 rg 40 555 4 14 re f
0.04 0.04 0.04 rg
BT /F2 14 Tf 50 557 Td (2. AI Tools & Engineering Workflow) Tj ET

BT /F2 10.5 Tf 40 537 Td (A. Autonomous Perception & Reverse-Engineering (AI Browser Agent):) Tj ET
BT /F1 9.5 Tf 50 523 Td (- Deployed an autonomous Playwright browser subagent to inspect the reference platform.) Tj ET
BT /F1 9.5 Tf 50 510 Td (- Mapped typography (Sora for headings, Inter for body copy) and color palettes (#e3241b crimson).) Tj ET
BT /F1 9.5 Tf 50 497 Td (- Extracted the full structure of all 11 sections, blog system, and single-post article template.) Tj ET

BT /F2 10.5 Tf 40 477 Td (B. 3D WebGL Mathematical Reconstruction (Three.js r160):) Tj ET
BT /F1 9.5 Tf 50 463 Td (- Reconstructed the Interactive 3D Earth (assets/globe.js) with quadratic Bezier trade routes) Tj ET
BT /F1 9.5 Tf 50 450 Td (  connecting Chinese hubs (Shanghai, Yiwu, Guangzhou) to Indian ports (Nhava Sheva, Chennai).) Tj ET
BT /F1 9.5 Tf 50 437 Td (- Engineered the 700vh Ocean Voyage (assets/voyage.js) with procedural GLSL water waves,) Tj ET
BT /F1 9.5 Tf 50 424 Td (  physical atmospheric sky lighting, container ship with livery, and working port gantry cranes.) Tj ET

BT /F2 10.5 Tf 40 404 Td (C. Client-Side Data Architecture & Zero-Build Runtime:) Tj ET
BT /F1 9.5 Tf 50 390 Td (- Structured an in-memory client database (assets/posts.js) containing 8 technical import guides.) Tj ET
BT /F1 9.5 Tf 50 377 Td (- Implemented instant live search, category tab filtering, pagination, and dynamic TOC generation.) Tj ET
BT /F1 9.5 Tf 50 364 Td (- Engineered interactive 3D perspective card tilt with mouse-tracking radial glare (--mx, --my).) Tj ET
BT /F1 9.5 Tf 50 351 Td (- Integrated quote inquiry form directly encoding RFQ parameters into WhatsApp (wa.me/919989724320).) Tj ET

0.89 0.14 0.11 rg 40 327 4 14 re f
0.04 0.04 0.04 rg
BT /F2 14 Tf 50 329 Td (3. Codebase Architecture & File Structure) Tj ET

0.96 0.96 0.96 rg 40 200 515 115 re f
0.85 0.85 0.85 RG 40 200 515 115 re S
0.04 0.04 0.04 rg
BT /F2 9.5 Tf 50 295 Td (File / Path) Tj 170 295 Td (Technology) Tj 270 295 Td (Description) Tj ET
0.7 0.7 0.7 RG 50 290 495 0.5 re S
BT /F2 9 Tf 50 275 Td (index.html) Tj /F1 9 Tf 170 275 Td (HTML5 Semantic) Tj 270 275 Td (Landing page: Hero, 3D Voyage, Products, FAQ, Contact) Tj ET
BT /F2 9 Tf 50 260 Td (blog.html) Tj /F1 9 Tf 170 260 Td (HTML5 / Vanilla JS) Tj 270 260 Td (Knowledge Hub: instant search, 8 category filters, pagination) Tj ET
BT /F2 9 Tf 50 245 Td (post.html) Tj /F1 9 Tf 170 245 Td (HTML5 / Vanilla JS) Tj 270 245 Td (Dynamic reader: automated Table of Contents & social share) Tj ET
BT /F2 9 Tf 50 230 Td (assets/site.css) Tj /F1 9 Tf 170 230 Td (CSS3 Modern) Tj 270 230 Td (Design tokens, 3D card tilt glare, responsive media queries) Tj ET
BT /F2 9 Tf 50 215 Td (assets/globe.js) Tj /F1 9 Tf 170 215 Td (Three.js r160) Tj 270 215 Td (3D Earth, quadratic Bezier routes, pulse glow, pin badges) Tj ET
BT /F2 9 Tf 50 205 Td (assets/voyage.js) Tj /F1 9 Tf 170 205 Td (Three.js WebGL) Tj 270 205 Td (700vh scroll ocean voyage, STS gantry cranes, milestone tracker) Tj ET

0.6 0.6 0.6 rg
BT /F1 8 Tf 40 50 Td (ImportNow AI Executive Screening Assignment | Candidate: Premsai | Page 1 of 2) Tj ET
"""
pdf.create_page(c1)

# Page 2 content
c2 = """
0.89 0.14 0.11 rg 40 800 515 3 re f
0.04 0.04 0.04 rg
BT /F2 16 Tf 40 765 Td (Technical Deep-Dive & Key Component Features) Tj ET

0.89 0.14 0.11 rg 40 740 4 14 re f
0.04 0.04 0.04 rg
BT /F2 13 Tf 50 742 Td (4. Interactive 3D WebGL Innovations) Tj ET

BT /F2 10.5 Tf 40 720 Td (1. Interactive 3D Trade Route Globe (assets/globe.js):) Tj ET
0.2 0.2 0.2 rg
BT /F1 9.5 Tf 50 706 Td (- Dotted sphere projection rendered with ACESFilmicToneMapping and custom atmosphere rim shader.) Tj ET
BT /F1 9.5 Tf 50 693 Td (- Quadratic Bezier arcs connecting Chinese export centers (Shanghai, Yiwu, Guangzhou) with Indian ports.) Tj ET
BT /F1 9.5 Tf 50 680 Td (- Mathematical unprojection converts 3D vector coordinates into responsive 2D screen badges with country flags.) Tj ET
BT /F1 9.5 Tf 50 667 Td (- Drag-to-rotate inertia controls with smooth auto-drift damping.) Tj ET

0.04 0.04 0.04 rg
BT /F2 10.5 Tf 40 647 Td (2. 700vh Scroll-Driven Ocean Voyage (assets/voyage.js):) Tj ET
0.2 0.2 0.2 rg
BT /F1 9.5 Tf 50 633 Td (- Procedural Three.js Water displacement shader with specular reflections and realistic water normals.) Tj ET
BT /F1 9.5 Tf 50 620 Td (- Physical Rayleigh and Mie atmospheric scattering sky model with animated sun positioning.) Tj ET
BT /F1 9.5 Tf 50 607 Td (- Fully procedural container ship with bulbous bow, deckhouse bridge, radar, and ImportNow livery.) Tj ET
BT /F1 9.5 Tf 50 594 Td (- Animated STS harbor gantry cranes with trolleys, spreader beams, and cables loading/unloading cargo.) Tj ET
BT /F1 9.5 Tf 50 581 Td (- 6-stage milestone tracker (Day 0 to Day 30+) with real-time ship wake foam and telemetry.) Tj ET

0.89 0.14 0.11 rg 40 555 4 14 re f
0.04 0.04 0.04 rg
BT /F2 13 Tf 50 557 Td (5. Fresher Perspective: Problem Solving & Agility) Tj ET

0.96 0.96 0.96 rg 40 470 515 75 re f
0.89 0.14 0.11 RG 40 470 3 75 re f S
0.2 0.2 0.2 rg
BT /F2 10 Tf 55 528 Td ("As an entry-level candidate, this challenge was an exciting opportunity to demonstrate not just") Tj ET
BT /F2 10 Tf 55 514 Td ("theoretical familiarity with AI tools, but the real-world ability to orchestrate agents, inspect code,") Tj ET
BT /F2 10 Tf 55 500 Td ("debug 3D WebGL edge-cases, and deliver a production-ready application within the deadline.") Tj ET
BT /F1 9 Tf 55 484 Td (— Premsai, AI Executive Candidate) Tj ET

BT /F2 10 Tf 40 450 Td (Key Strengths Demonstrated in this Assignment:) Tj ET
0.2 0.2 0.2 rg
BT /F1 9.5 Tf 50 435 Td (- Fast Learning Agility: Mastered Three.js WebGL shaders and coordinate unprojection rapidly.) Tj ET
BT /F1 9.5 Tf 50 422 Td (- Problem Solving: Diagnosed and solved complex DOM serialization edge cases and layout shifts.) Tj ET
BT /F1 9.5 Tf 50 409 Td (- Architecture: Zero external build dependencies using native browser Import Maps for instant load.) Tj ET
BT /F1 9.5 Tf 50 396 Td (- Rigorous Verification: Version-controlled in Git, tested cross-browser, and hosted live.) Tj ET

0.89 0.14 0.11 rg 40 368 4 14 re f
0.04 0.04 0.04 rg
BT /F2 13 Tf 50 370 Td (6. Conclusion & Submission Sign-Off) Tj ET

0.2 0.2 0.2 rg
BT /F1 9.5 Tf 40 348 Td (The complete codebase has been committed and pushed to GitHub, with the live deployment verified.) Tj ET
BT /F1 9.5 Tf 40 335 Td (I look forward to discussing the architecture, design choices, and AI implementation in the interview.) Tj ET

BT /F2 10 Tf 40 305 Td (Submission Package Checklist:) Tj ET
BT /F1 9.5 Tf 50 290 Td ([x] Live Website URL: https://premsai19.github.io/importnow-replica/) Tj ET
BT /F1 9.5 Tf 50 277 Td ([x] Public GitHub Repository: https://github.com/Premsai19/importnow-replica) Tj ET
BT /F1 9.5 Tf 50 264 Td ([x] PDF Technical Workflow Explanation (This document)) Tj ET
BT /F1 9.5 Tf 50 251 Td ([x] Direct Submission Email to Sabiya@importnow.in) Tj ET

0.04 0.04 0.04 rg
BT /F2 10.5 Tf 40 215 Td (Sincerely,) Tj ET
BT /F2 11 Tf 40 198 Td (Premsai) Tj ET
0.3 0.3 0.3 rg
BT /F1 9.5 Tf 40 184 Td (Aspiring AI Executive) Tj ET
BT /F1 9.5 Tf 40 171 Td (Email: maheshmannef4@gmail.com | GitHub: github.com/Premsai19) Tj ET

0.6 0.6 0.6 rg
BT /F1 8 Tf 40 50 Td (ImportNow AI Executive Screening Assignment | Candidate: Premsai | Page 2 of 2) Tj ET
"""
pdf.create_page(c2)

pdf.save()
print("PDF generated successfully!")
