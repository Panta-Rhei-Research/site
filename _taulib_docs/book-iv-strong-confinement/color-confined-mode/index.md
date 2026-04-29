---
{
  "projection_kind": "taulib_declaration",
  "title": "ColorConfinedMode",
  "permalink": "/verify/taulib/docs/book-iv-strong-confinement/color-confined-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.Confinement`.",
  "declaration_id": "TauLib.BookIV.Strong.Confinement::ColorConfinedMode",
  "declaration_slug": "color-confined-mode",
  "kind": "structure",
  "name": "ColorConfinedMode",
  "module_name": "TauLib.BookIV.Strong.Confinement",
  "module_url": "/verify/taulib/docs/book-iv-strong-confinement/",
  "source_line_start": 71,
  "source_line_end": 78,
  "registry_ids": [
    "IV.D159"
  ],
  "related_registry_items": [
    {
      "id": "IV.D159",
      "title": "Color-confined mode",
      "url": "/registry/object/IV.D159/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L71-L78",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.Confinement",
        "url": "/verify/taulib/docs/book-iv-strong-confinement/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L71-L78",
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

- Module: [TauLib.BookIV.Strong.Confinement](/verify/taulib/docs/book-iv-strong-confinement/)
- Source path: [`TauLib/BookIV/Strong/Confinement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L71-L78)
- Source range: L71-L78
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D159` — Color-confined mode

## Immediate Comment / Docstring

```lean
/-- [IV.D159] A mode chi_{m,n} is color-confined if:
    1. n not equiv 0 mod 3 (fractional eta-holonomy)
    2. The associated boundary character fails to converge in H_partial[omega]
    Confinement = non-convergence in the profinite limit. -/
```

## Source Excerpt

```lean
structure ColorConfinedMode where
  /-- Eta-winding (not divisible by 3). -/
  eta_winding_mod3 : Nat
  /-- Non-zero mod 3 condition. -/
  fractional : Bool
  /-- Fails to converge in profinite limit. -/
  non_convergent : Bool := true
  deriving Repr
```
