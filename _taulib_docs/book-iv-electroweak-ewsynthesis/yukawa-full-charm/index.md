---
{
  "projection_kind": "taulib_declaration",
  "title": "yukawa_full_charm",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-full-charm/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.EWSynthesis`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWSynthesis::yukawa_full_charm",
  "declaration_slug": "yukawa-full-charm",
  "kind": "def",
  "name": "yukawa_full_charm",
  "module_name": "TauLib.BookIV.Electroweak.EWSynthesis",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/",
  "source_line_start": 101,
  "source_line_end": 106,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L101-L106",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWSynthesis",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L101-L106",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIV.Electroweak.EWSynthesis](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/)
- Source path: [`TauLib/BookIV/Electroweak/EWSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L101-L106)
- Source range: L101-L106
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Charm quark: generation 2, y_c ≈ 0.0072. -/
```

## Source Excerpt

```lean
def yukawa_full_charm : YukawaCouplingFull where
  flavor := "charm"
  generation := 2
  coupling_numer := 7200
  coupling_denom := 1000000
  gen_valid := ⟨by omega, by omega⟩
```
