---
{
  "projection_kind": "taulib_declaration",
  "title": "yukawa_full_top",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-full-top/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.EWSynthesis`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWSynthesis::yukawa_full_top",
  "declaration_slug": "yukawa-full-top",
  "kind": "def",
  "name": "yukawa_full_top",
  "module_name": "TauLib.BookIV.Electroweak.EWSynthesis",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/",
  "source_line_start": 85,
  "source_line_end": 90,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L85-L90",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L85-L90",
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
- Source path: [`TauLib/BookIV/Electroweak/EWSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L85-L90)
- Source range: L85-L90
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Top quark: generation 3, y_t ≈ 0.995. -/
```

## Source Excerpt

```lean
def yukawa_full_top : YukawaCouplingFull where
  flavor := "top"
  generation := 3
  coupling_numer := 995000
  coupling_denom := 1000000
  gen_valid := ⟨by omega, by omega⟩
```
