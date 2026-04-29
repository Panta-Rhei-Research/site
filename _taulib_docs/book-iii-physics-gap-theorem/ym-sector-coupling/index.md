---
{
  "projection_kind": "taulib_declaration",
  "title": "ym_sector_coupling",
  "permalink": "/verify/taulib/docs/book-iii-physics-gap-theorem/ym-sector-coupling/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.GapTheorem`.",
  "declaration_id": "TauLib.BookIII.Physics.GapTheorem::ym_sector_coupling",
  "declaration_slug": "ym-sector-coupling",
  "kind": "def",
  "name": "ym_sector_coupling",
  "module_name": "TauLib.BookIII.Physics.GapTheorem",
  "module_url": "/verify/taulib/docs/book-iii-physics-gap-theorem/",
  "source_line_start": 166,
  "source_line_end": 169,
  "registry_ids": [
    "III.D46"
  ],
  "related_registry_items": [
    {
      "id": "III.D46",
      "title": "Strong Defect Functional",
      "url": "/registry/object/III.D46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L166-L169",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.GapTheorem",
        "url": "/verify/taulib/docs/book-iii-physics-gap-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L166-L169",
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

- Module: [TauLib.BookIII.Physics.GapTheorem](/verify/taulib/docs/book-iii-physics-gap-theorem/)
- Source path: [`TauLib/BookIII/Physics/GapTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L166-L169)
- Source range: L166-L169
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D46` — Strong Defect Functional

## Immediate Comment / Docstring

```lean
/-- [III.D46] YM sector coupling at level k: the ratio B-product / C-product
    (integer division). Measures the degree of B/C asymmetry. -/
```

## Source Excerpt

```lean
def ym_sector_coupling (k : TauIdx) : TauIdx :=
  let bp := split_zeta_b k
  let cp := split_zeta_c k
  if cp == 0 then 0 else bp / cp
```
