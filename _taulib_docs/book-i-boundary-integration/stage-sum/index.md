---
{
  "projection_kind": "taulib_declaration",
  "title": "stage_sum",
  "permalink": "/verify/taulib/docs/book-i-boundary-integration/stage-sum/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Integration`.",
  "declaration_id": "TauLib.BookI.Boundary.Integration::stage_sum",
  "declaration_slug": "stage-sum",
  "kind": "def",
  "name": "stage_sum",
  "module_name": "TauLib.BookI.Boundary.Integration",
  "module_url": "/verify/taulib/docs/book-i-boundary-integration/",
  "source_line_start": 39,
  "source_line_end": 45,
  "registry_ids": [
    "I.D99"
  ],
  "related_registry_items": [
    {
      "id": "I.D99",
      "title": "τ-Integral",
      "url": "/registry/object/I.D99/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L39-L45",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Integration",
        "url": "/verify/taulib/docs/book-i-boundary-integration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L39-L45",
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

- Module: [TauLib.BookI.Boundary.Integration](/verify/taulib/docs/book-i-boundary-integration/)
- Source path: [`TauLib/BookI/Boundary/Integration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L39-L45)
- Source range: L39-L45
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D99` — τ-Integral

## Immediate Comment / Docstring

```lean
/-- [I.D99] Sum a function over Z/M_k Z. -/
```

## Source Excerpt

```lean
def stage_sum (f : Nat → Int) (k : Nat) : Int :=
  go 0 (primorial k) (0 : Int)
where
  go (x bound : Nat) (acc : Int) : Int :=
    if x >= bound then acc
    else go (x + 1) bound (acc + f x)
  termination_by bound - x
```
