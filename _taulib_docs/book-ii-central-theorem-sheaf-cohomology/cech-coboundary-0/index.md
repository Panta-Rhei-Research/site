---
{
  "projection_kind": "taulib_declaration",
  "title": "cech_coboundary_0",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/cech-coboundary-0/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.SheafCohomology`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.SheafCohomology::cech_coboundary_0",
  "declaration_slug": "cech-coboundary-0",
  "kind": "def",
  "name": "cech_coboundary_0",
  "module_name": "TauLib.BookII.CentralTheorem.SheafCohomology",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/",
  "source_line_start": 57,
  "source_line_end": 58,
  "registry_ids": [
    "II.D86"
  ],
  "related_registry_items": [
    {
      "id": "II.D86",
      "title": "Čech Complex",
      "url": "/registry/object/II.D86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L57-L58",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.SheafCohomology",
        "url": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L57-L58",
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

- Module: [TauLib.BookII.CentralTheorem.SheafCohomology](/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/)
- Source path: [`TauLib/BookII/CentralTheorem/SheafCohomology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L57-L58)
- Source range: L57-L58
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D86` — Čech Complex

## Immediate Comment / Docstring

```lean
/-- [II.D86] Čech coboundary δ⁰: (δ⁰ f)(a,b) = f(b) - f(a).
    For cylinders at the same stage, intersections are empty unless a = b
    (ultrametric property), so δ⁰ is the difference map. -/
```

## Source Excerpt

```lean
def cech_coboundary_0 (f : Nat → Int) (k : Nat) (a b : Nat) : Int :=
  cech_cochain f k b - cech_cochain f k a
```
