---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_sprint4",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/remark-sprint4/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::remark_sprint4",
  "declaration_slug": "remark-sprint4",
  "kind": "def",
  "name": "remark_sprint4",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 491,
  "source_line_end": 495,
  "registry_ids": [
    "V.R372"
  ],
  "related_registry_items": [
    {
      "id": "V.R372",
      "title": "Sprint 4 Findings and OQ-C3 Status",
      "url": "/registry/object/V.R372/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L491-L495",
  "formal_status": "defined",
  "declaration_role": "docstring/data record",
  "formal_status_label": "docstring/data record",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L491-L495",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "docstring/data record",
      "status": "docstring/data record"
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L491-L495)
- Source range: L491-L495
- Kind: `def`
- Public role: `docstring/data record`
- Formal status hint: `docstring/data record`

## Registry Links

- `V.R372` — Sprint 4 Findings and OQ-C3 Status

## Immediate Comment / Docstring

```lean
/-- [V.R372] Sprint 4 OQ-C3 status.
    Upgraded to tau-effective for mass hierarchy and ratio.
    Remaining open: first-principles exponent derivation, full PMNS, CP phase. -/
```

## Source Excerpt

```lean
def remark_sprint4 : String :=
  "Sprint 4 complete. OQ-C3 upgraded to tau-effective. " ++
  "Ratio 32.82 (PDG 32.58, 0.75%), Sigma_mnu=0.089 eV<0.12 eV. " ++
  "Normal ordering: structural (c>a). Majorana: structural (tau^1 self-dual). " ++
  "Open: exponent derivation, full PMNS, CP phase, absolute scale."
```
