---
{
  "projection_kind": "taulib_declaration",
  "title": "agency_generator_match",
  "permalink": "/corpus/taulib/docs/book-vi-agency-agency-sector/agency-generator-match/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Agency.AgencySector`.",
  "declaration_id": "TauLib.BookVI.Agency.AgencySector::agency_generator_match",
  "declaration_slug": "agency-generator-match",
  "kind": "theorem",
  "name": "agency_generator_match",
  "module_name": "TauLib.BookVI.Agency.AgencySector",
  "module_url": "/corpus/taulib/docs/book-vi-agency-agency-sector/",
  "source_line_start": 55,
  "source_line_end": 57,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L55-L57",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Agency.AgencySector",
        "url": "/corpus/taulib/docs/book-vi-agency-agency-sector/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L55-L57",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookVI.Agency.AgencySector](/corpus/taulib/docs/book-vi-agency-agency-sector/)
- Source path: [`TauLib/BookVI/Agency/AgencySector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L55-L57)
- Source range: L55-L57
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Agency sector matches the FourPlusOne agency_sector definition. -/
```

## Source Excerpt

```lean
theorem agency_generator_match :
    agency_def.generator = agency_sector.generator :=
  rfl
```
