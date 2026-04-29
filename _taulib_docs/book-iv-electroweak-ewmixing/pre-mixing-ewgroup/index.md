---
{
  "projection_kind": "taulib_declaration",
  "title": "PreMixingEWGroup",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/pre-mixing-ewgroup/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::PreMixingEWGroup",
  "declaration_slug": "pre-mixing-ewgroup",
  "kind": "structure",
  "name": "PreMixingEWGroup",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 104,
  "source_line_end": 113,
  "registry_ids": [
    "IV.D128"
  ],
  "related_registry_items": [
    {
      "id": "IV.D128",
      "title": "Pre-Mixing Electroweak Gauge Group",
      "url": "/registry/object/IV.D128/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L104-L113",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWMixing",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L104-L113",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L104-L113)
- Source range: L104-L113
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D128` — Pre-Mixing Electroweak Gauge Group

## Immediate Comment / Docstring

```lean
/-- [IV.D128] The pre-mixing electroweak gauge group G_EW = SU(2)_L × U(1)_Y.
    In the τ-framework, this is the product of sector A (weak/SU(2))
    and the U(1) subgroup of sector B (electromagnetic).
    This group acts BEFORE mixing produces the physical bosons. -/
```

## Source Excerpt

```lean
structure PreMixingEWGroup where
  /-- The weak (SU(2)_L) sector. -/
  weak_sector : Sector
  /-- The hypercharge U(1)_Y component. -/
  hypercharge_sector : Sector
  /-- Weak is sector A. -/
  weak_is_A : weak_sector = .A
  /-- Hypercharge derives from sector B. -/
  hyper_is_B : hypercharge_sector = .B
  deriving Repr
```
