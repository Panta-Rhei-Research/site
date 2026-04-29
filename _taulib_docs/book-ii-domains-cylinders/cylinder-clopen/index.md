---
{
  "projection_kind": "taulib_declaration",
  "title": "cylinder_clopen",
  "permalink": "/verify/taulib/docs/book-ii-domains-cylinders/cylinder-clopen/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.Cylinders`.",
  "declaration_id": "TauLib.BookII.Domains.Cylinders::cylinder_clopen",
  "declaration_slug": "cylinder-clopen",
  "kind": "def",
  "name": "cylinder_clopen",
  "module_name": "TauLib.BookII.Domains.Cylinders",
  "module_url": "/verify/taulib/docs/book-ii-domains-cylinders/",
  "source_line_start": 76,
  "source_line_end": 80,
  "registry_ids": [
    "II.D11"
  ],
  "related_registry_items": [
    {
      "id": "II.D11",
      "title": "Clopen Basis",
      "url": "/registry/object/II.D11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L76-L80",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.Cylinders",
        "url": "/verify/taulib/docs/book-ii-domains-cylinders/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L76-L80",
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

- Module: [TauLib.BookII.Domains.Cylinders](/verify/taulib/docs/book-ii-domains-cylinders/)
- Source path: [`TauLib/BookII/Domains/Cylinders.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L76-L80)
- Source range: L76-L80
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D11` — Clopen Basis

## Immediate Comment / Docstring

```lean
/-- [II.D11] Every cylinder domain is clopen by construction.
    Basic cylinders: defined by finitely many modular conditions (open)
    and complement is a finite union of cylinders (closed).
    Boolean operations preserve clopenness. -/
```

## Source Excerpt

```lean
def cylinder_clopen : CylinderDomain → Bool
  | .basic k c => primorial k > 0 && reduce c k < primorial k
  | .inter a b => cylinder_clopen a && cylinder_clopen b
  | .union a b => cylinder_clopen a && cylinder_clopen b
  | .compl a   => cylinder_clopen a
```
